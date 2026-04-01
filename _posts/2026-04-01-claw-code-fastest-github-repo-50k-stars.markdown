---
title:  "Claw Code: 역대 최단 시간 GitHub 5만 스타 달성한 오픈소스 프로젝트"
subtitle: "Claude Code 아키텍처를 Python과 Rust로 재구현한 커뮤니티 프로젝트"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/posts/2026-04-01-claw-code-fastest-github-repo-50k-stars.jpg"
date:   2026-04-01 15:00:00
source_url: "https://github.com/instructkr/claw-code"
---

> 원본 기사: [https://github.com/instructkr/claw-code](https://github.com/instructkr/claw-code)

오픈소스 커뮤니티에서 **Claw Code**가 큰 화제를 모으고 있습니다. 이 프로젝트는 공개 후 단 **2시간 만에 GitHub 스타 5만 개**를 돌파하며, 역대 최단 시간 기록을 세웠습니다. 현재 **6만 1천 개 이상의 스타**와 **6만 2천 개 이상의 포크**를 기록하고 있습니다.

### Claw Code란?

Claw Code는 Anthropic의 Claude Code 에이전트 프레임워크의 아키텍처 패턴을 클린룸 방식으로 재구현한 오픈소스 프로젝트입니다. 유출된 소스 코드를 단순히 보관하는 것이 아니라, **에이전트 시스템의 도구 통합, 워크플로우 관리, 런타임 컨텍스트 처리 방식**을 연구하고 Python으로 처음부터 다시 구축했습니다.

> ⚠️ 이 프로젝트는 Anthropic과 제휴, 보증, 유지보수 관계가 없는 독립적인 커뮤니티 프로젝트입니다.

### 주요 특징

- **클린룸 재구현**: 원본 소스를 보존하지 않고, 아키텍처 패턴만을 참고하여 독립적으로 구현
- **하네스 엔지니어링 연구**: AI 에이전트가 도구를 통합하고 워크플로우를 관리하는 방식에 대한 심층 연구
- **CLI 인터페이스 제공**: 매니페스트 생성, 서브시스템 열거, 명령어/도구 인벤토리 검사, 패리티 감사 등 다양한 기능
- **Rust 전환 진행 중**: Python 기반에서 Rust로의 전환 작업이 `dev/rust` 브랜치에서 활발히 진행 중 (현재 코드베이스의 87.7%가 Rust)

### 기술 스택 및 구조

| 항목 | 내용 |
|------|------|
| 주요 언어 | Rust (87.7%), Python (12.3%) |
| 오케스트레이션 | oh-my-codex (OmX) |
| 커밋 수 | 83개 (main 브랜치) |
| 기여자 | 2명 (Yeachan Heo, Sigrid Jin) |
| 감시자 | 624명 |

프로젝트의 핵심 구성 요소는 다음과 같습니다:

- `port_manifest.py` — 워크스페이스 구조 요약
- `models.py` — 서브시스템 및 상태 데이터클래스 정의
- `commands.py` / `tools.py` — 명령어 및 도구 포트 메타데이터
- `query_engine.py` — 포팅 분석 렌더링 엔진
- `main.py` — CLI 인터페이스

### 프로젝트의 배경

이 프로젝트는 2026년 3월 31일, 창작자 Sigrid Jin이 Claude Code의 소스 코드 노출 사건에 대응하여 시작했습니다. OpenAI Codex 기반 워크플로우 도구인 **oh-my-codex(OmX)**의 `$team` 모드(병렬 코드 리뷰)와 `$ralph` 모드(검증 포함 지속 실행 루프)를 활용하여 전체 오케스트레이션을 수행한 것으로 알려져 있습니다.

월스트리트저널 보도(2026년 3월 21일)에 따르면, Sigrid Jin은 연간 250억 개의 Claude Code 토큰을 소비하며 에이전트 시스템 역량을 적극적으로 탐구해온 것으로 전해집니다.

### 커뮤니티

Claw Code는 instructkr Discord 서버를 중심으로 LLM 및 에이전트 워크플로우에 관심 있는 커뮤니티가 활발히 활동하고 있습니다. GitHub 스폰서십을 통한 지원도 가능합니다.

### 향후 전망

현재 Python 기반의 기능은 안정적으로 작동하고 있으며, Rust 포트가 메인 브랜치에 머지될 예정입니다. 아직 원본 TypeScript 시스템과 완전한 런타임 동등성을 달성하지는 못했지만, 아카이브된 파일 구조, 서브시스템 이름, 인벤토리를 충실히 반영하고 있어 빠른 발전이 기대됩니다.

AI 에이전트 프레임워크에 대한 관심이 높아지는 가운데, Claw Code는 에이전트 하네스 엔지니어링의 이해를 넓히는 중요한 커뮤니티 프로젝트로 자리매김하고 있습니다.
