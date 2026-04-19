---
title:  "Hacker News 오늘의 Top 10 (2026-04-19)"
subtitle: "Claude Design 출시, Michael Rabin 별세, Kelp DAO $292M 해킹, Amiga 그래픽 아카이브 등"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/posts/2026-04-19-hn-top10.jpg"
date:   2026-04-19 12:00:00
source_url: "https://news.ycombinator.com"
---

> 원본: [Hacker News](https://news.ycombinator.com)

2026년 4월 19일 Hacker News 상위 10개 스토리를 요약합니다.

---

#### 1. Anthropic, Claude Design 출시 — AI로 시각 디자인을 즉시 생성

> 원본 기사: [https://www.anthropic.com/news/claude-design-anthropic-labs](https://www.anthropic.com/news/claude-design-anthropic-labs)

Anthropic이 4월 17일 **Claude Design**을 Anthropic Labs 제품으로 공개했습니다. Claude Opus 4.7을 기반으로 하는 이 도구는 자연어 프롬프트만으로 **프레젠테이션·슬라이드·원페이저·인터랙티브 프로토타입** 등 폭넓은 시각 자료를 생성합니다. 대화형 디자인 프로세스가 핵심으로, 사용자가 원하는 것을 설명하면 Claude가 초안을 만들고 인라인 코멘트·직접 편집·커스텀 슬라이더로 반복 수정할 수 있습니다. 팀 온보딩 시 코드베이스와 디자인 파일을 분석해 **자동 디자인 시스템**(색상·타이포그래피·컴포넌트)을 구축하며, 이후 모든 작업에 적용됩니다. 완성물은 조직 내부 URL 공유, Canva·PDF·PPTX·HTML 내보내기, Claude Code 핸드오프 번들 생성까지 지원합니다. Claude Pro/Max/Team/Enterprise 구독자를 대상으로 연구 프리뷰 중이며, Figma의 강력한 경쟁자로 HN에서 뜨거운 토론을 이어가고 있습니다.

---

#### 2. Michael Rabin 별세 (1931–2026) — 컴퓨터과학의 거인

> 원본 기사: [https://www.ynetnews.com/health_science/article/byohxvw611l](https://www.ynetnews.com/health_science/article/byohxvw611l)

컴퓨터과학의 거장 **Michael Oser Rabin**이 4월 14일 94세를 일기로 별세했습니다. Dana Scott과 함께 **1976년 ACM 튜링상**을 수상한 그는 비결정적 유한 오토마타(NFA) 이론을 확립하고, 랜덤화 알고리즘의 개념을 컴퓨팅에 도입한 선구자입니다. **Miller–Rabin 소수 판별법**, **Rabin–Karp 문자열 검색 알고리즘**, **Rabin 지문(fingerprinting)** 등 현대 암호학·알고리즘 분야 전반에 그의 업적이 살아 있습니다. 히브리 대학교에서 이스라엘 컴퓨터과학의 기반을 쌓았으며, 딸 Tal Rabin 역시 著名한 암호학자입니다. HN에서 추모 댓글이 쏟아지며 "자연이 우리의 무작위성의 원천"이라는 그의 유명 어록이 다시 회자됐습니다.

---

#### 3. Kelp DAO, LayerZero 브릿지 해킹으로 $292M 탈취 — 2026년 최대 DeFi 익스플로잇

> 원본 기사: [https://www.coindesk.com/tech/2026/04/19/2026-s-biggest-crypto-exploit-kelp-dao-hit-for-usd292-million-with-wrapped-ether-stranded-across-20-chains](https://www.coindesk.com/tech/2026/04/19/2026-s-biggest-crypto-exploit-kelp-dao-hit-for-usd292-million-with-wrapped-ether-stranded-across-20-chains)

4월 19일 17:35 UTC, 공격자가 Kelp DAO의 LayerZero 기반 크로스체인 브릿지를 해킹해 **116,500 rsETH($292M)**를 탈취했습니다. 이는 2026년 DeFi 최대 규모 익스플로잇으로 이전 기록(Drift Protocol $285M)을 갱신했습니다. 공격 방식은 **LayerZero EndpointV2의 단일 DVN(1/1) 검증 구성**의 취약점을 이용, 타 체인에서 정당한 전송 명령이 도착한 것처럼 위장해 rsETH를 탈취한 뒤 즉시 Aave·Compound V3·Euler에 담보로 맡겨 clean WETH $236M을 대출 받는 방식입니다. 공격자는 Tornado Cash로 자금 출처를 숨겼으며, 10시간 후 공격을 실행했습니다. Kelp은 46분 후 컨트랙트를 긴급 정지했고 후속 2건의 추가 탈취 시도는 차단됐습니다. Aave TVL은 $6.6B 급감했고 토큰 가격은 16% 하락했습니다. rsETH는 20개 이상의 체인에 분산된 채 묶여 있습니다.

---

#### 4. Category Theory Illustrated – Orders

> 원본 기사: [https://abuseofnotation.github.io/category-theory-illustrated/04_order/](https://abuseofnotation.github.io/category-theory-illustrated/04_order/)

범주 이론(Category Theory)을 시각적으로 설명하는 온라인 교재 **"Category Theory Illustrated"** 의 Orders 챕터가 HN 상위권에 올랐습니다. 이 챕터는 **편순서 집합(poset, partially ordered set)**을 중심으로 반사성·전이성·반대칭성 세 가지 법칙을 따르는 이진 관계를 소개합니다. 시각적 직관을 위해 **하세 다이어그램(Hasse diagram)**을 활용하며, 더 "큰" 원소를 항상 위에 배치하는 규칙으로 두 점의 비교를 직관적으로 표현합니다. 핵심 개념으로는 **join(∨)**과 **meet(∧)** 연산이 있으며, 이는 범주론의 쌍대곱(coproduct)·곱(product)과 정확히 대응됩니다. "수학의 수학"이라 불리는 범주론을 코드 작성과 연결하는 방식이 호평받으며, 댓글에서는 프로그래밍 언어 설계에서의 응용 사례 논의가 활발했습니다.

---

#### 5. Amiga Graphics Archive — 80~90년대 픽셀 아트의 보고

> 원본 기사: [https://amiga.lychesis.net/](https://amiga.lychesis.net/)

Commodore Amiga용으로 제작된 그래픽들을 체계적으로 보존하는 **Amiga Graphics Archive**가 HN 상위에 등장했습니다. 이 사이트는 Deluxe Paint 등 당시 툴로 만들어진 픽셀 아트·데모씬 그래픽을 수집·보존하며, 2026년 1월 업데이트를 통해 CU Amiga 매거진의 "Art Gallery" 섹션 이미지를 대규모로 추가했습니다. Amiga는 1985~1995년 당시 독보적인 그래픽 능력(copper list, planar 그래픽 모드, 512색 동시 표시)으로 게임·데모씬·그래픽 디자인의 중심이었습니다. HN 댓글에서는 Amiga가 16비트인지 32비트인지에 대한 고전적 논쟁과 함께, 현대 GPU와 비교되는 당시의 하드웨어 철학 토론이 이어졌습니다.

---

#### 6. Ada, 그 설계, 그리고 언어를 만든 언어

> 원본 기사: [https://www.iqiipi.com/the-quiet-colossus.html](https://www.iqiipi.com/the-quiet-colossus.html)

"The Quiet Colossus"라는 제목의 이 글은 **Ada 프로그래밍 언어**의 설계 철학과 역사를 심층 분석합니다. 1977~1983년 미국 국방부 계약으로 Jean Ichbiah이 이끈 팀이 설계한 Ada는 강타입 시스템, 명시적 인터페이스 분리(specification vs body), 동시성 내장(tasking), 계약 기반 설계(contract by design)를 특징으로 합니다. 글은 특히 Ada의 **패키지 아키텍처**—사양(contract)과 본체(implementation)를 물리적으로 분리하는 컴파일 단위—가 C++ 모듈, Rust 트레이트, Swift 프로토콜로 이어지는 현대 언어 설계의 원형임을 주장합니다. 2026년 TIOBE Top 10 진입을 계기로 Ada 르네상스 논의가 활발한 가운데, HN 댓글에서는 Intel i432 칩의 Ada 기반 하드웨어 설계, 안전 핵심 시스템(항공·방산)에서의 실제 사용 사례가 공유됐습니다.

---

#### 7. Show HN: 불연속 구간 집합으로 동작하는 계산기

> 원본 기사: [https://news.ycombinator.com/item?id=47812341](https://news.ycombinator.com/item?id=47812341)

개발자 Victor Poughon이 **불연속 구간의 집합(disjoint sets of intervals)**에 대한 사칙연산·교집합·합집합을 지원하는 온라인 계산기를 공개했습니다. 기존 구간 연산 라이브러리들이 수동 disjoint 관리를 요구하는 문제를 해결하며, `[1,2] ∪ [4,5]` 같은 복합 구간 표현을 직접 다룰 수 있습니다. 신경망 오차 한계 분석, 결정 트리 경계 계산, 일정 충돌 감지 등 AI·엔지니어링 영역에서 구간 연산이 자주 필요하다는 맥락에서 소개됐습니다. 약 300 포인트, 50여 개의 댓글을 획득했으며, 구간 나무 자료구조(Interval Tree)와 성능 비교 토론이 활발하게 이루어졌습니다.

---

#### 8. A Python Interpreter Written in Python

> 원본 기사: [https://news.ycombinator.com/item?id=47755261](https://news.ycombinator.com/item?id=47755261)

"500 Lines or Less" 오픈소스 프로젝트의 일환으로 작성된 **Python으로 구현된 Python 인터프리터** 글이 다시 HN 상위에 올랐습니다. 자기 호스팅(self-hosting) 인터프리터 구현을 단계별로 설명하며, 바이트코드 컴파일, 프레임 스택, CPython 내장 객체 구조를 Python으로 재현하는 과정을 다룹니다. "인터프리터를 실행하려면 결국 어딘가에 바이너리가 있어야 한다"는 부트스트래핑 역설과 함께, 각 계층을 거칠수록 누적되는 성능 저하 문제가 댓글 토론의 핵심이었습니다. 교육적 가치가 높아 컴파일러·인터프리터 개념을 처음 배우는 개발자들에게 추천 글로 꼽혔습니다.

---

#### 9. Bluesky April 2026 서비스 장애 사후 분석 (Post-Mortem)

> 원본 기사: [https://pckt.blog/b/jcalabro/april-2026-outage-post-mortem-219ebg2](https://pckt.blog/b/jcalabro/april-2026-outage-post-mortem-219ebg2)

Bluesky 엔지니어 Jim Calabro가 4월 4~7일 발생한 약 8시간의 부분 서비스 장애에 대한 상세 사후 분석을 공개했습니다. **근본 원인**은 두 가지가 맞물린 것이었습니다. (1) 새로 배포된 내부 서비스가 GetPostRecord RPC를 호출할 때 한 배치에 15,000~20,000개의 URI를 전송하는 구조였는데, 이 엔드포인트에만 **바운디드 동시성(bounded concurrency)** 처리가 빠져 있어 요청마다 수만 개의 goroutine이 생성됐습니다. (2) 이로 인해 TCP 연결이 TIME_WAIT 상태로 쌓이며 **이페머럴 포트 고갈**이 발생, memcache 오류가 폭증했습니다. 초당 수백만 건 요청에서 발생하는 memcache 오류를 Go의 블로킹 write syscall로 로깅하자 Go 런타임이 OS 스레드를 정상 대비 10배로 증설했고, 가비지 컬렉터 압박으로 요청이 지연되는 악순환이 이어졌습니다. HN에서는 분산 시스템 장애 패턴의 교과서적 사례로 극찬받았습니다.

---

#### 10. Ask HN: Codex가 정말로 Claude Code와 대등한가?

> 원본 기사: [https://news.ycombinator.com/item?id=47750069](https://news.ycombinator.com/item?id=47750069)

OpenAI Codex 대규모 업데이트 이후 "Codex가 실제로 Claude Code와 비교되는가?"를 묻는 Ask HN 스레드가 큰 반응을 얻었습니다. 상위 답변들은 두 도구의 차별점을 다음과 같이 분석했습니다: **Claude Code**는 긴 컨텍스트 유지, 복잡한 리팩토링, CLAUDE.md 기반 프로젝트 기억이 강점인 반면, **Codex**는 새로 추가된 컴퓨터 사용(Computer Use) 기능과 90+ 플러그인 생태계, 스케줄링·메모리 기능이 강점으로 꼽혔습니다. "도구가 아니라 워크플로우의 문제"라는 시각도 많았으며, 두 도구를 병행 사용하는 팀의 경험담이 활발하게 공유됐습니다. AI 코딩 도구 시장의 경쟁이 격화되는 가운데, 사용자 경험 기반의 실질적 비교가 이루어진 스레드로 주목받았습니다.
