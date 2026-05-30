---
title:  "[2026-05-30 / Top 4] 최전선 LLM들, 실제 팩트체크에서 67% 불일치 드러나"
subtitle: "GPT-5.4, Claude, Gemini 등 5개 모델이 1,000개 실제 팩트체크 질문의 3분의 2에서 의견 불일치"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-30 12:00:00
source_url: "https://lenz.io/research/llm-disagreement"
---

> 원본 기사: [https://lenz.io/research/llm-disagreement](https://lenz.io/research/llm-disagreement)

> HN 토론: [https://news.ycombinator.com/item?id=48307887](https://news.ycombinator.com/item?id=48307887)

### 개요

HN 4위(446점, 307개 댓글)를 기록한 이 연구는 최전선 LLM들이 실제 사용자가 제출한 팩트체크 질문에 얼마나 일관되게 답변하는지를 조사했습니다. 결과는 충격적입니다: 5개 모델이 1,000개 질문 중 672개(67%)에서 적어도 1개 모델이 다수의견에서 이탈했습니다.

### 연구 방법론

#### 테스트 대상 모델
- GPT-5.4
- Claude Opus 4.7
- Gemini 3 Pro
- Gemini 3 Pro (Search 포함)
- Sonar Pro

#### 데이터셋의 특징

기존 벤치마크(AVeriTeC, PolitiFact 등)는 학습 데이터에 포함되어 있어 신뢰하기 어렵습니다. 이 연구는 **2026년 2월 15일 이후** 실제 사용자가 Lenz 플랫폼에 팩트체크를 요청한 신선한 데이터 1,000개를 활용했습니다. 각 모델에게 주장의 진위를 True / Mostly True / Misleading / False 중 하나로 판정하도록 요청했습니다.

### 주요 발견

#### 불일치율

| 지표 | 수치 |
|------|------|
| 적어도 1개 모델 이탈 | 67% (672/1,000) |
| 2개 이상 범주 차이의 심각한 불일치 | 34% (343/1,000) |
| Krippendorff's alpha 신뢰도 | 0.639 (신뢰 기준 0.8 미달) |

#### 의미

판정이 True와 False로 정반대로 갈리는 경우도 34%에 달합니다. 이는 단순한 보정 차이가 아닌 실질적 의견 불일치입니다.

### 시사점

- **AI 팩트체킹의 한계**: 어느 한 모델만 사용하면 틀릴 가능성이 높음
- **앙상블 접근 필요**: 여러 모델 합의를 거쳐야 신뢰성 확보 가능
- **신선한 데이터의 중요성**: 학습 데이터 오염 없는 실시간 검증 필요

### HN 커뮤니티 반응

HN 점수 446점, 댓글 307개로 AI 신뢰성 논의에 불을 지폈습니다. 연구팀은 이 1,000개 질문에 인간 라벨을 붙여 각 모델 및 Lenz 자체 시스템을 평가하는 후속 연구를 진행 중입니다.
