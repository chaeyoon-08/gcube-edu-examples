# edu-llm-train — LLM 파인튜닝·RAG 실습

`edu-llm-train` 컨테이너용 실습 예제입니다. LoRA·QLoRA로 LLM을 효율적으로 파인튜닝하고, FAISS 기반 RAG(검색 증강 생성)를 구현합니다.

## 실습 순서

번호 순서대로 진행하는 것을 권장합니다.

| 노트북 | 내용 |
|---|---|
| `01_lora_finetuning.ipynb` | LoRA로 원본 가중치는 고정하고 작은 추가 행렬만 학습합니다. `peft` + `trl` SFTTrainer로 작은 LLM을 instruction 데이터에 지도 파인튜닝합니다. |
| `02_qlora_4bit.ipynb` | bitsandbytes 4비트 양자화 + LoRA(QLoRA)로 더 적은 메모리에서 LLM을 파인튜닝합니다. 제한된 자원에서 LLM을 다루는 표준 기법. |
| `03_rag_faiss.ipynb` | 문서를 임베딩으로 변환해 FAISS로 색인·검색하고, 검색 결과를 LLM 프롬프트에 넣어 답변을 생성하는 RAG를 구현합니다. |

## 실행 방법

1. `edu-llm-train` 템플릿으로 워크로드 배포 (GPU VRAM 16GB 이상 권장. 7B 이상 모델 QLoRA 시 24GB 이상).
   실습 github repo를 clone 받아야 하는데, 방법은 두 가지입니다.
- 자동 clone — 환경변수 `GIT_CLONE_REPO`에 저장소 주소를 입력하면 워크로드 배포 시 자동으로 받아집니다.
- 직접 clone — 배포 후 워크로드 컨테이너의 내부 터미널에서 `git clone <repo 주소>`를 실행합니다.
2. JupyterLab에 접속합니다.
3. `edu-llm-train` 폴더를 열어 `01`부터 순서대로 실행합니다.

## 모델·데이터

- 모델(TinyLlama 등)과 데이터셋(Alpaca 등)은 노트북 실행 시 Hugging Face Hub에서 자동 다운로드되어 `/workspace/.cache/huggingface`에 저장됩니다.
- 4비트 양자화(bitsandbytes)와 QLoRA는 CUDA GPU가 필요합니다.

## 포함 환경

PyTorch 2.11 (CUDA 13.0) 기반이며, LLM 파인튜닝·RAG에 필요한 패키지가 미리 설치되어 있습니다.

| 패키지 | 역할 |
|---|---|
| transformers | LLM·토크나이저·pipeline |
| datasets | 데이터셋 로드·전처리 |
| peft | LoRA 등 효율적 파인튜닝(PEFT) |
| trl | SFTTrainer 등 LLM 지도 파인튜닝 |
| bitsandbytes | 4비트/8비트 양자화(QLoRA) |
| accelerate | 학습 가속·분산 처리 |
| faiss-cpu | 벡터 색인·유사도 검색(RAG) |
| sentencepiece | 서브워드 토크나이저 |
| einops | 텐서 연산 표기 |
| evaluate, scikit-learn | 평가 지표 |
| tensorboard | 학습 로그 시각화 |
| tqdm | 진행 상황 표시 |
