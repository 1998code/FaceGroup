# Bộ Nhóm Khuôn Mặt (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |

Công cụ này tự động nhận dạng khuôn mặt trong ảnh và nhóm chúng vào các thư mục.

## Yêu cầu

- **Hệ điều hành:** macOS, Linux hoặc Windows
- **Phiên bản Python:** `3.11.9` (được chỉ định trong `.python-version`)
- **Thư viện chính:** `face_recognition`, `opencv-python`, `numpy`, `gradio`

## GUI

![Face Grouper GUI](../GUI.png)

## Cài đặt & Chạy

### 1. Cài đặt
Trước tiên, hãy đảm bảo bạn đã thiết lập môi trường ảo và cài đặt tất cả các thư viện cần thiết.

#### macOS / Linux:
```bash
# Tạo và kích hoạt môi trường ảo
python3 -m venv venv
source venv/bin/activate

# Cài đặt các thư viện yêu cầu
./venv/bin/python3 -m pip install -r requirements.txt
```

#### Windows:
```bash
# Tạo và kích hoạt môi trường ảo
python -m venv venv
.\venv\Scripts\activate

# Cài đặt các thư viện yêu cầu
.\venv\Scripts\python -m pip install -r requirements.txt
```

### 2. Chạy công cụ
Chúng tôi khuyên bạn nên sử dụng giao diện web hiện đại để có trải nghiệm tốt nhất.

#### Khởi chạy Web GUI (Khuyên dùng):
- **macOS / Linux:** `./venv/bin/python3 app.py`
- **Windows:** `.\venv\Scripts\python app.py`

#### Khởi chạy phiên bản dòng lệnh (CLI):
- **macOS / Linux:** `./venv/bin/python3 face_grouper.py`
- **Windows:** `.\venv\Scripts\python face_grouper.py`

## Xử lý sự cố

### `ModuleNotFoundError: No module named 'face_recognition'`
Điều này thường xảy ra khi bạn chạy script bên ngoài môi trường ảo. Luôn đảm bảo sử dụng đường dẫn đến python của môi trường ảo:
- `macOS/Linux: ./venv/bin/python3 app.py`
- `Windows: .\venv\Scripts\python app.py`

### `zsh: command not found: python`
Trên macOS, sử dụng `python3` thay vì `python`.

### Quá trình xử lý rất chậm
Nhận dạng khuôn mặt tiêu tốn nhiều tài nguyên CPU. Việc đóng các ứng dụng nặng khác hoặc sử dụng máy tính có nhiều nhân xử lý hơn sẽ giúp ích.

### Kết quả nhận dạng kém
Hãy thử điều chỉnh thanh trượt **Tolerance (Strictness)** trong giao diện (UI):
- **Thấp (ví dụ: 0.4):** Chặt chẽ hơn. Sử dụng nếu công cụ đang trộn lẫn những người khác nhau vào cùng một thư mục.
- **Cao (ví dụ: 0.6):** Lỏng lẻo hơn. Sử dụng nếu công cụ đang tạo ra quá nhiều thư mục cho cùng một người.

## Đóng góp

Chúng tôi rất hoan nghênh các đóng góp! Nếu bạn muốn giúp cải thiện công cụ này, vui lòng:
1. Fork kho lưu trữ.
2. Tạo một nhánh mới cho tính năng hoặc bản sửa lỗi của bạn.
3. Gửi pull request với mô tả rõ ràng về các thay đổi của bạn.

## Cách thức hoạt động

1. **Quét**: Quét tất cả hình ảnh trong thư mục đầu vào bạn đã chỉ định.
2. **Phát hiện**: Sử dụng AI để phát hiện khuôn mặt và tạo chữ ký duy nhất.
3. **Nhóm**: Nhóm các khuôn mặt giống nhau dựa trên mức độ chặt chẽ bạn chọn.
4. **Tổ chức**: Tạo thư mục trong thư mục đầu ra và sao chép hình ảnh vào đó.
5. **UI**: Hiển thị thư viện thời gian thực về những người duy nhất được phát hiện.

*Lưu ý: Nếu một hình ảnh có nhiều người, nó sẽ được sao chép vào thư mục của mỗi người được phát hiện.*


## Giấy phép

Dự án này được cấp phép theo Giấy phép MIT - xem tệp [LICENSE](../LICENSE) để biết chi tiết.