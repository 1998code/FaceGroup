# Groupeur de Visages (Face Grouper)

![Face Grouper Cover](../Cover.png)

Cet outil reconnaît automatiquement les visages dans les images et les regroupe dans des dossiers.

## Prérequis

- **Système d'exploitation :** macOS, Linux ou Windows
- **Version de Python :** `3.11.9` (spécifiée dans `.python-version`)
- **Bibliothèques principales :** `face_recognition`, `opencv-python`, `numpy`

## Configuration

1. Installez les dépendances :
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. Placez vos images dans un dossier nommé `input_images`.

3. Lancez le script :
   ```bash
   python face_grouper.py
   ```

## Comment ça marche

Le script va :
1. Scanner toutes les images du répertoire `input_images`.
2. Détecter les visages et générer des signatures uniques pour chaque personne.
3. Créer des dossiers pour chaque personne détectée dans `output_groups`.
4. Copier les images dans les dossiers correspondants.

*Note : Si une image contient plusieurs personnes, elle sera copiée dans le dossier de chaque personne détectée.*
