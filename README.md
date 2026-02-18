# Face Grouper

![Face Grouper Cover](Cover.png)

| [English](README.md) | [廣東話](readme/README.yue.md) | [繁體中文](readme/README.zh-TW.md) | [简体中文](readme/README.zh.md) | [日本語](readme/README.ja.md) | [한국어](readme/README.ko.md) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| [Français](readme/README.fr.md) | [Español](readme/README.es.md) | [Indonesian](readme/README.id.md) | [हिन्दी](readme/README.hi.md) | [Tiếng Việt](readme/README.vi.md) | [ภาษาไทย](readme/README.th.md) |

This tool automatically recognizes faces in images and groups them into folders.

## GUI

![Face Grouper GUI](GUI.png)

## Requirements

- **Operating System:** macOS, Linux, or Windows
- **Python Version:** `3.11.9`
- **Core Libraries:** `face_recognition`, `opencv-python`, `numpy`, `gradio`

## Setup & Execution

### 1. Installation
First, ensure you have a virtual environment set up and all dependencies installed.

#### macOS / Linux:
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
./venv/bin/python3 -m pip install -r requirements.txt
```

#### Windows:
```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install requirements
.\venv\Scripts\python -m pip install -r requirements.txt
```

### 2. Running the Tool
We recommend using the modern web interface for the best experience.

#### Launch Web UI (Recommended):
- **macOS / Linux:** `./venv/bin/python3 app.py`
- **Windows:** `.\venv\Scripts\python app.py`

#### Launch CLI Version:
- **macOS / Linux:** `./venv/bin/python3 face_grouper.py`
- **Windows:** `.\venv\Scripts\python face_grouper.py`

## Troubleshooting

### `ModuleNotFoundError: No module named 'face_recognition'`
This usually happens when you run the script outside of the virtual environment. Always make sure to use the path to the virtual environment's python:
- `macOS/Linux: ./venv/bin/python3 app.py`
- `Windows: .\venv\Scripts\python app.py`

### `zsh: command not found: python`
On macOS, use `python3` instead of `python`.

### Processing is very slow
Face recognition is CPU-intensive. Closing other heavy applications or using a machine with more cores will help.

### Poor detection results
Try adjusting the **Tolerance (Strictness)** slider in the UI:
- **Lower (e.g., 0.4):** More strict. Use this if the tool is mixing different people into one folder.
- **Higher (e.g., 0.6):** More loose. Use this if the tool is creating too many folders for the same person.

## Contributing

Contributions are welcome! If you'd like to help improve this tool, please:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a clear description of your changes.

Ways to contribute:
- Add support for more image formats.
- Improve face recognition accuracy or speed.
- Enhance the Gradio UI with more features.
- Translate the documentation into more languages.

## How it works

1. **Scan**: Scans all images in your specified input folder.
2. **Detect**: Uses AI to detect faces and generate unique signatures.
3. **Group**: Clusters similar faces based on your preferred strictness.
4. **Organize**: Creates folders in the output directory and copies images into them.
5. **UI**: Displays a real-time gallery of detected unique people.

*Note: If an image contains multiple people, it will be copied into the folder of each person detected.*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
