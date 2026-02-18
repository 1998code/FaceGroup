# Face Grouper

![Face Grouper Cover](Cover.png)

| [English](README.md) | [廣東話](readme/README.yue.md) | [繁體中文](readme/README.zh-TW.md) | [简体中文](readme/README.zh.md) | [日本語](readme/README.ja.md) | [한국어](readme/README.ko.md) | [Français](readme/README.fr.md) | [Español](readme/README.es.md) | [Indonesian](readme/README.id.md) | [हिन्दी](readme/README.hi.md) | [Tiếng Việt](readme/README.vi.md) | [ภาษาไทย](readme/README.th.md) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

This tool automatically recognizes faces in images and groups them into folders.

## Requirements

- **Operating System:** macOS, Linux, or Windows
- **Python Version:** `3.11.9` (as specified in `.python-version`)
- **Core Libraries:** `face_recognition`, `opencv-python`, `numpy`

## Setup

1. Install dependencies:
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. Place your images in a folder named `input_images`.

3. Run the tool:
   - **Modern UI (Recommended):**
     ```bash
     python app.py
     ```
   - **Command Line:**
     ```bash
     python face_grouper.py
     ```

## How it works

1. **Scan**: Scans all images in `input_images`.
2. **Detect**: Uses AI to detect faces and generate unique signatures.
3. **Group**: Clusters similar faces based on your preferred strictness.
4. **Organize**: Creates folders in `output_groups` and copies images into them.
5. **UI**: If using `app.py`, you can see a gallery of detected unique people in real-time.

*Note: If an image contains multiple people, it will be copied into the folder of each person detected.*
