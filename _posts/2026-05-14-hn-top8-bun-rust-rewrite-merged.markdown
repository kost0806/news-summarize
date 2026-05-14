---
title:  "[2026-05-14 / Top 8] Bun의 Rust 재작성 PR이 병합됨"
subtitle: "Zig으로 작성된 JavaScript 런타임 Bun, AI 도움으로 Rust로 전환 완료"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-14 12:07:00
source_url: "https://github.com/oven-sh/bun/pull/30412"
---

> 원본 기사: [https://github.com/oven-sh/bun/pull/30412](https://github.com/oven-sh/bun/pull/30412)

> HN 토론: [https://news.ycombinator.com/item?id=48132488](https://news.ycombinator.com/item?id=48132488)

### Bun의 Zig→Rust 재작성 PR 병합 완료

JavaScript/TypeScript 런타임 **Bun**의 창업자 Jarred Sumner가 Zig으로 작성된 100만 줄이 넘는 코드를 Rust로 재작성하는 거대한 PR(#30412)이 메인 저장소에 병합됐다. v1.3.14가 마지막 Zig 버전이다.

#### 재작성의 규모

- **추가 코드**: 1,009,257줄의 Rust 코드, 6,755개 커밋
- **기간**: 약 9일
- **테스트 통과율**: Linux x64 glibc 기준 기존 테스트 스위트의 **99.8%** 통과
- **바이너리 크기**: 3~8MB 감소
- **메모리 누수 수정**: 여러 메모리 누수 및 불안정한 테스트 케이스 해결

#### AI를 활용한 재작성

이 재작성의 핵심은 **Anthropic의 내부 에이전트 인프라**를 활용한 AI 주도 개발이다. 4단계 프로세스로 진행됐다:

1. 에이전트들이 전체 Zig 코드베이스를 입력받음
2. 병렬로 Rust 코드 생성
3. 컴파일러 오류를 피드백 루프에 넣어 반복 수정
4. 기존 테스트 스위트로 호환성 검증

초기에는 16,000개 이상의 컴파일러 오류가 발생했으나, 9일 후 99.8% 통과율에 도달했다. 현재 13,044개의 `unsafe` 블록이 남아 있으며 이는 향후 과제다.

#### Zig에서 Rust로 전환한 이유

Jarred Sumner는 전환 이유로 세 가지를 꼽았다:

1. **생태계**: Rust의 crates.io에 비해 Zig의 패키지 생태계는 협소함
2. **채용**: Rust 개발자 풀이 훨씬 넓음
3. **보안**: Rust의 메모리 안전성 보장이 장기적으로 유리함

#### 미완성 부분

- macOS arm64, Windows 지원은 아직 '실험적' 상태로 진행 중
- 0.2%의 테스트 실패 케이스 해결 필요

#### HN 커뮤니티 반응

"AI로 100만 줄을 9일 만에 재작성"한다는 사실 자체가 놀라움과 우려를 동시에 불러일으켰다. 13,000개의 `unsafe` 블록에 대한 코드 품질 우려, AI 생성 코드의 유지보수 가능성, 그리고 "Zig의 미래는 어떻게 되는가"에 대한 토론이 활발히 이루어졌다.
