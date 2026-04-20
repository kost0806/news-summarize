---
title:  "[2026-04-20 / Top 4] Show HN: TRELLIS.2 이미지-3D 변환, 맥 실리콘에서 실행 – 엔비디아 GPU 불필요"
subtitle: "마이크로소프트 TRELLIS.2 모델을 애플 실리콘 맥에서 네이티브로 실행하는 오픈소스 포팅"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-20 11:00:00
source_url: "https://github.com/shivampkumar/trellis-mac"
---

> 원본 기사: [https://github.com/shivampkumar/trellis-mac](https://github.com/shivampkumar/trellis-mac)

### 개요

마이크로소프트의 최신 이미지-3D 생성 모델인 TRELLIS.2를 엔비디아 GPU 없이 맥(Apple Silicon)에서 실행할 수 있게 해주는 오픈소스 포팅 프로젝트입니다. 3D 콘텐츠 생성에 관심 있는 맥 사용자들에게 큰 주목을 받았습니다.

### 주요 기능

- 단일 이미지로부터 **40만+ 버텍스(vertex) 메시**와 PBR(물리 기반 렌더링) 텍스처가 입혀진 3D 모델 생성
- 베이스 컬러, 메탈릭, 러프니스 텍스처가 포함된 **GLB 파일** 출력
- 성능: M4 Pro (24GB) 기준 콜드 스타트에서 약 **5분 40초** 소요
- Metal 가속 텍스처 베이킹 (순수 Python 폴백 지원)

### 기술적 구현

원본 TRELLIS.2는 CUDA 전용으로 설계되어 엔비디아 GPU가 없으면 실행이 불가능했습니다. 이 포팅 프로젝트는 CUDA 전용 의존성을 애플 실리콘 대안으로 교체했습니다:

| CUDA 의존성 | 애플 실리콘 대안 |
|---|---|
| Sparse 3D Convolution | PyTorch gather-scatter 연산 |
| CUDA 해시맵 기반 메시 추출 | Python 딕셔너리 기반 |
| Flash Attention | PyTorch SDPA |
| CUDA 텍스처 베이킹 | Metal 기반 또는 KDTree 기반 |

### 시스템 요구사항

- macOS (Apple Silicon M1 이상)
- Python 3.11+
- **24GB+ 통합 메모리** 권장
- 모델 가중치용 약 15GB 디스크 공간

### 현재 한계

- CUDA 대비 속도가 느림 (Sparse Convolution 기준 약 10배 느림)
- 홀(hole) 채우기 기능 미지원
- 메시가 텍스처 베이킹 전 20만 면(face)으로 사전 단순화됨
- 추론(inference) 전용 (훈련 불가)

### 시사점

엔비디아 GPU가 없는 맥 사용자들도 최신 3D 생성 AI 모델을 활용할 수 있게 된 의미 있는 포팅 작업입니다. CUDA 종속성이 Apple Metal로 대체되는 흐름은 AI 모델 접근성을 높이는 중요한 추세이며, 애플 실리콘의 통합 메모리 아키텍처가 AI 추론에서 충분한 경쟁력을 보여주고 있음을 시사합니다.
