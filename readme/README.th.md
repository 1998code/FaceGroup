# เครื่องมือจัดกลุ่มใบหน้า (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

เครื่องมือนี้จะจดจำใบหน้าในรูปภาพโดยอัตโนมัติและจัดกลุ่มลงในโฟลเดอร์ต่างๆ

## ข้อกำหนด

- **ระบบปฏิบัติการ:** macOS, Linux หรือ Windows
- **เวอร์ชัน Python:** `3.11.9` (ระบุไว้ใน `.python-version`)
- **ไลบรารีหลัก:** `face_recognition`, `opencv-python`, `numpy`

## การติดตั้ง

1. ติดตั้งไลบรารีที่จำเป็น:
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. วางรูปภาพของคุณในโฟลเดอร์ชื่อ `input_images`

3. รันสคริปต์:
   ```bash
   python face_grouper.py
   ```

## วิธีการทำงาน

สคริปต์จะ:
1. สแกนรูปภาพทั้งหมดในไดเรกทอรี `input_images`
2. ตรวจจับใบหน้าและสร้างลายเซ็นเฉพาะสำหรับแต่ละคน
3. สร้างโฟลเดอร์สำหรับแต่ละคนที่ตรวจพบใน `output_groups`
4. คัดลอกรูปภาพไปยังโฟลเดอร์ที่เกี่ยวข้อง

*หมายเหตุ: หากรูปภาพมีหลายคน รูปภาพนั้นจะถูกคัดลอกไปยังโฟลเดอร์ของทุกคนที่ตรวจพบ*
