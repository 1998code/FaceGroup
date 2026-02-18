# फेस ग्रूपर (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |

यह टूल स्वचालित रूप से छवियों में चेहरों को पहचानता है और उन्हें फ़ोल्डरों में समूहित (group) करता है।

## आवश्यकताएं

- **ऑपरेटिंग सिस्टम:** macOS, Linux, या Windows
- **पायथन संस्करण:** `3.11.9` (`.python-version` में निर्दिष्ट)
- **मुख्य लाइब्रेरी:** `face_recognition`, `opencv-python`, `numpy`, `gradio`

## GUI

![Face Grouper GUI](../GUI.png)

## स्थापना और निष्पादन

### 1. स्थापना
सबसे पहले, सुनिश्चित करें कि आपने एक वर्चुअल एनवायरनमेंट सेट किया है और सभी निर्भरताएँ (dependencies) स्थापित की हैं।

#### macOS / Linux:
```bash
# वर्चुअल एनवायरनमेंट बनाएं और सक्रिय करें
python3 -m venv venv
source venv/bin/activate

# आवश्यकताएं स्थापित करें
./venv/bin/python3 -m pip install -r requirements.txt
```

#### Windows:
```bash
# वर्चुअल एनवायरनमेंट बनाएं और सक्रिय करें
python -m venv venv
.\venv\Scripts\activate

# आवश्यकताएं स्थापित करें
.\venv\Scripts\python -m pip install -r requirements.txt
```

### 2. टूल चलाना
बेहतर अनुभव के लिए हम आधुनिक वेब इंटरफेस का उपयोग करने की सलाह देते हैं।

#### वेब GUI लॉन्च करें (अनुशंसित):
- **macOS / Linux:** `./venv/bin/python3 app.py`
- **Windows:** `.\venv\Scripts\python app.py`

#### CLI संस्करण लॉन्च करें:
- **macOS / Linux:** `./venv/bin/python3 face_grouper.py`
- **Windows:** `.\venv\Scripts\python face_grouper.py`

## समस्या निवारण (Troubleshooting)

### `ModuleNotFoundError: No module named 'face_recognition'`
यह आमतौर तब होता है जब आप वर्चुअल एनवायरनमेंट के बाहर स्क्रिप्ट चलाते हैं। हमेशा वर्चुअल एनवायरनमेंट के पायथन पथ का उपयोग करना सुनिश्चित करें:
- `macOS/Linux: ./venv/bin/python3 app.py`
- `Windows: .\venv\Scripts\python app.py`

### `zsh: command not found: python`
macOS पर, `python` के बजाय `python3` का उपयोग करें।

### प्रोसेसिंग बहुत धीमी है
चेहरा पहचानना (Face recognition) प्रोसेसर के लिए काफी भारी काम है। अन्य भारी एप्लिकेशन बंद करने या अधिक कोर वाली मशीन का उपयोग करने से मदद मिलेगी।

### खराब परिणाम (Poor detection results)
UI में **Tolerance (Strictness)** स्लाइडर को समायोजित करने का प्रयास करें:
- **कम (जैसे 0.4):** अधिक सख्त। इसका उपयोग तब करें जब टूल अलग-अलग लोगों को एक ही फ़ोल्डर में मिला रहा हो।
- **अधिक (जैसे 0.6):** अधिक ढीला। इसका उपयोग तब करें जब टूल एक ही व्यक्ति के लिए बहुत अधिक फ़ोल्डर बना रहा हो।

## यह कैसे काम करता है

1. **स्कैन**: आपके द्वारा निर्दिष्ट इनपुट फ़ोल्डर की सभी छवियों को स्कैन करता है।
2. **खोज**: चेहरों का पता लगाने और अद्वितीय हस्ताक्षर उत्पन्न करने के लिए AI का उपयोग करता है।
3. **समूह**: आपकी पसंदीदा सख्ती के आधार पर समान चेहरों को समूहित करता है।
4. **व्यवस्थित**: आउटपुट निर्देशिका में फ़ोल्डर बनाता है और छवियों को उनमें कॉपी करता है।
5. **UI**: पहचाने गए अद्वितीय लोगों की रीयल-टाइम गैलरी प्रदर्शित करता है।

*नोट: यदि एक छवि में कई लोग हैं, तो उसे पहचाने गए प्रत्येक व्यक्ति के फ़ोल्डर में कॉपी किया जाएगा।*
