# 人臉分組工具 (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-TW.md) | [廣東話](README.yue.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

呢個工具可以自動識別圖像入面嘅人臉，並將佢哋分組到唔同嘅文件夾入面。

## 運行要求

- **操作系統:** macOS, Linux, 或 Windows
- **Python 版本:** `3.11.9` (見 `.python-version`)
- **核心庫:** `face_recognition`, `opencv-python`, `numpy`

## 安裝與設置

1. 安裝依賴項:
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. 將你嘅圖像放入名為 `input_images` 嘅文件夾入面。

3. 運行腳本:
   ```bash
   python face_grouper.py
   ```

## 工作原理

個腳本會咁樣做：
1. 掃描 `input_images` 目錄入面所有圖像。
2. 檢測人臉並為每個人生成唯一嘅特徵簽名。
3. 喺 `output_groups` 入面為每個檢測到嘅人創建文件夾。
4. 將圖像複製到相應嘅文件夾入面。

*注意：如果一張圖像入面有幾個人，佢會被複製到每個檢測到嘅人嘅文件夾入面。*
