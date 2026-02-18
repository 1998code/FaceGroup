# 人臉分組工具 (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |

呢個工具可以自動識別圖像入面嘅人臉，並將佢哋分組到唔同嘅文件夾入面。

## 運行要求

- **操作系統:** macOS, Linux, 或 Windows
- **Python 版本:** `3.11.9` (見 `.python-version`)
- **核心庫:** `face_recognition`, `opencv-python`, `numpy`, `gradio`

## GUI

![Face Grouper GUI](../GUI.png)

## 安裝與運行

### 1. 安裝
首先，確保你已經設置好虛擬環境並安裝咗所有依賴項。

#### macOS / Linux:
```bash
# 創建並激活虛擬環境
python3 -m venv venv
source venv/bin/activate

# 安裝依賴
./venv/bin/python3 -m pip install -r requirements.txt
```

#### Windows:
```bash
# 創建並激活虛擬環境
python -m venv venv
.\venv\Scripts\activate

# 安裝依賴
.\venv\Scripts\python -m pip install -r requirements.txt
```

### 2. 運行工具
我哋建議使用現代 Web 界面以獲得最佳體驗。

#### 啟動 Web GUI (推薦):
- **macOS / Linux:** `./venv/bin/python3 app.py`
- **Windows:** `.\venv\Scripts\python app.py`

#### 啟動命令行版本:
- **macOS / Linux:** `./venv/bin/python3 face_grouper.py`
- **Windows:** `.\venv\Scripts\python face_grouper.py`

## 故障排除

### `ModuleNotFoundError: No module named 'face_recognition'`
呢個通常發生喺你喺虛擬環境之外運行腳本嘅時候。請務必使用虛擬環境嘅 python 路徑：
- `macOS/Linux: ./venv/bin/python3 app.py`
- `Windows: .\venv\Scripts\python app.py`

### `zsh: command not found: python`
喺 macOS 上，請使用 `python3` 而唔係 `python`。

### 處理速度非常慢
人臉識別係 CPU 密集型嘅。關閉其他繁重嘅應用程序或使用具有更多內核嘅機器會有幫助。

### 檢測結果唔理想
嘗試調整 UI 入面嘅 **Tolerance (Strictness)** 滑塊：
- **較低 (例如 0.4):** 更嚴格。如果工具將唔同嘅人混入同一個文件夾，請使用呢個設置。
- **較高 (例如 0.6):** 更寬鬆。如果工具為同一個人創建咗太多文件夾，請使用呢個設置。

## 工作原理

1. **掃描**: 掃描你指定嘅輸入文件夾入面嘅所有圖像。
2. **檢測**: 使用 AI 檢測人臉並生成唯一嘅特徵簽名。
3. **分組**: 根據你鍾意嘅嚴格程度對相似嘅人臉進行聚類。
4. **整理**: 喺輸出目錄入面創建文件夾並將圖像複製入去。
5. **UI**: 顯示檢測到嘅唯一身份嘅實時畫廊。

*注意：如果一張圖像入面有幾個人，佢會被複製到每個檢測到嘅人嘅文件夾入面。*
