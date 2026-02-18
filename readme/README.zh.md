# 人脸分组工具 (Face Grouper)

![Face Grouper Cover](../Cover.png)

此工具可以自动识别图像中的人脸并将其分组到不同的文件夹中。

## 运行要求

- **操作系统:** macOS, Linux, 或 Windows
- **Python 版本:** `3.11.9` (见 `.python-version`)
- **核心库:** `face_recognition`, `opencv-python`, `numpy`

## 安装与设置

1. 安装依赖项:
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. 将您的图像放入名为 `input_images` 的文件夹中。

3. 运行脚本:
   ```bash
   python face_grouper.py
   ```

## 工作原理

该脚本将执行以下操作：
1. 扫描 `input_images` 目录中的所有图像。
2. 检测人脸并为每个人生成唯一的特征签名。
3. 在 `output_groups` 中为每个检测到的人创建文件夹。
4. 将图像复制到相应的文件夹中。

*注意：如果一张图像中包含多个人，它将被复制到每个检测到的人的文件夹中。*
