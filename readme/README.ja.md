# 顔グループ化ツール (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-TW.md) | [廣東話](README.yue.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

このツールは、画像内の顔を自動的に認識し、フォルダにグループ化します。

## 必要条件

- **オペレーティングシステム:** macOS, Linux, または Windows
- **Python バージョン:** `3.11.9` (`.python-version` に指定)
- **コアライブラリ:** `face_recognition`, `opencv-python`, `numpy`

## セットアップ

1. 依存関係のインストール:
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. 画像を `input_images` という名前のフォルダに配置します。

3. スクリプトの実行:
   ```bash
   python face_grouper.py
   ```

## 仕組み

スクリプトは以下の手順を実行します：
1. `input_images` ディレクトリ内のすべての画像をスキャンします。
2. 顔を検出し、各人物のユニークなシグネチャを生成します。
3. `output_groups` 内に検出された各人物のフォルダを作成します。
4. 対応するフォルダに画像をコピーします。

*注意: 1枚の画像に複数の人物が含まれている場合、その画像は検出された各人物のフォルダにコピーされます。*
