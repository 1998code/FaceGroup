# Bộ Nhóm Khuôn Mặt (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

Công cụ này tự động nhận dạng khuôn mặt trong ảnh và nhóm chúng vào các thư mục.

## Yêu cầu

- **Hệ điều hành:** macOS, Linux hoặc Windows
- **Phiên bản Python:** `3.11.9` (được chỉ định trong `.python-version`)
- **Thư viện chính:** `face_recognition`, `opencv-python`, `numpy`

## Thiết lập

1. Cài đặt các thư viện phụ thuộc:
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. Đặt hình ảnh của bạn vào thư mục có tên `input_images`.

3. Chạy script:
   ```bash
   python face_grouper.py
   ```

## Cách thức hoạt động

Script sẽ:
1. Quét tất cả hình ảnh trong thư mục `input_images`.
2. Phát hiện khuôn mặt và tạo chữ ký duy nhất cho mỗi người.
3. Tạo thư mục cho mỗi người được phát hiện trong `output_groups`.
4. Sao chép hình ảnh vào các thư mục tương ứng.

*Lưu ý: Nếu một hình ảnh có nhiều người, nó sẽ được sao chép vào thư mục của mỗi người được phát hiện.*
