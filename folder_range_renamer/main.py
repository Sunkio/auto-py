import os

def rename_folders(start_sku, end_sku, append_str, source_dir):
    start_num = int(start_sku[2:])
    end_num = int(end_sku[2:])
    prefix = start_sku[:2]
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
    source_dir = input("Enter the source directory (leave empty for current directory): ")
    if not source_dir:
        source_dir = "."

    i = 0

    while True:
        print("")  # Add an empty line for better readability
        start_sku = input("Enter the start SKU (leave empty to exit): ").strip()
        if not start_sku:
            break

        end_sku = input("Enter the end SKU (inclusive): ").strip()
        append_str = input("Enter the string to append to the folder name: ").strip()

        if i == 1:
            new_source_dir = input(f"Enter a new source directory or press Enter to use the same as before ({source_dir}): ").strip()
            if new_source_dir:
                source_dir = new_source_dir

        renamed_count = rename_folders(start_sku, end_sku, append_str, source_dir)
        print(f"Job completed. {renamed_count} folders have been renamed.")
        i = 1
