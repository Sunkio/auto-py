import os
import sys
from pathlib import Path
from PIL import Image
import img2pdf

def convert_image(input_file, output_format):
    input_path = Path(input_file)
    output_dir = input_path.parent / input_path.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{input_path.stem}.{output_format.lower()}"

    if output_format.lower() == "pdf":
        with open(output_file, "wb") as f:
            f.write(img2pdf.convert(input_file))
    else:
        im = Image.open(input_file)
        
        if output_format.lower() in ["jpeg", "eps"] and im.mode == "RGBA":
            im = im.convert("RGB")
        
        im.save(output_file, output_format.upper())

def main():
    formats = ["png", "jpeg", "pdf", "eps"]
    print("Supported formats: ", ", ".join(formats))

    input_files = input("Enter the file path(s) or directory (separated by commas): ").strip().split(",")

    conversion_mode = input("Enter the output format(s) or 'all' for all formats: ").strip().lower()

    if conversion_mode == "all":
        target_formats = formats
    else:
        target_formats = [f.strip() for f in conversion_mode.split(",")]

    for input_file in input_files:
        input_file = input_file.strip()

        if os.path.isdir(input_file):
            for file in os.listdir(input_file):
                if file.lower().endswith((".png", ".jpeg", ".jpg")):
                    for target_format in target_formats:
                        convert_image(os.path.join(input_file, file), target_format)
        elif os.path.isfile(input_file) and input_file.lower().endswith((".png", ".jpeg", ".jpg")):
            for target_format in target_formats:
                convert_image(input_file, target_format)
        else:
            print(f"Invalid file or directory: {input_file}")

if __name__ == "__main__":
    main()