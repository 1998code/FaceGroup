# 人臉分組工具 (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

此工具可以自動識別圖像中的人臉並將其分組到不同的文件夾中。

## 運行要求

- **操作系統:** macOS, Linux, 或 Windows
- **Python 版本:** `3.11.9` (見 `.python-version`)
- **核心庫:** `face_recognition`, `opencv-python`, `numpy`

## 安裝與設置

1. 安裝依賴項:
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. 將您的圖像放入名為 `input_images` 的文件夾中。

3. 運行腳本:
   ```bash
   python face_grouper.py
   ```

## 工作原理

該腳本將執行以下操作：
1. 掃描 `input_images` 目錄中的所有圖像。
2. 檢測人臉並為每個人生成唯一的特徵簽名。
3. 在 `output_groups` 中為每個檢測到的人創建文件夾。
4. 將圖像複製到相應的文件夾中。

*注意：如果一張圖像中包含多個人，它將被複製到每個檢測到的人的文件夾中。*
