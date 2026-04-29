---
title:  "[2026-04-29 / Top 7] VibeVoice: 마이크로소프트의 오픈소스 최첨단 음성 AI"
subtitle: "60분 장문 오디오를 단일 패스로 처리하는 TTS/ASR 통합 음성 AI 모델"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-29 12:06:00
source_url: "https://github.com/microsoft/VibeVoice"
---

> 원본 기사: [https://github.com/microsoft/VibeVoice](https://github.com/microsoft/VibeVoice)

### 요약

**Microsoft**가 오픈소스 음성 AI 모델 시리즈 **VibeVoice**를 공개했습니다. TTS(텍스트→음성)와 ASR(음성→텍스트) 모델을 모두 포함하며, 특히 **60분 장문 오디오를 단일 패스로 처리**하는 ASR 기능이 주목을 받고 있습니다.

---

### 주요 모델

#### VibeVoice-ASR (음성 인식)
- **60분 장문 오디오** 단일 패스 처리
- 구조화된 전사 결과 생성: **누가(화자), 언제(타임스탬프), 무엇을(내용)** 포함
- **사용자 맞춤 컨텍스트** 지원
- **50개 이상 언어** 지원 (네이티브 다국어)
- 2026년 1월 21일 오픈소스 공개

#### VibeVoice-Realtime-0.5B (실시간 TTS)
- **스트리밍 텍스트 입력** 지원
- 견고한 장문 음성 생성
- 실시간 처리에 최적화된 경량 모델

---

### 핵심 기술

VibeVoice의 핵심 혁신은 **연속 음성 토크나이저(Continuous Speech Tokenizer)** 입니다:

- **초저프레임율 7.5Hz**로 동작하는 음향(Acoustic) 및 의미(Semantic) 토크나이저
- 오디오 품질을 유지하면서 긴 시퀀스 처리의 연산 효율을 크게 향상
- 기존 모델 대비 긴 오디오 처리 성능 개선

---

### 커뮤니티 활용

- **Vibing**: VibeVoice-ASR 기반의 음성 입력 방식 앱 (2026년 3월 29일 공개)
- 커뮤니티 포크 `vibevoice-community/VibeVoice`도 활발히 개발 중
- 모델 가중치는 **Hugging Face**에서 공개 제공 (`microsoft/VibeVoice-1.5B`)

---

### 접근 방법

- **GitHub**: [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice)
- **공식 문서**: [microsoft.github.io/VibeVoice](https://microsoft.github.io/VibeVoice/)
- **모델 다운로드**: Hugging Face에서 제공
