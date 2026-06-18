# edu-dl-tensorflow — TensorFlow/Keras 딥러닝 실습

`edu-dl-tensorflow` 컨테이너용 실습 예제입니다. TensorFlow의 고수준 API인 Keras로 이미지 분류, 전이학습, 과적합 대응까지 딥러닝의 표준 워크플로를 다룹니다. 데이터셋은 실행 시 자동으로 다운로드됩니다.

## 실습 순서

번호 순서대로 진행하는 것을 권장합니다.

| 노트북 | 내용 |
|---|---|
| `01_image_classification_keras.ipynb` | Fashion-MNIST를 Keras로 분류합니다. 데이터 로드·시각화, 모델 정의(Sequential), `model.fit`/`evaluate`, 학습 곡선·예측 결과 시각화까지 TensorFlow/Keras의 기본 워크플로를 익힙니다. |
| `02_transfer_learning.ipynb` | ImageNet 사전학습 MobileNetV2를 CIFAR-10에 전이학습합니다. 특징 추출(freeze) 후 미세조정(fine-tuning)하며, Keras 전처리 레이어로 데이터 증강을 적용합니다. |
| `03_overfitting_callbacks.ipynb` | 과적합을 학습/검증 곡선으로 진단하고, 데이터 증강·Dropout·EarlyStopping 콜백으로 완화하는 효과를 비교합니다. |

## 실행 방법

1. `edu-dl-tensorflow` 템플릿으로 워크로드 배포 (GPU VRAM 8GB 이상 권장).
   실습 github repo를 clone 받아야 하는데, 방법은 두 가지입니다.
- 자동 clone — 환경변수 `GIT_CLONE_REPO`에 저장소 주소를 입력하면 워크로드 배포 시 자동으로 받아집니다.
- 직접 clone — 배포 후 워크로드 컨테이너의 내부 터미널에서 `git clone <repo 주소>`를 실행합니다.
2. JupyterLab에 접속합니다.
3. `edu-dl-tensorflow` 폴더를 열어 `01`부터 순서대로 실행합니다.

## 데이터셋

- **Fashion-MNIST** — 10종류 의류(티셔츠, 바지, 신발 등)의 28×28 흑백 이미지 7만 장. 딥러닝 입문 표준 데이터셋.
- **CIFAR-10** — 10개 클래스의 32×32 컬러 이미지 6만 장.
- 모두 `tf.keras.datasets`로 노트북 실행 시 자동 다운로드됩니다. 별도 준비가 필요 없습니다.

## 포함 환경

TensorFlow 2.17 (CUDA 12.8) 기반이며, 딥러닝 실습에 필요한 패키지가 미리 설치되어 있습니다.

| 패키지 | 역할 |
|---|---|
| TensorFlow (Keras 포함) | 딥러닝 프레임워크 및 고수준 API. 모델 정의·학습·평가, 사전학습 모델(applications), 전처리 레이어 |
| scikit-learn | 평가 지표·전처리 등 보조 머신러닝 도구 |
| SciPy | 과학 연산 |
| Pillow | 기본 이미지 입출력 |
| Matplotlib | 시각화 (한글 폰트 NanumGothic 포함 — 그래프 제목·라벨에 한글 사용 가능) |
| tqdm | 진행 상황 표시 |
