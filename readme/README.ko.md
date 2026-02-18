# 얼굴 그룹화 도구 (Face Grouper)

![Face Grouper Cover](../Cover.png)

이 도구는 이미지 속 얼굴을 자동으로 인식하여 폴더별로 그룹화합니다.

## 요구 사항

- **운영 체제:** macOS, Linux 또는 Windows
- **Python 버전:** `3.11.9` (`.python-version`에 명시됨)
- **핵심 라이브러리:** `face_recognition`, `opencv-python`, `numpy`

## 설정 방법

1. 의존성 설치:
   ```bash
   pip install face_recognition opencv-python numpy
   ```

2. 이미지를 `input_images` 폴더에 넣습니다.

3. 스크립트 실행:
   ```bash
   python face_grouper.py
   ```

## 작동 원리

스크립트는 다음과 같이 작동합니다:
1. `input_images` 디렉토리의 모든 이미지를 스캔합니다.
2. 얼굴을 감지하고 각 개인의 고유한 시그니처를 생성합니다.
3. 감지된 각 인물에 대한 폴더를 `output_groups` 아래에 생성합니다.
4. 해당 이미지를 대응하는 폴더에 복사합니다.

*참고: 한 이미지에 여러 명이 포함된 경우, 감지된 각 인물의 폴더로 이미지가 복사됩니다.*
