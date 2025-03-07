import os
import time
from rembg import remove
from PIL import Image

def remove_background_from_folder(source_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    
    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'webp'))]
    total_images = len(image_files)

    print("\033[1;34m=================================================\033[0m")
    print("\033[1;32mMade By: Osanda Lakshitha\033[0m")
    print("\033[1;36mBackground Remover Script\033[0m")
    print("\033[1;33mGitHub: https://github.com/osandalakshitha\033[0m")
    print("\033[1;34m=================================================\033[0m")
    
    print(f"📂 Found {total_images} images in '{source_folder}'\n")
    
    if total_images == 0:
        print("⚠️ No images found! Please add images to the source folder and try again.\n")
        input("Press any key to exit...")
        return

    processed_count = 0
    for image_file in image_files:
        try:
            input_path = os.path.join(source_folder, image_file)
            output_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + "_no_bg.png")
            
            with Image.open(input_path) as img:
                img_no_bg = remove(img)
                img_no_bg.save(output_path, "PNG")
            
            print(f"✅ Processed: {image_file} -> {output_path}")
            processed_count += 1
        except Exception as e:
            print(f"❌ Error processing {image_file}: {e}")

    print("\n===================================")
    print(f"🎉 Successfully removed background from {processed_count}/{total_images} images!")
    print("===================================\n")

    input("Press any key to exit...")

if __name__ == "__main__":
    source_folder = "source_images"
    output_folder = "output_images"
    
    remove_background_from_folder(source_folder, output_folder)
