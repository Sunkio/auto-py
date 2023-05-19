import os
from PIL import Image

def double_image_horizontal(image_path):
    img = Image.open(image_path)
    width, height = img.size
    new_width = width * 2
    new_img = Image.new(img.mode, (new_width, height))
    new_img.paste(img, (0, 0))
    new_img.paste(img, (width, 0))
    return new_img

def process_images(source_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(source_folder):
        if file_name.endswith('.png'):
            source_file_path = os.path.join(source_folder, file_name)
            output_file_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '_DOUBLED.png')
            doubled_img = double_image_horizontal(source_file_path)
            doubled_img.save(output_file_path)

if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ")
    output_folder = input("Enter the output folder path: ")
    print("Images are being processed...")
    process_images(source_folder, output_folder)
    print("Images processed successfully.")