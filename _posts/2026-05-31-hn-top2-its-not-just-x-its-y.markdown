---
title:  "[2026-05-31 / Top 2] 그냥 데이터 문제가 아니야, 포스트 트레이닝 문제야"
subtitle: "AI 모델의 편향은 학습 데이터보다 사후 조정(post-training) 과정에서 더 많이 발생한다"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/posts/2026-05-31-hn-top2-its-not-just-x-its-y.jpg"
date:   2026-05-31 12:00:00
source_url: "https://mail.cyberneticforests.com/its-not-just-data-its-post-training/"
---

> 원본 기사: [https://mail.cyberneticforests.com/its-not-just-data-its-post-training/](https://mail.cyberneticforests.com/its-not-just-data-its-post-training/)

> HN 토론: [https://news.ycombinator.com/item?id=48350149](https://news.ycombinator.com/item?id=48350149)

### 개요

AI 연구자이자 미디어 비평가 Eryk Salvaggio가 쓴 이 에세이는 AI 모델의 문제점을 단순히 "학습 데이터의 편향" 때문으로 돌리는 시각에 도전합니다. 그는 "그냥 X가 아니야, Y야(It's Not Just X, It's Y)"라는 구조로, 문제의 근원이 포스트 트레이닝(post-training) 과정—RLHF(인간 피드백 강화학습), 파인튜닝, 정렬(alignment) 과정—에 있다고 주장합니다.

### 주요 내용

#### 포스트 트레이닝의 숨겨진 영향력

많은 사람들이 AI 모델의 특정 행동 패턴을 "학습 데이터에 그런 내용이 있었기 때문"이라고 설명합니다. 하지만 Salvaggio는 이것이 문제를 단순화한다고 지적합니다. 같은 학습 데이터로도 포스트 트레이닝 방식에 따라 완전히 다른 모델이 만들어집니다. 진짜 문제는 훈련 후 조정 단계에서 어떤 인간이 어떤 가치관으로 모델을 빚는가입니다.

#### 인간 피드백의 역할

RLHF(Reinforcement Learning from Human Feedback) 과정에서 수천 명의 인간 평가자들이 모델의 응답을 채점합니다. 이 평가자들의 문화적 배경, 편견, 선호가 모델의 "성격"을 형성합니다. 이것이 단순한 데이터 편향보다 훨씬 더 직접적으로 모델 행동에 영향을 미칩니다.

#### 책임 소재의 문제

저자는 이 구분이 단순한 학술적 논의가 아니라 책임 소재와 직결된다고 강조합니다. 데이터 편향 프레임은 "데이터를 고치면 된다"는 기술적 해결책으로 향하지만, 포스트 트레이닝 프레임은 "누가 AI의 가치관을 결정하는가"라는 정치적·윤리적 질문으로 이어집니다.

### HN 커뮤니티 반응

44점, 17개의 댓글로 AI 정렬 연구자들과 비평가들 사이에서 토론이 벌어졌습니다. AI의 행동을 설명하는 프레임워크에 대한 메타적 토론과, 포스트 트레이닝 과정의 투명성 부족에 대한 우려가 주요 논점이었습니다.

### 시사점

AI 시스템의 문제를 진단하고 해결하려면 학습 데이터뿐 아니라 포스트 트레이닝 과정 전체를 투명하게 검토해야 합니다. 기술 기업들이 AI 정렬 방식을 블랙박스로 유지하는 한, 어떤 가치관이 AI에 내재화되는지 알 수 없습니다.
