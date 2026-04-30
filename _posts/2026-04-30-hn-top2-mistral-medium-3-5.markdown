---
title:  "[2026-04-30 / Top 2] Vibe의 원격 에이전트. Mistral Medium 3.5로 구동."
subtitle: "Mistral AI의 128B 밀집 모델과 클라우드 기반 코딩 에이전트 출시"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-30 12:01:00
source_url: "https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5"
---

> 원본 기사: [https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5)

### Mistral Medium 3.5 및 Vibe 원격 에이전트 발표

Mistral AI가 2026년 4월 29일, 세 가지 주요 발표를 동시에 내놓았습니다: **Mistral Medium 3.5** 모델, **Vibe 원격 에이전트**, 그리고 **Le Chat Work Mode**입니다.

#### Mistral Medium 3.5

Mistral의 첫 번째 플래그십 통합 모델로, 단일 가중치 세트에서 명령어 이해, 추론, 코딩을 모두 처리하는 **128B 밀집 모델**입니다.

주요 사양:
- **컨텍스트 윈도우:** 256k 토큰
- **벤치마크:** SWE-Bench Verified에서 **77.6%** 달성
- **비전:** 처음부터 학습된 비전 인코더가 다양한 이미지 크기와 비율 처리
- **가변 추론:** 요청별로 추론 노력을 설정 가능하여 빠른 답변부터 심층 사고까지 대응
- **배포:** 최소 4개의 GPU로 자체 호스팅 가능
- **라이선스:** 수정 MIT 라이선스로 오픈 웨이트 공개

이전 모델인 Devstral 2, Qwen3.5 397B A17B를 코딩 및 에이전트 벤치마크에서 능가합니다.

#### Vibe 원격 코딩 에이전트

기존 코딩 에이전트가 로컬 환경에서만 동작하던 한계를 넘어, Mistral은 이를 클라우드로 이동시켰습니다. Vibe 원격 에이전트는:

- **비동기 실행:** 백그라운드에서 독립적으로 실행되며 완료 시 알림
- **병렬 처리:** 여러 에이전트가 동시에 실행 가능
- **시작 방법:** Mistral Vibe CLI 또는 Le Chat에서 직접 시작
- **클라우드 이전:** 로컬 CLI 세션을 클라우드로 "텔레포트" 가능
- **결과물:** GitHub Pull Request 형태로 완성된 코드 제출

#### Le Chat Work Mode

Le Chat의 새로운 Work Mode(미리보기)는 복잡한 멀티스텝 작업을 위한 강력한 에이전트를 제공합니다. 이메일 분류, 리서치 합성, 크로스 도구 작업 등 복잡한 업무 흐름을 처리할 수 있습니다.

#### 의의

Mistral Medium 3.5는 클로즈드 모델에 대한 의존 없이 기업급 AI 성능을 자체 인프라에서 구현할 수 있는 가능성을 보여줍니다. 특히 코딩 에이전트의 클라우드 이전은 AI 개발 환경의 새로운 패러다임을 제시하고 있습니다.
