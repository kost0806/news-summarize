---
title:  "월 $20 인프라로 $10K MRR 여러 개를 운영하는 법"
subtitle: "Steve Hanov: Go + SQLite + 저렴한 VPS로 최소 비용 SaaS를 유지하는 기술 스택 전략"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-16 09:30:00
source_url: "https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack"
---

> 원본 기사: [https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack](https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack)

### 개요

개발자 Steve Hanov가 **websequencediagrams.com** 등 여러 SaaS 제품을 월 **$20 미만**의 인프라 비용으로 운영하는 기술 스택을 공유했습니다. Hacker News에서 이 글은 큰 반향을 일으키며 인디 해커와 부트스트래퍼 커뮤니티에서 광범위하게 공유됐습니다.

### 핵심 철학

> "비용이 제로에 가깝게 유지되면 백만 달러 펀딩을 받고 높은 번 레이트로 운영하는 것과 동일한 런웨이를 가집니다. 스트레스가 적고, 아키텍처가 단순해지며, 제품-시장 적합성을 찾을 시간이 충분해집니다."

### 기술 스택 상세

#### 백엔드 언어: Go

- 정적 컴파일되어 단일 바이너리로 배포 가능
- LLM이 추론하기 쉬운 언어
- 배포 방법: 노트북에서 컴파일 → `scp`로 $5 VPS에 전송 → 실행

#### 데이터베이스: SQLite (WAL 모드)

PostgreSQL 대신 **SQLite + WAL(Write-Ahead Logging)** 모드를 사용합니다. 별도 DB 서버가 없어 운영 복잡도가 0에 수렴하며, 단일 서버 SaaS의 일반적인 부하에는 충분한 성능을 냅니다.

#### 서버: 저렴한 VPS

AWS 대신 **Linode / DigitalOcean** 의 $5~$10/월 VPS를 사용합니다. 관리형 클라우드 서비스 없이 직접 운영해 비용을 최소화합니다.

#### AI 통합: 두 가지 경로

| 용도 | 도구 |
|------|------|
| 사용자 대면 저지연 채팅 | **OpenRouter** (OpenAI 호환 단일 엔드포인트로 모든 주요 모델 접근) |
| 배치 AI 작업 | 로컬 GPU + **Ollama / VLLM** |

#### 개발 도구

- **GitHub Copilot**: 에이전트가 30분 동안 수백 개의 파일을 변경할 수 있으며 요청당 약 $0.04
- **smhanov/auth**: 저자가 직접 만든 인증 라이브러리. DB에 직접 통합되어 회원가입·세션·비밀번호 재설정을 처리하고 Google, Facebook, X, SAML 로그인을 지원

### 전체 월 비용 구성

| 항목 | 비용 |
|------|------|
| VPS (Linode/DigitalOcean) | $5~$10 |
| 도메인 | ~$1 |
| AI API (OpenRouter, 배치 제외) | 사용량 기반, 낮게 유지 |
| **합계** | **~$20/월** |

### HN 반응

"$20 스택이 $1M 펀딩과 같은 런웨이를 줄 수 있다"는 주장에 커뮤니티가 큰 호응을 보냈습니다. 일부는 SQLite의 동시성 한계를 지적했지만, 저자는 단일 서버로 운영하는 SaaS에는 WAL 모드로 충분하다고 반박했습니다. 또한 Hetzner를 VPS 대안으로 추천하는 댓글도 많았습니다.
