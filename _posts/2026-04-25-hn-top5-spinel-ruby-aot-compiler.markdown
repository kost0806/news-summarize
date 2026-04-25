---
title:  "[2026-04-25 / Top 5] Spinel: Ruby AOT 네이티브 컴파일러"
subtitle: "Ruby 창시자 Matz가 공개한 AOT 컴파일러로 CRuby 대비 평균 11.6배 속도 향상 달성"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-25 12:04:00
source_url: "https://github.com/matz/spinel"
---

> 원본 기사: [https://github.com/matz/spinel](https://github.com/matz/spinel)

### 개요

Ruby 언어 창시자 Yukihiro Matsumoto(Matz)가 Ruby 소스 코드를 런타임 의존성 없이 독립적인 네이티브 실행 파일로 컴파일하는 AOT(Ahead-Of-Time) 컴파일러 **Spinel**을 공개했습니다.

### 성능

28개 벤치마크 기준 CRuby miniruby 대비 기하평균 **약 11.6배 속도 향상**을 달성했습니다.

| 벤치마크 | 속도 향상 |
|---------|---------|
| Conway's Game of Life | 86.7배 |
| 재귀적 피보나치 | 34.2배 |
| 만델브로트 집합 | 58.1배 |

### 기술적 원리

세 단계 파이프라인으로 동작합니다.

1. **파싱**: Ruby 소스를 libprism으로 AST 생성
2. **코드 생성**: `spinel_codegen.rb`가 전체 프로그램 타입 추론 및 최적화된 C 코드 생성
3. **컴파일**: 표준 C 컴파일러로 네이티브 바이너리 생성

컴파일러 백엔드(21,000줄)는 Ruby로 작성되었으며, 자기 자신을 컴파일하는 반복적 부트스트랩 과정을 통해 동작합니다. 흥미롭게도 Claude의 도움을 받아 약 한 달 만에 개발되었습니다.

### 제약 사항

Spinel은 Ruby의 모든 기능을 지원하지 않습니다. `eval`, `send`, `method_missing` 같은 메타프로그래밍 기능은 지원하지 않습니다. 따라서 CRuby의 대체재가 아니라, 메타프로그래밍이 필요 없는 계산 집약적 워크로드(데이터 처리 스크립트, 수치 알고리즘, CLI 도구 등)를 위한 특수 도구입니다.

### Hacker News 반응

Ruby 커뮤니티와 컴파일러 관심자들에게 큰 관심을 받았습니다. Matz가 직접 작성한 컴파일러라는 점, 그리고 Claude의 도움으로 빠르게 개발되었다는 점에서 AI 보조 개발의 실제 사례로도 주목받았습니다.
