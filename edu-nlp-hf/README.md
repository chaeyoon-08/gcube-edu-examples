# edu-nlp-hf — 자연어처리(Hugging Face) 실습

`edu-nlp-hf` 컨테이너용 실습 예제입니다. Hugging Face Transformers로 사전학습 모델 활용, 텍스트 분류 파인튜닝, 문장 임베딩 기반 의미 검색까지 NLP의 표준 흐름을 다룹니다.

## 실습 순서

번호 순서대로 진행하는 것을 권장합니다.

| 노트북 | 내용 |
|---|---|
| `01_pipeline_inference.ipynb` | `pipeline`으로 학습 없이 감정분석·개체명인식·질의응답·요약·제로샷 분류를 수행합니다. 사전학습 모델 활용 입문. |
| `02_text_classification_finetune.ipynb` | 사전학습 DistilBERT를 IMDb 데이터로 파인튜닝합니다. 토크나이징 → 모델 준비 → `Trainer` 학습·평가까지 NLP 전이학습의 표준 과정을 다룹니다. |
| `03_embeddings_semantic_search.ipynb` | 문장 임베딩을 추출해 코사인 유사도로 의미를 비교하고, 의미 기반 검색을 구현합니다. RAG·추천의 기반 기술. |

## 실행 방법

1. `edu-nlp-hf` 템플릿으로 워크로드 배포 (GPU VRAM 8GB 이상 권장. BERT-large 등 대형 모델 파인튜닝 시 16GB 이상).
   실습 github repo를 clone 받아야 하는데, 방법은 두 가지입니다.
- 자동 clone — 환경변수 `GIT_CLONE_REPO`에 저장소 주소를 입력하면 워크로드 배포 시 자동으로 받아집니다.
- 직접 clone — 배포 후 워크로드 컨테이너의 내부 터미널에서 `git clone <repo 주소>`를 실행합니다.
2. JupyterLab에 접속합니다.
3. `edu-nlp-hf` 폴더를 열어 `01`부터 순서대로 실행합니다.

## 모델·데이터

- 사전학습 모델(DistilBERT, MiniLM 등)과 데이터셋(IMDb)은 노트북 실행 시 Hugging Face Hub에서 자동 다운로드되어 `/workspace/.cache/huggingface`에 저장됩니다.
- 별도 준비가 필요 없습니다.

## 포함 환경

PyTorch 2.11 (CUDA 13.0) 기반이며, Hugging Face NLP 생태계가 미리 설치되어 있습니다.

| 패키지 | 역할 |
|---|---|
| transformers | 사전학습 모델·토크나이저·pipeline·Trainer |
| datasets | 데이터셋 로드·전처리 |
| tokenizers | 고속 토크나이저 백엔드 |
| sentencepiece | 일부 모델용 서브워드 토크나이저 |
| accelerate | 학습 가속·분산 처리 백엔드 |
| evaluate | 평가 지표(accuracy 등) |
| tensorboard | 학습 로그 시각화 |
| scikit-learn | 보조 평가·전처리 |
| tqdm | 진행 상황 표시 |