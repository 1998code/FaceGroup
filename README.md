# Face Grouper

This tool automatically recognizes faces in images and groups them into folders.

## Setup

1. Install dependencies:
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. Place your images in a folder named `input_images`.

3. Run the script:
   ```bash
   python face_grouper.py
   ```

## How it works

The script will:
1. Scan all images in the `input_images` directory.
2. Detect faces and generate unique signatures for each person.
3. Create folders for each detected person in `output_groups`.
4. Copy the images into the corresponding folders.

*Note: If an image contains multiple people, it will be copied into the folder of each person detected.*
