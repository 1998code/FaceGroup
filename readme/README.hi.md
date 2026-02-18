# फेस ग्रूपर (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

यह टूल स्वचालित रूप से छवियों में चेहरों को पहचानता है और उन्हें फ़ोल्डरों में समूहित (group) करता है।

## आवश्यकताएं

- **ऑपरेटिंग सिस्टम:** macOS, Linux, या Windows
- **पायथन संस्करण:** `3.11.9` (`.python-version` में निर्दिष्ट)
- **मुख्य लाइब्रेरी:** `face_recognition`, `opencv-python`, `numpy`

## सेटअप

1. निर्भरताएँ (Dependencies) स्थापित करें:
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. अपनी छवियों को `input_images` नामक फ़ोल्डर में रखें।

3. स्क्रिप्ट चलाएँ:
   ```bash
   python face_grouper.py
   ```

## यह कैसे काम करता है

स्क्रिप्ट निम्न कार्य करेगी:
1. `input_images` निर्देशिका की सभी छवियों को स्कैन करेगी।
2. चेहरों का पता लगाएगी और प्रत्येक व्यक्ति के लिए अद्वितीय हस्ताक्षर (signatures) उत्पन्न करेगी।
3. `output_groups` में प्रत्येक पहचाने गए व्यक्ति के लिए फ़ोल्डर बनाएगी।
4. छवियों को संबंधित फ़ोल्डरों में कॉपी करेगी।

*नोट: यदि एक छवि में कई लोग हैं, तो उसे पहचाने गए प्रत्येक व्यक्ति के फ़ोल्डर में कॉपी किया जाएगा।*
