import os
import re
from pathlib import Path


def get_next_filename(base_filename, current_number):
    m = re.match(r'(.*\D)(\d+)(_.*)', base_filename)
    if not m:
        raise ValueError("Invalid format for the base filename")
    prefix, num, suffix = m.groups()
    return f"{prefix}{int(num) + current_number:05}{suffix}"


def rename_files_in_folder(folder, first_filename):
    file_extensions = ('.png', '.jpg', '.jpeg')
    files = sorted([f for f in os.listdir(folder) if f.lower().endswith(file_extensions)])

    if not files:
        print(f"No files with extensions {file_extensions} found in the folder")
        return

    os.rename(os.path.join(folder, files[0]), os.path.join(folder, first_filename))
    print(f"Renamed {files[0]} to {first_filename}")

    for i, file in enumerate(files[1:], start=1):
        new_filename = get_next_filename(first_filename, i)
        os.rename(os.path.join(folder, file), os.path.join(folder, new_filename))
        print(f"Renamed {file} to {new_filename}")


def main():
    folder = input("Enter the folder path (leave empty for the current folder): ")
    first_filename = input("Enter the first file's new name: ")

    if not folder:
        folder = os.getcwd()

    folder = Path(folder)
    if not folder.is_dir():
        print(f"{folder} is not a valid directory")
        return

    rename_files_in_folder(folder, first_filename)


if __name__ == "__main__":
    main()