from PIL import Image
import os

source_folder = "/home/tanja/gen_pop-mac-new/hustle/pod-designs/1_Tumbler-Designs/new-upscale-cyber-punk/toTumble"
output_folder = "/home/tanja/gen_pop-mac-new/hustle/pod-designs/1_Tumbler-Designs/new-upscale-cyber-punk/tumbled"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file in os.listdir(source_folder):
    if file.endswith((".png", ".jpg", ".jpeg")):
        source_file = os.path.join(source_folder, file)
        source_image = Image.open(source_file)

        file_name = file.replace("_source-4x.png", "")

        source_image_ratio = source_image.width / source_image.height
        target_ratio = 2790 / 2460

        if source_image_ratio < target_ratio:
            # Source image is taller, so resize based on width
            new_width = 2790
            new_height = int(2790 / source_image_ratio)
        else:
            # Source image is wider, so resize based on height
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
        mask = tapered_template.split()[3]  # Use the alpha channel of the tapered template as a mask
        tapered_image = Image.composite(straight_image.convert("RGBA"), tapered_template, mask)
        tapered_image.info["dpi"] = (300, 300)
        tapered_image.save(os.path.join(output_folder, f"{file_name}_TAPERED-Skinny-Tumbler.png"))