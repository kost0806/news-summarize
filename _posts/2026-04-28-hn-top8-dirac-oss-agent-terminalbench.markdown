---
title:  "[2026-04-28 / Top 8] Show HN: 내가 만든 오픈소스 에이전트, Gemini-3-flash-preview로 TerminalBench 1위 달성"
subtitle: "토큰 효율성에 집중한 코딩 에이전트 Dirac이 TerminalBench 2.0에서 최고 점수를 기록했습니다"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-28 12:07:00
source_url: "https://github.com/dirac-run/dirac"
---

> 원본 기사: [https://github.com/dirac-run/dirac](https://github.com/dirac-run/dirac)

### 개요

개발자 Max Trivedi가 만든 오픈소스 코딩 에이전트 Dirac이 TerminalBench 2.0 리더보드에서 65.2%의 점수로 1위를 달성했습니다. 이는 Google의 공식 기준선(47.6%)과 당시 최고 성능의 상용 에이전트 Junie CLI(64.3%)를 모두 능가하는 성과입니다.

### Dirac 소개

Dirac은 효율성과 컨텍스트 큐레이션에 집중하는 코딩 에이전트입니다. 주요 특징:

- **비용 절감:** 다른 에이전트 대비 API 비용 50~80% 절감 (2.8배 저렴)
- **Hash Anchored 편집:** 파일 전체를 읽고 쓰는 대신 해시 기반으로 필요한 부분만 수정
- **대규모 병렬 작업:** 여러 작업을 동시에 처리
- **AST 조작:** 추상 구문 트리 기반의 정확한 코드 수정
- **승인 기반 워크플로:** 파일 읽기/쓰기, 터미널 명령 실행, 헤드리스 브라우저 사용 등 모든 동작에 사용자 승인 요청

### 벤치마크 성과

| 에이전트 | TerminalBench 2.0 점수 |
|--------|----------------------|
| Dirac (Gemini-3-flash-preview) | **65.2%** |
| Junie CLI | 64.3% |
| Google 공식 기준선 | 47.6% |

개발자는 어떠한 에이전트/스킬 힌트 파일도 삽입하지 않았고 치팅 메커니즘도 사용하지 않았다고 밝혔습니다.

### 설치

VS Code Marketplace에서 확장 프로그램으로 설치할 수 있으며, GitHub 저장소에서 소스 코드를 직접 확인할 수 있습니다.
