---
title:  "[2026-04-27 / Top 9] SWE-bench Verified는 더 이상 최첨단 코딩 능력을 측정하지 않는다"
subtitle: "훈련 데이터 오염과 결함 있는 테스트 케이스로 벤치마크 신뢰성이 붕괴되고 있다"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-27 09:00:00
source_url: "https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"
---

> 원본 기사: [https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)

### 개요

OpenAI가 2026년 2월 SWE-bench Verified가 최첨단 AI 모델의 코딩 능력을 측정하는 데 더 이상 적합하지 않다고 공식 발표하며, 대신 SWE-bench Pro를 권장하겠다고 밝혔습니다. AI 코딩 벤치마크에 대한 신뢰성 위기를 보여주는 중요한 사례입니다.

### 문제의 원인

- **결함 있는 테스트 케이스**: 감사된 문제의 최소 59.4%가 기능적으로 올바른 제출을 거부하는 결함 있는 테스트 케이스를 가지고 있습니다.
- **훈련 데이터 오염**: 테스트된 모든 최첨단 모델이 특정 작업에서 원래의 인간이 작성한 버그 수정과 문제 진술 세부 사항을 재현할 수 있었습니다. 즉, 모델이 훈련 중에 문제에 노출되었을 가능성이 높습니다.
- **오염의 심각성**: Claude Opus 4.5 기준으로 SWE-bench Verified에서 80.9%를 기록하지만, SWE-bench Pro에서는 45.9%에 그칩니다. 약 35%p의 괴리는 오염이 벤치마크 점수를 얼마나 부풀릴 수 있는지를 보여줍니다.

### 새로운 기준: SWE-bench Pro

SWE-bench Pro는 훈련 데이터 오염을 최소화하고, 더 현실적인 소프트웨어 개발 시나리오를 반영하도록 설계되었습니다. OpenAI는 이제 SWE-bench Pro에서의 성능을 보고할 것을 권장합니다.

### 시사점

AI 벤치마크의 신뢰성 문제는 점점 심각해지고 있습니다. 모델이 특정 벤치마크 데이터를 훈련 중에 접하고, 그 벤치마크에서 높은 점수를 얻어도 실제 능력을 반영하지 못하는 "벤치마크 오버피팅" 현상입니다. 진정한 AI 능력 평가를 위해서는 새로운 문제와 지속적인 벤치마크 갱신이 필수적입니다.
