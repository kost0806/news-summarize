---
title:  "[2026-05-16 / Top 2] MCP Hello Page – MCP 서버 접속 안내 페이지로 지원 티켓 절감"
subtitle: "브라우저로 MCP 서버 열면 안내 HTML 반환하는 UX 개선법"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-16 12:00:00
source_url: "https://www.hybridlogic.co.uk/blog/2026/05/mcp-hello-page"
---

> 원본 기사: [https://www.hybridlogic.co.uk/blog/2026/05/mcp-hello-page](https://www.hybridlogic.co.uk/blog/2026/05/mcp-hello-page)

> HN 토론: [https://news.ycombinator.com/item?id=48164294](https://news.ycombinator.com/item?id=48164294)

### 개요

Hybrid Logic 팀은 MCP(Model Context Protocol) 서버를 제공하면서 사용자들이 브라우저로 MCP 엔드포인트를 열어 401 오류를 보고 지원 티켓을 제출하는 문제를 경험했습니다. 해결책으로, 브라우저에서 `GET /mcp`를 요청할 때 `Accept` 헤더가 `text/html`을 포함하면 JSON 오류 대신 친절한 HTML 안내 페이지를 반환하도록 구현했습니다. 이 간단한 변경만으로 지원 티켓이 급격히 감소했습니다.

### 주요 내용

#### 문제 상황

MCP 서버를 도입한 후, 고객들이 `mcp.acme.com/mcp` 주소를 브라우저로 직접 열면 `401 Unauthorized`와 함께 날것의 JSON 오류 메시지를 보게 됩니다. 이를 본 사용자들은 서버가 고장났다고 판단하여 CS 팀에 지원 요청을 쏟아냈습니다.

#### 해결책: 스마트한 콘텐츠 협상

해결책은 HTTP 콘텐츠 협상(Content Negotiation)을 활용하는 것이었습니다. 요청의 `Accept` 헤더를 검사하여:
- `text/html`을 포함하고 `application/json` 또는 `text/event-stream`을 포함하지 않으면 → HTML 안내 페이지 반환
- 그 외의 경우 → 기존 MCP 프로토콜 응답

HTML 안내 페이지에는 "이 주소는 MCP 서버입니다. MCP 클라이언트에 추가하여 사용하세요"라는 명확한 설명을 담았습니다.

#### 결과

이 변경 이후 관련 지원 티켓이 급감했고, CS 팀의 부담이 줄었으며, 고객들이 MCP 클라이언트 설정을 더 빠르게 완료하게 되었습니다.

### HN 커뮤니티 반응

이 포스트는 점수 29점, 댓글 10개를 기록했습니다. 커뮤니티에서는 이런 단순하지만 효과적인 UX 개선 사례에 공감하는 반응이 많았을 것으로 보입니다. MCP 자체가 "끔찍한 스펙 시도"라고 표현한 저자의 솔직한 평가도 화제가 되었을 것이며, 비슷한 문제를 겪은 다른 MCP 서버 운영자들의 공감대가 형성되었을 것입니다.

### 시사점

기술적으로 복잡한 문제처럼 보이는 것이 사실은 간단한 UX 개선으로 해결될 수 있음을 보여주는 좋은 사례입니다. API 서버를 운영하는 개발자라면 브라우저로 엔드포인트를 직접 열었을 때 어떤 경험을 제공하는지 점검해볼 필요가 있습니다. 개발자 도구를 제공할 때 비기술적 사용자의 관점도 반드시 고려해야 한다는 교훈을 줍니다.
