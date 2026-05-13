---
title:  "[2026-05-13 / Top 2] AI가 코드를 작성한다면, 왜 파이썬을 사용해야 할까?"
subtitle: "AI 코드 생성 시대, 프로그래밍 언어 선택의 패러다임이 바뀐다"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-13 11:50:00
source_url: "https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055"
---

> 원본 기사: [https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055)

> HN 토론: [https://news.ycombinator.com/item?id=48100433](https://news.ycombinator.com/item?id=48100433)

### AI 시대의 언어 선택

2026년 4월 기준, Claude Opus 4.7, GPT-5.5, Gemini 3.1, DeepSeek V4가 모두 몇 주 안에 SWE-bench Verified에서 80%를 돌파했다. AI가 코드를 생성하는 것이 일상이 된 지금, Noah Mitchem은 "그렇다면 왜 여전히 파이썬을 써야 하는가?"라는 근본적인 질문을 던진다.

#### 핵심 주장: AI가 코드를 쓴다고 언어가 무의미해지지는 않는다

저자는 AI가 코드를 생성하더라도 **개발자가 그 코드를 읽고 이해하고 수정할 수 있어야 한다**는 점을 강조한다. 따라서 언어 선택의 기준이 "AI가 이 언어를 잘 쓰는가?"가 아니라, **"내가 AI가 쓴 코드를 잘 읽을 수 있는가?"** 로 바뀌어야 한다고 주장한다.

#### AI와 언어의 새로운 관계

- **컴파일러 피드백 루프**: Rust 같이 컴파일러 에러가 명확하고 구체적인 언어는 AI가 오류를 빠르게 수정하는 데 유리하다. 파이썬은 런타임 에러가 많아 AI의 수정 반복 주기가 길어질 수 있다.
- **타입 시스템**: 강타입 언어는 AI가 코드를 수정할 때 의도치 않은 변경을 방지하는 역할을 한다.
- **생태계와 라이브러리**: 파이썬이 여전히 ML·데이터 분야에서 강점을 가지므로, 도메인에 따라 언어 선택이 달라진다.

#### HN 커뮤니티 토론

Hacker News에서는 이 주제에 대해 활발한 논쟁이 벌어졌다. AI 코드를 사용하더라도 "자신이 잘 아는 언어를 써야 AI 코드를 검토하고 수정할 수 있다"는 의견이 많았다. 반면, "AI가 충분히 발전하면 개발자가 언어를 알 필요도 없어질 것"이라는 전망도 있었다. AI 시대의 프로그래밍 교육과 언어 선택에 대한 근본적인 재고를 촉구하는 글이다.
