---
title:  "[2026-05-13 / Top 9] 위임할 때 LLM이 문서를 오염시킨다"
subtitle: "최신 AI 모델도 장기 작업 시 문서 내용의 25%를 손상시킨다는 연구"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-13 10:40:00
source_url: "https://arxiv.org/abs/2604.15597"
---

> 원본 기사: [https://arxiv.org/abs/2604.15597](https://arxiv.org/abs/2604.15597)

> HN 토론: [https://news.ycombinator.com/item?id=48073246](https://news.ycombinator.com/item?id=48073246)

### LLM에 문서 편집을 맡기면 무슨 일이 생길까

Microsoft Research의 Philippe Laban, Tobias Schnabel, Jennifer Neville이 공동 저술한 논문 "LLMs Corrupt Your Documents When You Delegate"가 Hacker News에서 큰 주목을 받고 있다.

#### 연구 배경: 위임 작업(Delegated Work)

LLM의 발전으로 사용자가 AI에게 문서 편집 작업을 위임하는 새로운 작업 방식이 생겨났다. 이메일 초안 작성, 보고서 수정, 코드 문서화 등이 대표적인 예다. 이 연구는 "AI가 내 지시를 수행하면서 문서에 오류를 도입하는가?"라는 질문에 답한다.

#### DELEGATE-52 벤치마크

연구팀은 코딩, 결정학(crystallography), 음악 표기법 등 **52개 전문 도메인**에 걸쳐 장기 위임 작업을 시뮬레이션하는 벤치마크를 만들었다.

#### 충격적인 결과

**최신 프론티어 모델조차도** 장기 워크플로우 후반부에서는 문서 내용의 평균 **25%를 손상(corrupt)** 시켰다. 테스트된 모델에는 다음이 포함된다:
- Gemini 3.1 Pro
- Claude 4.6 Opus
- GPT 5.4

손상 유형:
- 원본에 없던 내용 추가
- 기존 내용의 무단 수정
- 맥락에 맞지 않는 형식 변경
- 수치나 이름의 조용한 오류(hallucination)

#### 시사점

AI에게 문서 편집을 위임할 때 **"AI가 내 지시를 따르면서 문서를 망가뜨리지 않는다"는 가정은 위험하다**. 특히 법률 문서, 의료 기록, 기술 명세서처럼 정확성이 중요한 분야에서는 AI 위임 작업에 주의가 필요하다.

#### HN 커뮤니티 반응

"프론티어 모델이 25%나 오염시킨다는 게 충격적"이라는 반응이 많았다. "AI 에이전트에게 중요한 문서를 맡기기 전에 반드시 검토해야 한다"는 실용적인 조언도 이어졌다. 일부는 "작업이 길어질수록 오염이 누적되는 건 맥락 창 한계의 문제"라고 분석했다.
