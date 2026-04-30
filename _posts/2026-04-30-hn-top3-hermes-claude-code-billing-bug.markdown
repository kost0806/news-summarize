---
title:  "[2026-04-30 / Top 3] git 커밋 메시지의 HERMES.md가 Claude Code에서 청구 버그 유발"
subtitle: "Max 플랜 사용자에게 $200 초과 청구 발생, Anthropic이 환불 조치"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-30 12:02:00
source_url: "https://github.com/anthropics/claude-code/issues/53262"
---

> 원본 기사: [https://github.com/anthropics/claude-code/issues/53262](https://github.com/anthropics/claude-code/issues/53262)

### Claude Code의 심각한 청구 버그 발견

Claude Code v2.1.119에서 git 커밋 메시지에 대소문자를 구분하는 문자열 `HERMES.md`가 포함될 경우, API 요청이 Max 플랜 할당량 대신 **추가 사용(extra usage) 청구**로 라우팅되는 심각한 버그가 발견되었습니다.

#### 버그의 원인

Claude Code는 시스템 프롬프트에 최근 git 커밋 히스토리를 포함시킵니다. 이 커밋 메시지에 정확히 `HERMES.md`(대소문자 구분)라는 문자열이 있으면, 서버 측 라우팅 로직이 요청을 플랜 할당량이 아닌 추가 사용 청구로 전환합니다.

#### 어떤 경우에 버그가 발생하나?

| 커밋 메시지 | 결과 |
|---|---|
| `HERMES.md` | **실패** — 추가 사용 청구로 라우팅 |
| `test HERMES.md test` | **실패** |
| `hermes.md` (소문자) | 정상 동작 |
| `HERMES` (확장자 없음) | 정상 동작 |
| `HERMES.txt` | 정상 동작 |
| `AGENTS.md` 또는 `README.md` | 정상 동작 |

파일이 실제로 디스크에 존재할 필요도 없으며, 커밋 메시지 문자열만으로도 버그가 발생합니다.

#### 피해 규모

한 사용자는 Max 20x 플랜($200/월)을 구독 중이었음에도 불구하고, 플랜 할당량의 13%만 사용한 상태에서 **추가 사용 크레딧 $200.98**이 소진되었습니다. 추가 사용량이 소진되자 프로젝트가 완전히 사용 불가 상태가 되었고, 오류 메시지("You're out of extra usage")에는 콘텐츠 기반 라우팅이 원인이라는 어떠한 힌트도 없었습니다.

#### 재현 방법

재현은 간단합니다:
1. `HERMES.md`를 커밋 메시지에 포함하여 git 저장소 생성
2. Claude Code 실행 시 "You're out of extra usage" 오류 발생

#### Anthropic의 대응

유지 관리자 ThariqS는 문제를 인지하였음을 확인하고, 영향받은 사용자들에게 **환불 및 추가 1개월 크레딧($200)을 이메일로 통지**하기로 하였습니다.

#### 근본적인 문제점

API 요청 청구는 절대로 git 커밋 메시지의 내용에 따라 달라져서는 안 됩니다. Max 플랜 구독자의 모든 요청은 저장소 히스토리와 무관하게 포함된 플랜 할당량으로 먼저 라우팅되어야 합니다. 이 버그는 HN에서 큰 반향을 일으키며 Anthropic이 신속히 대응하게 만들었습니다.
