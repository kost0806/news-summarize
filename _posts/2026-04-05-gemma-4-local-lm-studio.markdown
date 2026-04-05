---
title:  "Google Gemma 4를 로컬에서 실행하기 - LM Studio CLI와 Claude Code 활용 가이드"
subtitle: "LM Studio 0.4.0의 헤드리스 CLI로 Gemma 4 26B 모델을 로컬에서 구동하는 방법"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/posts/2026-04-05-gemma-4-local-lm-studio.jpg"
date:   2026-04-05 12:00:00
source_url: "https://ai.georgeliu.com/p/running-google-gemma-4-locally-with"
---

> 원본 기사: [https://ai.georgeliu.com/p/running-google-gemma-4-locally-with](https://ai.georgeliu.com/p/running-google-gemma-4-locally-with)

### Google Gemma 4 로컬 실행 가이드

Google이 새롭게 출시한 Gemma 4 모델을 LM Studio 0.4.0의 헤드리스 CLI를 활용해 로컬 환경에서 실행하고, Claude Code와 연동하는 방법을 소개하는 기사입니다.

#### Gemma 4란?

Google은 다양한 크기의 Gemma 4 모델 4종을 공개했습니다. 이 중 **26B-A4B** 변형이 특히 주목할 만한데, **Mixture-of-Experts(MoE)** 아키텍처를 채택하고 있습니다. 전체 260억 개의 파라미터 중 순방향 패스당 약 40억 개만 활성화하는 방식으로, 훨씬 큰 모델에 필적하는 성능을 더 적은 컴퓨팅 자원으로 달성합니다.

#### 하드웨어 요구 사항 및 성능

- **테스트 환경**: MacBook Pro 14인치 M4 Pro (48GB 통합 메모리)
- **처리 속도**: 초당 51토큰 생성
- **메모리 사용량**: 기본 모델 약 17.6GB, 기본 48K 컨텍스트 윈도우 기준 총 약 21GB
- **컨텍스트 길이 확장 시**: 컨텍스트 크기가 두 배가 될 때마다 약 3~4GB 추가 소요
- **GPU 사용률**: 최대 90%, 온도 91~92°C 수준으로 정상 범위 유지

Apple Silicon의 통합 메모리 아키텍처 덕분에 별도 GPU VRAM 제한 없이 모델을 구동할 수 있다는 점이 큰 장점입니다.

#### 설치 및 설정 방법

LM Studio 0.4.0에서는 추론 엔진 **llmster**와 **`lms` CLI**가 도입되어, 데스크톱 앱 없이도 명령줄에서 모델을 실행할 수 있습니다.

1. **설치**: 단일 셸 스크립트 실행으로 설치
2. **데몬 시작**: `lms daemon up` 명령으로 헤드리스 데몬 실행
3. **모델 다운로드**: `lms get google/gemma-4-26b-a4b` 명령으로 모델 가져오기

#### 주요 설정 팁

- `--estimate-only` 플래그로 모델 로드 전 메모리 요구량을 사전 확인 가능
- 사용 가능한 메모리에 맞춰 컨텍스트 길이 조절 (전체 메모리에서 OS 오버헤드 차감)
- GPU 오프로딩, 연속 배칭(continuous batching)을 통한 병렬 요청 처리 설정 가능
- TTL(Time-to-Live) 설정으로 자동 언로드 구성
- **MoE 모델에서는 추측적 디코딩(speculative decoding) 사용을 피할 것** — 메모리 대역폭 비효율 발생

#### Claude Code 연동

기사에서는 환경 변수를 설정하여 Claude Code의 요청을 로컬 LM Studio 서버로 리다이렉트하는 셸 함수 템플릿도 제공합니다. 이를 통해 Anthropic API 없이도 완전한 오프라인 코딩 어시스턴트를 구성할 수 있습니다. API 비용 절감과 프라이버시 확보가 가능하지만, 속도 면에서는 트레이드오프가 있습니다.

#### 핵심 요약

| 항목 | 내용 |
|------|------|
| 모델 | Gemma 4 26B-A4B (MoE, 활성 파라미터 4B) |
| 도구 | LM Studio 0.4.0 + lms CLI |
| 권장 사양 | Apple Silicon Mac, 48GB+ 메모리 |
| 성능 | ~51 tokens/sec |
| 메모리 | 기본 17.6GB, 48K 컨텍스트 시 ~21GB |

로컬 LLM 실행에 관심이 있는 개발자에게 실용적인 가이드를 제공하는 기사입니다.
