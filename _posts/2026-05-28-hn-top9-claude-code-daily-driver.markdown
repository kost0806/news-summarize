---
title:  "[2026-05-28 / Top 9] 일상 개발 도구로서의 Claude Code: Claude.md, Skills, Subagents, Plugins, MCPs"
subtitle: "HN 375점 · 228개 댓글"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-28 12:00:00
source_url: "https://arps18.github.io/posts/claude-code-mastery/"
---

> 원본 기사: [https://arps18.github.io/posts/claude-code-mastery/](https://arps18.github.io/posts/claude-code-mastery/)

> HN 토론: [https://news.ycombinator.com/item?id=48289950](https://news.ycombinator.com/item?id=48289950)

### 개요

저자 Arpan Patel이 Claude Code를 14일간 일상 개발 도구로 사용하면서 터득한 실전 노하우를 공유합니다. `.claude` 디렉토리 구조부터 CLAUDE.md 작성법, Skills, Subagents, Plugins, MCPs까지 Claude Code 생태계 전반을 다루는 심층 가이드입니다.

### 주요 내용

- **CLAUDE.md**: 프로젝트별 컨텍스트와 규칙을 Claude에게 전달하는 핵심 파일 — 같은 지시를 두 번 이상 반복하게 된다면 그것은 CLAUDE.md에 기록할 내용
- **Skills**: 재사용 가능한 전문 지식의 단위 — 특정 작업 패턴을 슬래시 커맨드로 등록해 반복 사용
- **Subagents**: 별도의 컨텍스트 창에서 독립적으로 동작하는 보조 에이전트 — 대규모 파일 탐색 등 무거운 작업을 메인 세션에 영향 없이 처리
- **Plugins**: Skills, Hooks, Subagents, MCP 서버를 하나의 설치 가능한 단위로 번들링
- **MCPs(Model Context Protocol)**: 외부 도구·API와의 연동을 표준화하는 프로토콜
- **실전 함정**: 리포지토리 컨텍스트 누적으로 인한 빌드 오류, 건드리지 않은 파일 자동 수정 등의 문제점도 솔직하게 공유

### HN 커뮤니티 반응

HN 점수 375점, 댓글 228개로 Claude Code 사용자들 사이에서 활발한 토론이 이루어졌습니다. 실제 사용 경험자들의 추가 팁과 개선 제안이 댓글에 다수 달렸습니다.

### 시사점

AI 코딩 도구가 단순 자동완성을 넘어 에이전트 기반 개발 환경으로 진화하고 있음을 보여줍니다. 이를 효과적으로 활용하려면 도구의 작동 원리를 이해하고 프로젝트에 맞게 최적화하는 과정이 필수적입니다.
