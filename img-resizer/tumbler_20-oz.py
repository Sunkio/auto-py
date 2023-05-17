from PIL import Image
import os

print("Welcome to the Skinny Tumbler Image Processor!")

source_folder = input("Please enter the path to the source folder: ").strip()
output_folder = input("Please enter the path to the output folder: ").strip()

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print("Processing images...")

for file in os.listdir(source_folder):
    if file.endswith((".png", ".jpg", ".jpeg")):
        source_file = os.path.join(source_folder, file)
        source_image = Image.open(source_file)

        file_name = file.replace("_source-4x.png", "")

        source_image_ratio = source_image.width / source_image.height
        target_ratio = 2790 / 2460

        if source_image_ratio < target_ratio:
            new_width = 2790
            new_height = int(2790 / source_image_ratio)
        else:
            new_width = int(2460 * source_image_ratio)
            new_height = 2460

        source_image_resized = source_image.resize((new_width, new_height), Image.LANCZOS)

        # STRAIGHT Skinny Tumbler
        straight_image = Image.new("RGB", (2790, 2460), (255, 255, 255))
        straight_position = (
            (straight_image.width - source_image_resized.width) // 2,
            (straight_image.height - source_image_resized.height) // 2,
        )
        straight_image.paste(source_image_resized, straight_position)
        straight_image.info["dpi"] = (300, 300)
        straight_image.save(os.path.join(output_folder, f"{file_name}_STRAIGHT-Skinny-Tumbler.png"))

        # TAPERED Skinny Tumbler
        tapered_template = Image.open("tapered_template-20-oz.png").convert("RGBA")
        mask = tapered_template.split()[3]
        tapered_image = Image.composite(straight_image.convert("RGBA"), tapered_template, mask)
        tapered_image.info["dpi"] = (300, 300)
        tapered_image.save(os.path.join(output_folder, f"{file_name}_TAPERED-Skinny-Tumbler.png"))

print("Image processing complete!")