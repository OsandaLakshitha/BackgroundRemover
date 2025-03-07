# Background Remover

## 📌 Description
This script removes the background from images in a given folder using `rembg` and saves the processed images in an output folder.

## 🚀 Features
- Processes all images from the source folder automatically.
- Supports multiple image formats: **PNG, JPG, JPEG, WEBP**.
- Saves the output images with transparent backgrounds.
- Uses command-line styled prints for better visibility.

## 🛠 Requirements
Make sure you have Python installed. Then, install the required dependencies:

```sh
pip install rembg pillow pyinstaller onnxruntime
```

## 🔧 Usage
1. Place all your images in the `source_images` folder.
2. Run the script:

```sh
python bgrm.py
```

3. The processed images will be saved in the `output_images` folder.


## 🖥️ Create an Executable (.exe) Yourself
If you want to generate an executable file manually, follow these steps:

1. Install PyInstaller:
   ```sh
   pip install pyinstaller
   ```

2. Navigate to the script's directory and run:
   ```sh
   pyinstaller --onefile --console bgrm.py
   ```

3. The `.exe` file will be created inside the `dist/` folder.

## 📂 Folder Structure
```
📁 background-remover
 ├── 📁 source_images    # Place input images here
 ├── 📁 output_images    # Processed images will be saved here
 ├── 📁 dist             # Contains the executable file
 ├── bgrm.py            # Background remover script
 ├── README.md          # Project documentation
```

## 👨‍💻 Author
**Osanda Lakshitha**  
GitHub: [YourGitHubLink](https://github.com/osandalakshitha)

## ✅ License
This project is open-source. Feel free to modify and use it!

