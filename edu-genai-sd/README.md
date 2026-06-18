# edu-genai-sd — 생성형 AI(Stable Diffusion) 실습

`edu-genai-sd` 컨테이너용 실습 예제입니다. Hugging Face `diffusers`로 Stable Diffusion을 사용해 텍스트→이미지 생성, 프롬프트·파라미터 실험, 이미지→이미지 변환을 다룹니다.

## 실습 순서

번호 순서대로 진행하는 것을 권장합니다.

| 노트북 | 내용 |
|---|---|
| `01_text_to_image.ipynb` | StableDiffusionPipeline으로 텍스트 프롬프트에서 이미지를 생성합니다. 파이프라인 로드, 생성, 여러 프롬프트 비교. |
| `02_prompt_and_parameters.ipynb` | `guidance_scale`·`num_inference_steps`·네거티브 프롬프트가 결과에 미치는 영향을 같은 seed로 비교 실험합니다. |
| `03_img2img.ipynb` | 입력 이미지와 프롬프트로 새 이미지를 생성하는 img2img를 다루고, `strength`(변형 정도)를 비교합니다. |

## 실행 방법

1. `edu-genai-sd` 템플릿으로 워크로드 배포 (GPU VRAM 16GB 이상 권장. SDXL 등 대형 모델은 24GB 이상).
   실습 github repo를 clone 받아야 하는데, 방법은 두 가지입니다.
- 자동 clone — 환경변수 `GIT_CLONE_REPO`에 저장소 주소를 입력하면 워크로드 배포 시 자동으로 받아집니다.
- 직접 clone — 배포 후 워크로드 컨테이너의 내부 터미널에서 `git clone <repo 주소>`를 실행합니다.
2. JupyterLab에 접속합니다.
3. `edu-genai-sd` 폴더를 열어 `01`부터 순서대로 실행합니다.

## 모델

- Stable Diffusion v1.5 모델은 노트북 실행 시 Hugging Face Hub에서 자동 다운로드되어 `/workspace/.cache/huggingface`에 저장됩니다.
- 이미지 생성은 GPU 메모리를 많이 사용합니다. 메모리가 빠듯하면 `enable_attention_slicing()`을 사용하세요.

## 포함 환경

PyTorch 2.11 (CUDA 13.0) 기반이며, 생성형 AI 실습에 필요한 패키지가 미리 설치되어 있습니다. 어텐션 연산은 PyTorch 내장 SDPA를 사용합니다(별도 xformers 불필요).

| 패키지 | 역할 |
|---|---|
| diffusers | 확산 모델 파이프라인(text-to-image·img2img 등) |
| transformers | 텍스트 인코더(CLIP) 등 모델 구성 요소 |
| accelerate | 모델 로딩·실행 가속 |
| safetensors | 안전한 모델 가중치 포맷 |
| datasets | 데이터셋 로드(파인튜닝 시) |
| opencv-python-headless | 이미지 처리 |
| Pillow | 이미지 입출력 |
| tqdm | 진행 상황 표시 |
