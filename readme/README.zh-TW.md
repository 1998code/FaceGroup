# 人臉分組工具 (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |

此工具可以自動識別圖像中的人臉並將其分組到不同的文件夾中。

## 運行要求

- **操作系統:** macOS, Linux, 或 Windows
- **Python 版本:** `3.11.9` (見 `.python-version`)
- **核心庫:** `face_recognition`, `opencv-python`, `numpy`, `gradio`

## GUI

![Face Grouper GUI](../GUI.png)

## 安裝與運行

### 1. 安裝
首先，確保您已設置虛擬環境並安裝了所有依賴項。

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
我們建議使用現代 Web 界面以獲得最佳體驗。

#### 啟動 Web GUI (推薦):
- **macOS / Linux:** `./venv/bin/python3 app.py`
- **Windows:** `.\venv\Scripts\python app.py`

#### 啟動命令行版本:
- **macOS / Linux:** `./venv/bin/python3 face_grouper.py`
- **Windows:** `.\venv\Scripts\python face_grouper.py`

## 故障排除

### `ModuleNotFoundError: No module named 'face_recognition'`
這通常發生在您在虛擬環境之外運行腳本時。請務必使用虛擬環境的 python 路徑：
- `macOS/Linux: ./venv/bin/python3 app.py`
- `Windows: .\venv\Scripts\python app.py`

### `zsh: command not found: python`
在 macOS 上，請使用 `python3` 而不是 `python`。

### 處理速度非常慢
人臉識別是 CPU 密集型的。關閉其他繁重的應用程序或使用具有更多內核的機器會有所幫助。

### 檢測結果不佳
嘗試調整 UI 中的 **Tolerance (Strictness)** 滑塊：
- **較低 (例如 0.4):** 更嚴格。如果工具將不同的人混入一個文件夾，請使用此設置。
- **較高 (例如 0.6):** 更寬鬆。如果工具為同一個人創建了過多的文件夾，請使用此設置。

## 工作原理

1. **掃描**: 掃描您指定的輸入文件夾中的所有圖像。
2. **檢測**: 使用 AI 檢測人臉並生成唯一的特徵簽名。
3. **分組**: 根據您喜歡的嚴格程度對相似的人臉進行聚類。
4. **整理**: 在輸出目錄中創建文件夾並將圖像複製到其中。
5. **UI**: 顯示檢測到的唯一身份的實時畫廊。

*注意：如果一張圖像中包含多個人，它將被複製到每個檢測到的人的文件夾中。*
