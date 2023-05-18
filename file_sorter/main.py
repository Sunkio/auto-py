import os
import shutil
import sys
import re

def create_destination_directory(file_prefix, destination):
    directory_path = os.path.join(destination, file_prefix)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    return directory_path

def extract_prefix(file_name):
    match = re.match(r"([A-Za-z]+[0-9]+)", file_name)
    if match:
        return match.group(1)
    return None

def sort_files(source_directories, destination):
    for source in source_directories:
        for root, _, files in os.walk(source):
            for file in files:
                file_prefix = extract_prefix(file)
                if file_prefix:
                    dest_directory = create_destination_directory(file_prefix, destination)
                    source_path = os.path.join(root, file)
                    dest_path = os.path.join(dest_directory, file)
                    shutil.copy2(source_path, dest_path)
                    print(f'Processed file: {file}')

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <source_directory_1> [<source_directory_2>...] <destination_directory>")
        sys.exit(1)

    source_directories = sys.argv[1:-1]
    destination_directory = sys.argv[-1]

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    print("Sorting files...")

    sort_files(source_directories, destination_directory)

    print("Sorting complete.")

if __name__ == "__main__":
    main()