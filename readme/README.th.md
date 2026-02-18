# เครื่องมือจัดกลุ่มใบหน้า (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

เครื่องมือนี้จะจดจำใบหน้าในรูปภาพโดยอัตโนมัติและจัดกลุ่มลงในโฟลเดอร์ต่างๆ

## ข้อกำหนด

- **ระบบปฏิบัติการ:** macOS, Linux หรือ Windows
- **เวอร์ชัน Python:** `3.11.9` (ระบุไว้ใน `.python-version`)
- **ไลบรารีหลัก:** `face_recognition`, `opencv-python`, `numpy`, `gradio`

## GUI

![Face Grouper GUI](../GUI.png)

## การติดตั้งและการใช้งาน

### 1. การติดตั้ง
ขั้นแรก ตรวจสอบให้แน่ใจว่าคุณได้ตั้งค่า virtual environment และติดตั้งไลบรารีที่จำเป็นทั้งหมดแล้ว

#### macOS / Linux:
```bash
# สร้างและเปิดใช้งาน virtual environment
python3 -m venv venv
source venv/bin/activate

# ติดตั้งไลบรารีที่จำเป็น
./venv/bin/python3 -m pip install -r requirements.txt
```

#### Windows:
```bash
# สร้างและเปิดใช้งาน virtual environment
python -m venv venv
.\venv\Scripts\activate

# ติดตั้งไลบรารีที่จำเป็น
.\venv\Scripts\python -m pip install -r requirements.txt
```

### 2. การเริ่มใช้งาน
เราขอแนะนำให้ใช้เว็บอินเตอร์เฟซที่ทันสมัยเพื่อประสบการณ์การใช้งานที่ดีที่สุด

#### เปิดใช้งาน Web GUI (แนะนำ):
- **macOS / Linux:** `./venv/bin/python3 app.py`
- **Windows:** `.\venv\Scripts\python app.py`

#### เปิดใช้งานเวอร์ชันบรรทัดคำสั่ง (CLI):
- **macOS / Linux:** `./venv/bin/python3 face_grouper.py`
- **Windows:** `.\venv\Scripts\python face_grouper.py`

## การแก้ไขปัญหา

### `ModuleNotFoundError: No module named 'face_recognition'`
ปัญหานี้มักเกิดขึ้นเมื่อคุณรันสคริปต์นอก virtual environment ตรวจสอบให้แน่ใจว่าได้ใช้พาธของ python ใน virtual environment เเสมอ:
- `macOS/Linux: ./venv/bin/python3 app.py`
- `Windows: .\venv\Scripts\python app.py`

### `zsh: command not found: python`
บน macOS ให้ใช้ `python3` แทน `python`

### การประมวลผลช้ามาก
การจดจำใบหน้าต้องใช้ทรัพยากร CPU สูง การปิดแอปพลิเคชันหนักอื่นๆ หรือการใช้เครื่องที่มีจำนวนคอร์มากขึ้นจะช่วยได้

### ผลการตรวจจับไม่ดี
ลองปรับแถบเลื่อน **Tolerance (Strictness)** ใน UI:
- **ต่ำ (เช่น 0.4):** เข้มงวดขึ้น ใช้เมื่อเครื่องมือรวมคนละคนเข้าในโฟลเดอร์เดียวกัน
- **สูง (เช่น 0.6):** ผ่อนปรนขึ้น ใช้เมื่อเครื่องมือสร้างโฟลเดอร์มากเกินไปสำหรับคนคนเดียวกัน

## วิธีการทำงาน

1. **สแกน**: สแกนรูปภาพทั้งหมดในโฟลเดอร์อินพุตที่คุณระบุ
2. **ตรวจจับ**: ใช้ AI เพื่อตรวจจับใบหน้าและสร้างลายเซ็นที่เป็นเอกลักษณ์
3. **จัดกลุ่ม**: จัดกลุ่มใบหน้าที่คล้ายกันตามระดับความเข้มงวดที่คุณต้องการ
4. **จัดระเบียบ**: สร้างโฟลเดอร์ในไดเรกทอรีเอาต์พุตและคัดลอกรูปภาพลงไป
5. **UI**: แสดงแกลเลอรีแบบเรียลไทม์ของบุคคลที่ไม่ซ้ำกันที่ตรวจพบ

*หมายเหตุ: หากรูปภาพหนึ่งมีหลายคน รูปภาพนั้นจะถูกคัดลอกลงในโฟลเดอร์ของแต่ละคนที่ตรวจพบ*
