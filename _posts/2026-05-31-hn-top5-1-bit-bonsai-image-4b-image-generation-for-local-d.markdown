---
title:  "[2026-05-31 / Top 5] 1비트 Bonsai Image 4B: 아이폰에서 실행되는 이미지 생성 AI"
subtitle: "PrismML, FP16 대비 1/8.3 크기의 로컬 이미지 생성 모델을 Apache 2.0으로 공개"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-31 12:00:00
source_url: "https://prismml.com/news/bonsai-image-4b"
---

> 원본 기사: [https://prismml.com/news/bonsai-image-4b](https://prismml.com/news/bonsai-image-4b)

> HN 토론: [https://news.ycombinator.com/item?id=48346257](https://news.ycombinator.com/item?id=48346257)

### 개요

PrismML이 2026년 5월 26일 공개한 Bonsai Image 4B는 아이폰과 맥북 등 로컬 기기에서 실행 가능한 이미지 생성 AI 모델입니다. FLUX.2 Klein 4B를 기반으로 1비트(binary) 또는 3값(ternary) 양자화 기법을 적용해 원본 대비 메모리 사용량을 1/8.3로 줄이면서도 88%의 성능을 유지합니다. Apache 2.0 라이선스로 오픈 가중치(open weights)를 제공합니다.

### 주요 내용

#### 두 가지 버전

**1비트 Bonsai Image 4B:**
- 트랜스포머 가중치를 이진(binary) {-1, +1} 형태로 압축
- FP16 그룹별 스케일링 인수 적용
- 1.125 유효 비트/가중치 = 0.93 GB 메모리 (FP16 대비 8.3배 작음)
- 최대 압축을 원할 때 적합

**Ternary(3값) Bonsai Image 4B:**
- {-1, 0, +1} 세 가지 값 사용
- 1-비트보다 약간 더 많은 메모리 사용
- 더 높은 이미지 품질 제공
- 메모리와 품질의 균형이 중요한 경우 적합

#### 하드웨어 호환성

- Apple Silicon (iPhone, iPad, Mac) - 아이폰에서 최초로 실행 가능한 이미지 생성 모델
- CUDA GPU
- 로컬 실행으로 클라우드 API 비용 없음, 완전한 프라이버시 보장

#### Bonsai Studio

함께 출시된 iOS 앱 "Bonsai Studio"를 통해 아이폰에서 직접 Bonsai Image 4B를 체험할 수 있습니다.

### HN 커뮤니티 반응

251점, 90개의 댓글로 온디바이스(on-device) AI에 대한 관심이 집중됐습니다. "이제 이미지 생성도 클라우드 불필요", "1비트 양자화의 품질 손실이 생각보다 작다", "애플 기기 최적화 방식" 등에 대한 기술적 토론이 활발했습니다.

### 시사점

클라우드 기반 AI에서 로컬 AI로의 전환이 이미지 생성 분야에도 본격화되고 있습니다. 1비트 양자화 기술의 발전으로 모바일 기기에서 고품질 이미지 생성이 가능해지면서, 프라이버시 보호와 오프라인 활용이라는 새로운 가능성이 열립니다.
