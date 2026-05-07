---
title:  "[2026-05-07 / Top 5] Bun, Zig에서 Rust로 포팅 시작: AI 코드 재작성 시대의 논쟁"
subtitle: "Zig의 노-AI 정책과 Anthropic 인수가 맞물려 JavaScript 런타임 이전 검토"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-07 05:00:00
source_url: "https://www.theregister.com/2026/05/05/bun_rust_port/"
---

> 원본 기사: [https://www.theregister.com/2026/05/05/bun_rust_port/](https://www.theregister.com/2026/05/05/bun_rust_port/)

### 개요

Bun(JavaScript 런타임) 창시자 Jarred Sumner가 GitHub에 Zig→Rust 포팅 가이드를 커밋하면서 Bun의 언어 마이그레이션 가능성이 수면 위로 떠올랐다. Bun은 2025년 12월 Anthropic에 인수됐는데, Zig 프로젝트의 **노-AI(no-AI) 정책**이 Claude Code와의 통합을 방해하고 있다는 분석이 나왔다. HN에서 두 개의 쓰레드가 합쳐져 약 1,000포인트를 기록했다.

### 주요 내용

- **포팅 가이드 공개**: Sumner가 커밋한 `docs/PORTING.md`는 Zig 코드를 Rust로 변환하는 코딩 에이전트용 가이드다. "Phase A는 로직을 담는 것, Phase B는 크레이트별 컴파일 가능하게 만드는 것"이라고 설명했다.
- **Zig의 노-AI 정책 충돌**: Zig는 이슈 트래커, PR, 버그 리포트에 AI 생성 콘텐츠를 금지하고 있다. Anthropic이 Bun을 인수해 Claude Code와 통합하려는 상황에서 이 정책은 걸림돌이 됐다. Bun 팀은 이미 Zig를 포크하여 병렬 LLVM 코드 생성으로 디버그 컴파일 속도를 4배 향상시켰지만, 이 개선 사항은 Zig 본류에 업스트림할 수 없다.
- **Sumner의 입장**: "Rust로 완전히 재작성하겠다는 약속이 아니라, 어떻게 돌아가는지 보고 싶을 뿐"이라고 밝혔다.
- **커뮤니티 반응**: "vibe-porting from Zig to Rust"라는 표현이 유행했다. 성능 벤치마크 논쟁, Zig 커뮤니티의 실망, AI 코드 재작성의 장단점 등 다양한 논의가 이어졌다.

### 시사점

이 사건은 AI 도구가 오픈소스 생태계의 거버넌스 결정에 영향을 미치기 시작한 최초의 사례 중 하나다. Zig의 노-AI 정책이 프로젝트 기여 방식을 보호하려는 의도였지만, 결과적으로 주요 사용자를 Rust로 밀어내는 상황이 됐다. AI와 오픈소스의 공존 방식에 대한 업계 논의가 더욱 필요해 보인다.
