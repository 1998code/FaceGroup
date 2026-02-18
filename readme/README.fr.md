# Groupeur de Visages (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |

Cet outil reconnaît automatiquement les visages dans les images et les regroupe dans des dossiers.

## Prérequis

- **Système d'exploitation :** macOS, Linux ou Windows
- **Version de Python :** `3.11.9` (spécifiée dans `.python-version`)
- **Bibliothèques principales :** `face_recognition`, `opencv-python`, `numpy`, `gradio`

## GUI

![Face Grouper GUI](../GUI.png)

## Installation et Exécution

### 1. Installation
Tout d'abord, assurez-vous d'avoir configuré un environnement virtuel et installé toutes les dépendances.

#### macOS / Linux :
```bash
# Créer et activer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
./venv/bin/python3 -m pip install -r requirements.txt
```

#### Windows :
```bash
# Créer et activer l'environnement virtuel
python -m venv venv
.\venv\Scripts\activate

# Installer les dépendances
.\venv\Scripts\python -m pip install -r requirements.txt
```

### 2. Exécution de l'outil
Nous recommandons d'utiliser l'interface web moderne pour la meilleure expérience.

#### Lancer l'interface Web GUI (Recommandé) :
- **macOS / Linux :** `./venv/bin/python3 app.py`
- **Windows :** `.\venv\Scripts\python app.py`

#### Lancer la version en ligne de commande :
- **macOS / Linux :** `./venv/bin/python3 face_grouper.py`
- **Windows :** `.\venv\Scripts\python face_grouper.py`

## Dépannage

### `ModuleNotFoundError: No module named 'face_recognition'`
Cela arrive généralement lorsque vous lancez le script en dehors de l'environnement virtuel. Assurez-vous de toujours utiliser le chemin vers le python de l'environnement virtuel :
- `macOS/Linux: ./venv/bin/python3 app.py`
- `Windows: .\venv\Scripts\python app.py`

### `zsh: command not found: python`
Sur macOS, utilisez `python3` au lieu de `python`.

### Le traitement est très lent
La reconnaissance faciale est intensive pour le processeur. Fermer d'autres applications lourdes ou utiliser une machine avec plus de cœurs aidera.

### Mauvais résultats de détection
Essayez d'ajuster le curseur **Tolerance (Strictness)** dans l'interface :
- **Plus bas (ex: 0.4) :** Plus strict. Utilisez ceci si l'outil mélange différentes personnes dans un même dossier.
- **Plus haut (ex: 0.6) :** Plus souple. Utilisez ceci si l'outil crée trop de dossiers pour la même personne.

## Comment ça marche

1. **Scan** : Scanne toutes les images de votre dossier d'entrée spécifié.
2. **Détection** : Utilise l'IA pour détecter les visages et générer des signatures uniques.
3. **Groupe** : Regroupe les visages similaires selon votre niveau de restriction.
4. **Organisation** : Crée des dossiers dans le répertoire de sortie et y copie les images.
5. **UI** : Affiche une galerie en temps réel des personnes uniques détectées.

*Note : Si une image contient plusieurs personnes, elle sera copiée dans le dossier de chaque personne détectée.*
