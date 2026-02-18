# Agrupador de Caras (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

Esta herramienta reconoce automáticamente las caras en las imágenes y las agrupa en carpetas.

## Requisitos

- **Sistema Operativo:** macOS, Linux o Windows
- **Versión de Python:** `3.11.9` (especificada en `.python-version`)
- **Bibliotecas principales:** `face_recognition`, `opencv-python`, `numpy`

## Configuración

1. Instale las dependencias:
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. Coloque sus imágenes en una carpeta llamada `input_images`.

3. Ejecute el script:
   ```bash
   python face_grouper.py
   ```

## Cómo funciona

El script:
1. Escaneará todas las imágenes en el directorio `input_images`.
2. Detectará las caras y generará firmas únicas para cada persona.
3. Creará carpetas para cada persona detectada en `output_groups`.
4. Copiará las imágenes en las carpetas correspondientes.

*Nota: Si una imagen contiene a varias personas, se copiará en la carpeta de cada persona detectada.*
