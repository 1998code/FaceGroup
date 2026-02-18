# 얼굴 그룹화 도구 (Face Grouper)

![Face Grouper Cover](../Cover.png)

| [English](../README.md) | [廣東話](README.yue.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh.md) | [日本語](README.ja.md) | [한국어](README.ko.md) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| [Français](README.fr.md) | [Español](README.es.md) | [Indonesian](README.id.md) | [हिन्दी](README.hi.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) |

이 도구는 이미지 속 얼굴을 자동으로 인식하여 폴더별로 그룹화합니다.

## 요구 사항

- **운영 체제:** macOS, Linux 또는 Windows
- **Python 버전:** `3.11.9` (`.python-version`에 명시됨)
- **핵심 라이브러리:** `face_recognition`, `opencv-python`, `numpy`, `gradio`

## GUI

![Face Grouper GUI](../GUI.png)

## 설치 및 실행

### 1. 설치
먼저 가상 환경이 설정되어 있고 모든 의존성이 설치되었는지 확인하십시오.

#### macOS / Linux:
```bash
# 가상 환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate

# 의존성 설치
./venv/bin/python3 -m pip install -r requirements.txt
```

#### Windows:
```bash
# 가상 환경 생성 및 활성화
python -m venv venv
.\venv\Scripts\activate

# 의존성 설치
.\venv\Scripts\python -m pip install -r requirements.txt
```

### 2. 도구 실행
최고의 경험을 위해 최신 Web 인터페이스를 사용하는 것을 권장합니다.

#### Web GUI 실행 (권장):
- **macOS / Linux:** `./venv/bin/python3 app.py`
- **Windows:** `.\venv\Scripts\python app.py`

#### 명령줄 버전 실행:
- **macOS / Linux:** `./venv/bin/python3 face_grouper.py`
- **Windows:** `.\venv\Scripts\python face_grouper.py`

## 문제 해결

### `ModuleNotFoundError: No module named 'face_recognition'`
이것은 보통 가상 환경 외부에서 스크립트를 실행했을 때 발생합니다. 반드시 가상 환경의 python 경로를 사용하십시오:
- `macOS/Linux: ./venv/bin/python3 app.py`
- `Windows: .\venv\Scripts\python app.py`

### `zsh: command not found: python`
macOS에서는 `python` 대신 `python3`를 사용하십시오.

### 처리가 매우 느림
얼굴 인식은 CPU 집약적인 작업입니다. 다른 무거운 애플리케이션을 닫거나 코어가 더 많은 컴퓨터를 사용하면 도움이 됩니다.

### 감지 결과가 좋지 않음
UI에서 **Tolerance (Strictness)** 슬라이더를 조정해 보십시오:
- **낮음 (예: 0.4):** 더 엄격해집니다. 도구가 서로 다른 사람을 한 폴더에 섞을 때 사용하십시오.
- **높음 (예: 0.6):** 더 느슨해집니다. 도구가 동일인물에 대해 폴더를 너무 많이 생성할 때 사용하십시오.

## 기여

기여는 언제나 환영합니다! 이 도구를 개선하는 데 도움을 주고 싶으시다면:
1. 저장소를 포크합니다.
2. 기능 추가 또는 버그 수정을 위한 새 브랜치를 생성합니다.
3. 변경 사항에 대한 명확한 설명과 함께 풀 리퀘스트를 제출합니다.

## 작동 원리

1. **스캔**: 지정된 입력 폴더의 모든 이미지를 스캔합니다.
2. **감지**: AI를 사용하여 얼굴을 감지하고 각 개인의 고유한 시그니처를 생성합니다.
3. **그룹화**: 선호하는 엄격도에 따라 유사한 얼굴을 클러스터링합니다.
4. **정리**: 출력 디렉토리에 폴더를 생성하고 이미지를 복사합니다.
5. **UI**: 감지된 개인의 실시간 갤러리를 표시합니다.

*참고: 한 이미지에 여러 명이 포함된 경우, 감지된 각 인물의 폴더로 이미지가 복사됩니다.*


## 라이선스

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](../LICENSE) 파일을 참조하십시오.