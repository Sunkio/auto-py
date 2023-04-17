import os
import glob
import pandas as pd
from PyPDF2 import PdfMerger
import shutil
from odf.opendocument import load
from odf import text, teletype

# Function to interactively get input with a default value
def get_input(prompt, default=None):
    result = input(f"{prompt} (default: {default}): ")
    return result.strip() or default

# Function to get output file name with the correct extension
def get_output_file_name(prompt, default, extension):
    while True:
        result = input(f"{prompt} (default: {default}): ").strip()
        if not result:
            return default
        if os.path.splitext(result)[1] == extension:
            return result
        print(f"Error: The output file extension must be {extension}. Please try again.")

# Get working directory and change to it
while True:
    working_dir = get_input("Enter the working directory", os.getcwd())
    if os.path.exists(working_dir):
        os.chdir(working_dir)
        break
    else:
        print("The entered working directory doesn't exist. Please try again.")

# Get the index setting for CSV and Excel files
index = get_input("Set index to true or false", "false").lower() == "true"

# Get output directory
output_dir = get_input("Enter the output directory", os.getcwd())

# Get the file type to be combined
file_type = get_input("Enter the file type to be combined (csv, xlsx, pdf, docx, odt)", "all")

# Get the specific files to be combined (comma-separated)
files_input = get_input("Enter the specific file names to be combined (comma-separated), or leave empty for all files", "").strip()
specified_files = [f.strip() for f in files_input.split(",")] if files_input else []

# Function to filter files based on user input
def filter_files(files):
    if specified_files:
        return [f for f in files if f in specified_files]
    return files

# Function to check if a PDF file is valid
def is_valid_pdf(file_path):
    try:
        with open(file_path, "rb") as f:
            PyPDF2.PdfFileReader(f)
        return True
    except PyPDF2.utils.PdfReadError:
        return False

# Initialize a flag to track if any files were combined
combined_any_files = False

# Combine CSV and Excel files
for ext, default_output_file in [('csv', 'combined_csv.csv'), ('xlsx', 'combined_excel.xlsx')]:
    if file_type != "all" and file_type != ext:
        continue
    all_filenames = filter_files([i for i in glob.glob(f'*.{ext}')])
    if not all_filenames:
        continue
    output_file = get_output_file_name(f"Enter the output {ext} file name", default_output_file, f".{ext}")
    combined_data = pd.concat([pd.read_csv(f) if ext == 'csv' else pd.read_excel(f) for f in all_filenames])
    output_path = os.path.join(output_dir, output_file)
    if ext == 'csv':
        combined_data.to_csv(output_path, index=index)
    else:
        combined_data.to_excel(output_path, index=index)
    combined_any_files = True

# Combine PDF files
if file_type in ["all", "pdf"]:
    pdf_files = filter_files([f for f in glob.glob('*.pdf') if is_valid_pdf(f)])
    if pdf_files:
        pdf_merger = PdfMerger()
        for pdf_file in pdf_files:
            pdf_merger.append(pdf_file)
        output_pdf_file = get_output_file_name("Enter the output PDF file name", "combined_pdf.pdf", ".pdf")
        output_pdf_path = os.path.join(output_dir, output_pdf_file)
        with open(output_pdf_path, "wb") as output_pdf:
            pdf_merger.write(output_pdf)
        combined_any_files = True

# Combine Word and LibreOffice Writer files
for ext, default_output_file in [('docx', 'combined_word.docx'), ('odt', 'combined_writer.odt')]:
    if file_type != "all" and file_type != ext:
        continue
    all_filenames = filter_files([i for i in glob.glob(f'*.{ext}')])
    if not all_filenames:
        continue
    output_file = get_output_file_name(f"Enter the output {ext} file name", default_output_file, f".{ext}")
    shutil.copy(all_filenames[0], output_file)
    for doc_file in all_filenames[1:]:
        os.system(f'pandoc {doc_file} -t {ext} -o temp.{ext}')
        os.system(f'pandoc temp.{ext} -t {ext} -o {output_file}')
    os.remove(f'temp.{ext}')
    shutil.move(output_file, os.path.join(output_dir, output_file))
    combined_any_files = True

if combined_any_files:
    print("Files combined successfully.")
else:
    print("No files of the specified file type were found, or an error occurred while combining files.")