import os
import re
from pathlib import Path


def get_next_filename(base_filename, current_number, original_ext):
    m = re.match(r'(.*\D)(\d+)(_.*)', base_filename)
    if not m:
        raise ValueError("Invalid format for the base filename")
    prefix, num, suffix = m.groups()

    # Check if the file extension is already in the base filename
    if not base_filename.lower().endswith(original_ext.lower()):
        suffix += original_ext

    return f"{prefix}{int(num) + current_number:05}{suffix}"

def remove_file_extension(first_filename):
    return re.sub(r'\.png|\.jpg|\.jpeg', '', first_filename, flags=re.IGNORECASE)


def rename_files_in_folder(folder, first_filename):
    file_extensions = ('.png', '.jpg', '.jpeg')
    files = sorted([f for f in os.listdir(folder) if f.lower().endswith(file_extensions)])

    if not files:
        print(f"No files with extensions {file_extensions} found in the folder")
        return

    counts = {ext: 0 for ext in file_extensions}
    skipped_files = 0

    original_ext = Path(files[0]).suffix
    entered_ext = Path(first_filename).suffix.lower()

    if entered_ext not in file_extensions:
        if entered_ext != "":
            print(
                f"Invalid file extension entered: {entered_ext}. Using the original file extension {original_ext} for renaming.")
        else:
            print(f"No file extension entered. Using the original file extension {original_ext} for renaming.")
        first_filename = remove_file_extension(first_filename) + original_ext
    elif entered_ext != original_ext.lower():
        print(
            f"Entered file extension {entered_ext} doesn't match the original file extension {original_ext}. Using the original file extension for renaming.")
        first_filename = remove_file_extension(first_filename) + original_ext

    os.rename(os.path.join(folder, files[0]), os.path.join(folder, first_filename))
    print(f"Renamed {files[0]} to {first_filename}")
    counts[original_ext.lower()] += 1

    for i, file in enumerate(files[1:], start=1):
        original_ext = Path(file).suffix
        new_filename = get_next_filename(first_filename, i, original_ext)
        counts[original_ext.lower()] += 1
        os.rename(os.path.join(folder, file), os.path.join(folder, new_filename))
        print(f"Renamed {file} to {new_filename}")

    total_renamed = sum(counts.values())
    print(f"Job completed. {total_renamed} files successfully renamed:")
    for ext, count in counts.items():
        print(f"- {count } {ext[1:]} files")
    print(f"- {skipped_files} files skipped")


def main():
    folder = input("Enter the folder path (leave empty for the current folder): ")
    first_filename = input("Enter the first file's new name: ")

    if not folder:
        folder = os.getcwd()

    folder = Path(folder)
    if not folder.is_dir():
        print(f"{folder} is not a valid directory. Please start over.")
        return

    rename_files_in_folder(folder, first_filename)


if __name__ == "__main__":
    main()

