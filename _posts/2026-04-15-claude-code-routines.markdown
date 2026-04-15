---
title:  "Claude Code Routines: 자동화 작업 실행 가이드"
subtitle: "스케줄·API·GitHub 이벤트로 Claude Code를 자동 실행하는 Routines 기능 총정리"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-15 12:00:00
source_url: "https://code.claude.com/docs/en/routines"
---

> 원본 기사: [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)

### 개요

Anthropic이 **Claude Code Routines** 기능을 공개했습니다(현재 리서치 프리뷰). Routines는 Claude Code 설정(프롬프트, 저장소, 커넥터)을 한 번 저장해두면 자동으로 반복 실행할 수 있는 기능입니다. Anthropic 클라우드 인프라에서 실행되므로 노트북이 꺼져 있어도 동작합니다.

### 트리거 종류

루틴은 세 가지 트리거를 하나의 루틴에 조합해서 사용할 수 있습니다.

| 트리거 | 설명 |
|--------|------|
| **Schedule** | 시간별·일별·주중·주간 등 반복 주기로 실행 |
| **API** | HTTP POST 요청으로 온디맨드 실행 (bearer 토큰 인증) |
| **GitHub** | PR·Push·이슈·워크플로우 등 저장소 이벤트 발생 시 자동 실행 |

Pro, Max, Team, Enterprise 플랜에서 Claude Code on the web이 활성화된 경우 사용 가능합니다.

### 주요 활용 사례

- **백로그 관리**: 매일 밤 이슈 트래커를 읽어 라벨 지정·담당자 할당·Slack 요약 게시
- **알림 트리지**: 모니터링 도구가 API 엔드포인트를 호출하면 스택 트레이스 분석 후 수정 PR 자동 생성
- **코드 리뷰**: PR이 열릴 때마다 팀 체크리스트 적용, 보안·성능·스타일 인라인 코멘트 작성
- **배포 검증**: 배포 후 CD 파이프라인이 API를 호출하면 스모크 테스트 실행 및 결과를 릴리즈 채널에 게시
- **문서 동기화**: 주간 스캔으로 변경된 API를 참조하는 문서를 찾아 업데이트 PR 생성
- **라이브러리 포팅**: 한 SDK의 PR이 머지되면 다른 언어의 동일 SDK에 자동으로 변경 사항 포팅

### 루틴 생성 방법

세 가지 방법으로 만들 수 있으며, 모두 동일한 클라우드 계정에 저장됩니다.

#### 웹 (claude.ai/code/routines)
1. **New routine** 클릭
2. 이름과 프롬프트 작성 (모델 선택 포함)
3. GitHub 저장소 추가 (기본 브랜치에서 클론, `claude/` 접두사 브랜치에 push)
4. 클라우드 환경 선택 (네트워크 접근·환경변수·설치 스크립트 설정)
5. 트리거 설정 (Schedule / GitHub event / API)
6. 커넥터 확인 후 **Create**

#### CLI
```
/schedule daily PR review at 9am
/schedule list          # 전체 목록
/schedule update        # 수정
/schedule run           # 즉시 실행
```
CLI에서는 Schedule 트리거만 생성 가능. API·GitHub 트리거는 웹에서 추가해야 합니다.

#### 데스크탑 앱
**Schedule** 페이지 → **New task** → **New remote task** 선택.
(New local task는 내 컴퓨터에서만 실행되는 로컬 예약 작업)

### API 트리거 사용법

루틴을 저장하면 고유한 HTTP 엔드포인트가 생성됩니다. 아래와 같이 POST 요청을 보내면 새 세션이 시작됩니다.

```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/trig_01ABCDEFGHJKLMNOPQRSTUVW/fire \
  -H "Authorization: Bearer sk-ant-oat01-xxxxx" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod. Stack trace attached."}'
```

요청 성공 시 응답:

```json
{
  "type": "routine_fire",
  "claude_code_session_id": "session_01HJKLMNOPQRSTUVWXYZ",
  "claude_code_session_url": "https://claude.ai/code/session_01HJKLMNOPQRSTUVWXYZ"
}
```

`text` 필드에 알림 내용이나 로그 같은 런타임 컨텍스트를 자유 형식으로 전달할 수 있습니다.

> **주의**: `/fire` 엔드포인트는 `experimental-cc-routine-2026-04-01` 베타 헤더 하에 제공됩니다. 리서치 프리뷰 기간 중 스펙이 변경될 수 있습니다.

### GitHub 트리거 지원 이벤트

| 이벤트 | 트리거 조건 |
|--------|------------|
| Pull request | PR 열림·닫힘·라벨·동기화 등 |
| Push | 브랜치에 커밋 push |
| Issues | 이슈 열림·수정·닫힘 등 |
| Issue comment | 이슈·PR 코멘트 생성·수정·삭제 |
| Workflow run | GitHub Actions 워크플로우 시작·완료 |
| Release | 릴리즈 생성·게시·수정·삭제 |
| Discussion | 디스커션 생성·수정·답변 등 |
| Check run / suite | 체크 요청·완료 |
| (그 외 8가지) | Merge queue, Repository dispatch 등 |

PR 트리거는 작성자, 제목, 본문, base/head 브랜치, 라벨, 초안 여부, 포크 여부 등 다양한 필터를 지원합니다.

### 루틴 실행 특성

- 루틴은 **완전 자율 실행**: 승인 프롬프트 없이 셸 명령 실행, 스킬·커넥터 사용 가능
- 기본적으로 `claude/` 접두사 브랜치에만 push 가능 (보호 브랜치 보호)
- GitHub 이벤트 하나마다 독립된 새 세션이 생성됨
- 루틴은 개인 계정에 귀속되며, 커밋·PR·Slack 메시지 등은 내 GitHub 계정 명의로 실행됨

### 사용량 및 제한

- 인터랙티브 세션과 동일한 방식으로 구독 사용량 소비
- 계정당 일일 실행 횟수 상한 있음 (`claude.ai/settings/usage`에서 확인)
- Extra Usage(종량제 초과) 활성화 시 한도 초과 후에도 계속 실행 가능
- GitHub 이벤트 트리거는 시간당 루틴별·계정별 상한이 적용됨 (초과 이벤트는 드롭)

### 관련 기능

- `/loop`: CLI 세션 내 인-세션 반복 작업
- [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks): 로컬 머신에서 실행되는 로컬 예약 작업
- [MCP Connectors](https://code.claude.com/docs/en/mcp): Slack, Linear, Google Drive 등 외부 서비스 연결
- [GitHub Actions](https://code.claude.com/docs/en/github-actions): CI 파이프라인에서 Claude 실행
