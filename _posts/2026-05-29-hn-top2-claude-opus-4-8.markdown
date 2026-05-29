---
title:  "[2026-05-29 / Top 2] Claude Opus 4.8"
subtitle: "더 정직하고 오래 독립적으로 작업하는 차세대 Opus 모델"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-29 12:00:00
source_url: "https://www.anthropic.com/news/claude-opus-4-8"
---

> 원본 기사: [https://www.anthropic.com/news/claude-opus-4-8](https://www.anthropic.com/news/claude-opus-4-8)

> HN 토론: [https://news.ycombinator.com/item?id=48311647](https://news.ycombinator.com/item?id=48311647)

### 개요

Anthropic이 Claude Opus 4.8을 출시했습니다. Opus 4.7 출시 41일 만의 업그레이드로, 코딩·에이전트 작업에서 더 날카로운 판단력, 강화된 정직성, 에포트(Effort) 제어 기능, 다이나믹 워크플로우 지원이 핵심입니다. 가격은 Opus 4.7과 동일하게 유지됩니다.

### 주요 내용

- **에포트 제어(Effort Control)**: claude.ai 및 Cowork에서 응답 품질과 속도를 슬라이더로 조절 가능 — 높일수록 더 깊이 사고, 낮출수록 더 빠른 응답
- **다이나믹 워크플로우**: 단일 세션에서 최대 1,000개의 서브에이전트를 병렬로 실행하는 대규모 오케스트레이션 기능 (리서치 프리뷰)
- **정직성 향상**: 결함이 있는 코드 결과를 무비판적으로 보고하는 비율 0% 달성, Opus 4.7 대비 과신(overconfidence) 10배 감소
- **독립 작업 능력**: 긴 시간 동안 인간의 개입 없이 독립적으로 작업을 수행하는 능력 향상
- **가격**: 입력 토큰 $5/M, 출력 토큰 $25/M (변경 없음); 패스트 모드는 2.5배 속도에 $10/$50/M
- **컨텍스트 창**: 기본 1M 토큰 (Claude API, Amazon Bedrock, Vertex AI 기준)

### HN 커뮤니티 반응

Anthropic이 모델 패밀리에서 세 번째 마이너 버전을 출시한 것이 처음이라는 점이 주목받았습니다. 다이나믹 워크플로우의 1,000 서브에이전트 상한선과 비용 급증 가능성에 대한 토론이 활발했습니다. 에포트 제어 기능이 기존 "확장된 사고(extended thinking)"와 어떻게 다른지에 대한 질문도 많았습니다.

### 시사점

AI 코딩 에이전트가 단순 작업에서 수백 개의 병렬 서브태스크를 조율하는 대규모 워크플로우로 진화하고 있음을 보여줍니다. 에포트 제어 기능은 비용 최적화와 품질 간의 트레이드오프를 사용자가 직접 관리할 수 있게 하는 중요한 변화입니다.
