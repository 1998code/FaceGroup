# 人脸分组工具 (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |

此工具可以自动识别图像中的人脸并将其分组到不同的文件夹中。

## 运行要求

- **操作系统:** macOS, Linux, 或 Windows
- **Python 版本:** `3.11.9` (见 `.python-version`)
- **核心库:** `face_recognition`, `opencv-python`, `numpy`, `gradio`

## GUI

![Face Grouper GUI](../GUI.png)

## 安装与运行

### 1. 安装
首先，确保您已设置虚拟环境并安装了所有依赖项。

#### macOS / Linux:
```bash
# 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
./venv/bin/python3 -m pip install -r requirements.txt
```

#### Windows:
```bash
# 创建并激活虚拟环境
python -m venv venv
.\venv\Scripts\activate

# 安装依赖
.\venv\Scripts\python -m pip install -r requirements.txt
```

### 2. 运行工具
我们建议使用现代 Web 界面以获得最佳体验。

#### 启动 Web GUI (推荐):
- **macOS / Linux:** `./venv/bin/python3 app.py`
- **Windows:** `.\venv\Scripts\python app.py`

#### 启动命令行版本:
- **macOS / Linux:** `./venv/bin/python3 face_grouper.py`
- **Windows:** `.\venv\Scripts\python face_grouper.py`

## 故障排除

### `ModuleNotFoundError: No module named 'face_recognition'`
这通常发生在您在虚拟环境之外运行脚本时。请务必使用虚拟环境的 python 路径：
- `macOS/Linux: ./venv/bin/python3 app.py`
- `Windows: .\venv\Scripts\python app.py`

### `zsh: command not found: python`
在 macOS 上，请使用 `python3` 而不是 `python`。

### 处理速度非常慢
人脸识别是 CPU 密集型的。关闭其他繁重的应用程序或使用具有更多内核的机器会有所帮助。

### 检测结果不佳
尝试调整 UI 中的 **Tolerance (Strictness)** 滑块：
- **较低 (例如 0.4):** 更严格。如果工具将不同的人混入一个文件夹，请使用此设置。
- **较高 (例如 0.6):** 更宽松。如果工具为同一个人创建了过多的文件夹，请使用此设置。

## 贡献

欢迎提供贡献！如果您想帮助改进此工具，请：
1. Fork 本仓库。
2. 为您的功能或错误修复创建一个新分支。
3. 提交拉取请求，并清楚说明您的更改。

## 工作原理

1. **扫描**: 扫描您指定的输入文件夹中的所有图像。
2. **检测**: 使用 AI 检测人脸并生成唯一的特征签名。
3. **分组**: 根据您喜欢的严格程度对相似的人脸进行聚类。
4. **整理**: 在输出目录中创建文件夹并将图像复制到其中。
5. **UI**: 显示检测到的唯一身份的实时画廊。

*注意：如果一张图像中包含多个人，它将被复制到每个检测到的人的文件夹中。*


## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](../LICENSE) 文件。