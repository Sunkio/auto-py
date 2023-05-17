from PIL import Image
import os

def process_images(width, height, oz_suffix):
    for file in os.listdir(source_folder):
        if file.endswith((".png", ".jpg", ".jpeg")):
            source_file = os.path.join(source_folder, file)
            source_image = Image.open(source_file)

            file_name = file.replace("_source-4x.png", "")

            source_image_ratio = source_image.width / source_image.height
            target_ratio = width / height

            if source_image_ratio < target_ratio:
                new_width = width
                new_height = int(width / source_image_ratio)
            else:
                new_width = int(height * source_image_ratio)
                new_height = height

            source_image_resized = source_image.resize((new_width, new_height), Image.LANCZOS)

            # STRAIGHT Skinny Tumbler
            straight_image = Image.new("RGB", (width, height), (255, 255, 255))
            straight_position = (
                (straight_image.width - source_image_resized.width) // 2,
                (straight_image.height - source_image_resized.height) // 2,
            )
            straight_image.paste(source_image_resized, straight_position)
            straight_image.info["dpi"] = (300, 300)
            straight_image.save(os.path.join(output_folder, f"{file_name}_STRAIGHT-{oz_suffix}.png"))

            # TAPERED Skinny Tumbler
            tapered_template = Image.open(f"tapered_template-{oz_suffix}.png").convert("RGBA")
            mask = tapered_template.split()[3]
            tapered_image = Image.composite(straight_image.convert("RGBA"), tapered_template, mask)
            tapered_image.info["dpi"] = (300, 300)
            tapered_image.save(os.path.join(output_folder, f"{file_name}_TAPERED-{oz_suffix}.png"))

            # Upscale source file to 300 DPI
            source_image_upscaled = source_image.copy()
            source_image_upscaled.info["dpi"] = (300, 300)
            source_image_upscaled.save(os.path.join(output_folder, f"{file_name}_square-pattern.png"))

print("Welcome to the Skinny Tumbler Image Processor!")

source_folder = input("Please enter the path to the source folder: ").strip()
output_folder = input("Please enter the path to the output folder: ").strip()

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print("Processing images...")

# Process 20 oz images
process_images(2790, 2460, "20-oz")

# Process 30 oz images
process_images(3000, 2820, "30-oz")

print("Image processing complete!")