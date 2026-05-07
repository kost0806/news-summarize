---
title:  "[2026-05-07 / Top 7] OpenAI가 대규모 저지연 음성 AI를 제공하는 방법"
subtitle: "WebRTC 인프라를 전면 재설계한 OpenAI의 실시간 음성 AI 아키텍처 공개"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-07 07:00:00
source_url: "https://openai.com/index/delivering-low-latency-voice-ai-at-scale/"
---

> 원본 기사: [https://openai.com/index/delivering-low-latency-voice-ai-at-scale/](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)
> HN 토론: [https://news.ycombinator.com/item?id=48013919](https://news.ycombinator.com/item?id=48013919)

### 개요

OpenAI 엔지니어링 팀이 Realtime API의 실시간 음성 AI 인프라를 어떻게 설계했는지 공개했다. 기존 WebRTC 아키텍처의 한계를 극복하고 전 세계 저지연 음성 스트리밍을 실현하기 위해 **스플릿 릴레이 + 트랜시버 아키텍처**를 새롭게 개발했다. 대화 중 AI가 여전히 말하는 동안 사용자가 끼어들어 방향을 바꾸는 "turn-taking"도 자연스럽게 처리한다.

### 주요 내용

- **핵심 과제**: 세션별 포트 할당은 OpenAI 인프라에 맞지 않았고, ICE/DTLS의 상태 유지 세션은 안정적인 오너십이 필요했으며, 글로벌 라우팅에서 첫 번째 홉 지연을 낮춰야 했다.
- **해결책: 스플릿 릴레이 + 트랜시버**:
  - 클라이언트에는 표준 WebRTC 동작을 유지하면서, OpenAI 내부에서는 패킷 라우팅 방식을 완전히 변경했다.
  - 릴레이 서비스는 Go로 구현됐으며, 범위를 의도적으로 좁혀 성능을 최대화했다.
- **음성 AI의 핵심 원칙**: 오디오는 연속 스트림으로 도착해야 하며, 사용자가 말하는 중에도 AI는 전사(transcription), 추론, 도구 호출, 음성 생성을 동시에 시작할 수 있어야 한다.
- **WebRTC 선택 이유**: 기존 RTP 기반 미디어 전송의 실전 검증된 신뢰성을 활용하면서, AI 특화 요구사항을 충족시켰다.
- **Realtime API 요금**: Translate·Whisper는 분당 과금, GPT-Realtime-2는 토큰 소비로 과금.

### 시사점

이 아키텍처 공개는 음성 AI를 실제 제품에 통합하려는 개발자들에게 귀중한 엔지니어링 인사이트를 제공한다. OpenAI가 WebRTC를 완전히 새로 구현한 배경에는 단순히 성능 문제뿐만 아니라, AI 특유의 "동시 처리" 요구사항이 있었다. Go를 선택한 이유, 릴레이 서비스의 좁은 범위 유지 철학 등 실제 인프라 설계에 대한 투명한 공유가 HN 기술 커뮤니티에서 높은 평가를 받았다.
