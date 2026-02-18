# Agrupador de Caras (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |

Esta herramienta reconoce automáticamente las caras en las imágenes y las agrupa en carpetas.

## Requisitos

- **Sistema Operativo:** macOS, Linux o Windows
- **Versión de Python:** `3.11.9` (especificada en `.python-version`)
- **Bibliotecas principales:** `face_recognition`, `opencv-python`, `numpy`, `gradio`

## GUI

![Face Grouper GUI](../GUI.png)

## Instalación y Ejecución

### 1. Instalación
Primero, asegúrese de haber configurado un entorno virtual e instalado todas las dependencias.

#### macOS / Linux:
```bash
# Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
./venv/bin/python3 -m pip install -r requirements.txt
```

#### Windows:
```bash
# Crear y activar el entorno virtual
python -m venv venv
.\venv\Scripts\activate

# Instalar dependencias
.\venv\Scripts\python -m pip install -r requirements.txt
```

### 2. Ejecutar la Herramienta
Recomendamos usar la interfaz web moderna para obtener la mejor experiencia.

#### Iniciar la GUI Web (Recomendado):
- **macOS / Linux:** `./venv/bin/python3 app.py`
- **Windows:** `.\venv\Scripts\python app.py`

#### Iniciar Versión de Línea de Comandos:
- **macOS / Linux:** `./venv/bin/python3 face_grouper.py`
- **Windows:** `.\venv\Scripts\python face_grouper.py`

## Solución de Problemas

### `ModuleNotFoundError: No module named 'face_recognition'`
Esto suele suceder cuando se ejecuta el script fuera del entorno virtual. Asegúrese siempre de usar la ruta al python del entorno virtual:
- `macOS/Linux: ./venv/bin/python3 app.py`
- `Windows: .\venv\Scripts\python app.py`

### `zsh: command not found: python`
En macOS, use `python3` en lugar de `python`.

### El procesamiento es muy lento
El reconocimiento facial es intensivo para la CPU. Cerrar otras aplicaciones pesadas o usar una máquina con más núcleos ayudará.

### Resultados de detección deficientes
Intente ajustar el control deslizante de **Tolerance (Strictness)** en la interfaz:
- **Más bajo (ej. 0.4):** Más estricto. Use esto si la herramienta está mezclando a diferentes personas en una sola carpeta.
- **Más alto (ej. 0.6):** Más flexible. Use esto si la herramienta está creando demasiadas carpetas para la misma persona.

## Contribución

¡Las contribuciones son bienvenidas! Si desea ayudar a mejorar esta herramienta, por favor:
1. Haga un fork del repositorio.
2. Cree una nueva rama para su función o corrección de errores.
3. Envíe una pull request con una descripción clara de sus cambios.

## Cómo funciona

1. **Escaneo**: Escanea todas las imágenes en el directorio de entrada especificado.
2. **Detección**: Utiliza IA para detectar caras y generar firmas únicas.
3. **Agrupación**: Agrupa caras similares según su nivel de restricción preferido.
4. **Organización**: Crea carpetas en el directorio de salida y copia las imágenes en ellas.
5. **UI**: Muestra una galería en tiempo real de las personas únicas detectadas.

*Nota: Si una imagen contiene a varias personas, se copiará en la carpeta de cada persona detectada.*


## Licencia

Este proyecto está bajo la Licencia MIT - vea el archivo [LICENSE](../LICENSE) para más detalles.