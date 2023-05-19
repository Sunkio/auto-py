import os
import shutil
import re


def create_destination_directory(file_prefix, destination):
    parent_directory_path = os.path.join(destination, file_prefix)
    if not os.path.exists(parent_directory_path):
        os.makedirs(parent_directory_path)
        os.makedirs(os.path.join(parent_directory_path, 'mockups'))
        os.makedirs(os.path.join(parent_directory_path, 'mockups_work-files'))
        os.makedirs(os.path.join(parent_directory_path, 'bigjpg-upscaled-source'))
        same_name_directory_path = os.path.join(parent_directory_path, file_prefix)
        os.makedirs(same_name_directory_path)
        os.makedirs(os.path.join(same_name_directory_path, 'doubled-design_for-animated-mockups-etc'))
    return parent_directory_path


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
                    parent_directory = create_destination_directory(file_prefix, destination)
                    doubled_ext = ('.png', '.jpg', '.jpeg')
                    if file.endswith(tuple('_DOUBLED' + ext for ext in doubled_ext)):
                        dest_directory = os.path.join(parent_directory, file_prefix,
                                                      'doubled-design_for-animated-mockups-etc')
                    elif file.endswith(tuple('_source-4x' + ext for ext in doubled_ext)):
                        dest_directory = os.path.join(parent_directory, 'bigjpg-upscaled-source')
                    else:
                        dest_directory = os.path.join(parent_directory, file_prefix)

                    source_path = os.path.join(root, file)
                    dest_path = os.path.join(dest_directory, file)
                    shutil.copy2(source_path, dest_path)
                    print(f'Processed file: {file}')


def main():
    source_directories = [s.strip() for s in input("Enter the source directories (separated by comma): ").split(',')]
    destination_directory = input("Enter the destination directory: ")

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    print("Sorting files...")

    sort_files(source_directories, destination_directory)

    print("Sorting complete.")


if __name__ == "__main__":
    main()