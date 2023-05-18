import os
import argparse

def rename_folders(start_skd, end_skd, append_str, source_dir):
    start_num = int(start_skd[2:])
    end_num = int(end_skd[2:])
    prefix = start_skd[:2]
    count = 0

    for folder_num in range(start_num, end_num + 1):
        original_folder = os.path.join(source_dir, f"{prefix}{str(folder_num).zfill(5)}")
        new_folder = os.path.join(source_dir, f"{prefix}{str(folder_num).zfill(5)}{append_str}")

        if os.path.exists(original_folder):
            os.rename(original_folder, new_folder)
            count += 1
            print(f"Renamed {original_folder} to {new_folder}")

    return count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename folders based on given start and end skd and string to append.")
    parser.add_argument("start_skd", help="The skd of the folder to start with")
    parser.add_argument("end_skd", help="The skd of the folder to end with (inclusive)")
    parser.add_argument("append_str", help="The string to append to the folder name")
    parser.add_argument("-s", "--source", dest="source_dir", default=".", help="The source directory where the folders to rename are located (default: current directory)")

    args = parser.parse_args()

    renamed_count = rename_folders(args.start_skd, args.end_skd, args.append_str, args.source_dir)
    print(f"Job completed. {renamed_count} folders have been renamed.")