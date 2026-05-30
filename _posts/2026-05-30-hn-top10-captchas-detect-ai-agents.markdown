---
title:  "[2026-05-30 / Top 10] CAPTCHA는 여전히 AI 에이전트를 탐지할 수 있다"
subtitle: "AI가 CAPTCHA를 통과해도 인간과 다른 클릭 패턴으로 탐지 가능 – Roundtable Research 연구 결과"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-30 12:00:00
source_url: "https://research.roundtable.ai/captchas-detect-ai/"
---

> 원본 기사: [https://research.roundtable.ai/captchas-detect-ai/](https://research.roundtable.ai/captchas-detect-ai/)

> HN 토론: [https://news.ycombinator.com/item?id=48324910](https://news.ycombinator.com/item?id=48324910)

### 개요

Roundtable Research의 이 연구는 AI 에이전트가 CAPTCHA를 통과하더라도 인간과 근본적으로 다른 인지 과정을 사용하기 때문에 여전히 탐지될 수 있다는 것을 보여줍니다. AI는 사람과 비슷한 정답률을 낼 수 있지만, 그 **방법(행동 패턴)**이 다릅니다.

### 핵심 발견

#### AI vs 인간의 차이점

통계적으로 유의미한 차이가 발견된 행동 지표들:

| 지표 | AI 에이전트의 특징 |
|------|------|
| 순차적 클릭 패턴 | 비인간적으로 일관된 패턴 |
| 방향 전환 | 인간보다 적은 불규칙 방향 전환 |
| 과잉 선택 | 불필요한 항목을 더 많이 선택하는 경향 |

#### CogCAPTCHA30

연구팀은 기존 CAPTCHA에 인지심리학에서 가져온 29가지 클래식 과제를 결합한 **CogCAPTCHA30** 배터리를 개발했습니다. 이 30가지 과제 묶음은 인간과 AI의 차이를 보다 정확하게 포착합니다.

### 왜 아직도 CAPTCHA가 유효한가?

AI 능력이 향상되면서 많은 사람들이 "CAPTCHA는 이제 끝났다"고 생각합니다. 하지만 이 연구는 다른 관점을 제시합니다:

1. **완전한 통과 vs 탐지 가능한 통과**: AI는 통과하더라도 인간처럼 통과하지는 않음
2. **행동 기반 탐지**: 정답 여부가 아닌 *어떻게* 푸는지로 구분 가능
3. **공격 비용 증가 효과**: CAPTCHA는 자동화 공격의 비용을 높이는 방어선 역할

### hCaptcha의 2026년 현황

hCaptcha에 따르면 CAPTCHA 시스템은 지속적으로 진화하고 있습니다:
- 여러 유형의 챌린지를 동시에 혼용
- 보이는 챌린지와 보이지 않는 챌린지 모두 활용
- AI/ML의 발전에 맞춰 지속적으로 어댑티브 업데이트

### HN 커뮤니티 반응

커뮤니티에서는 AI와 CAPTCHA의 군비경쟁, 행동 기반 봇 탐지의 미래, CogCAPTCHA30의 실용성, 그리고 AI 에이전트를 탐지해야 하는 상황의 윤리적 함의에 대한 토론이 이루어졌습니다.
