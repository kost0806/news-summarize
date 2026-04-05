---
title:  "Claude Code 소스 유출, 그리고 모든 LLM에서 돌아가는 OpenClaude의 등장"
subtitle: "npm 소스맵 유출로 드러난 에이전트 프레임워크의 진짜 경쟁력"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/posts/2026-04-05-claude-code-source-leak-openclaude.png"
date:   2026-04-05 12:00:00
source_url: "https://wikidocs.net/blog/@jaehong/10423/"
---

> 원본 기사: [https://wikidocs.net/blog/@jaehong/10423/](https://wikidocs.net/blog/@jaehong/10423/)

### 사건 개요

2026년 3월 31일, Anthropic의 Claude Code 소스코드가 npm 소스맵을 통해 의도치 않게 공개되었습니다. 이를 포크하여 OpenAI 호환 API 어댑터를 추가한 **OpenClaude** 프로젝트가 등장했으며, **6개 파일, 786줄 코드 변경, 외부 의존성 추가 0**이라는 최소한의 수정만으로 GPT-4o, DeepSeek, Gemini, Llama, Mistral, Ollama 등 OpenAI Chat Completions API를 지원하는 사실상 모든 LLM에서 Claude Code의 전체 도구 시스템을 그대로 사용할 수 있게 되었습니다.

### npm 소스맵 유출 — 보안 사각지대

npm 생태계에서 프로덕션 패키지에 소스맵이 포함되면 원본 TypeScript 소스가 사실상 공개됩니다. `.npmignore` 또는 `files` 필드 설정 누락 시 발생할 수 있는 흔한 보안 문제로, 이번 사건은 이 사각지대를 정면으로 드러냈습니다.

### 핵심 구현 — openaiShim.ts (724줄)

OpenClaude의 핵심은 724줄의 `openaiShim.ts` 파일 하나입니다. 이 심(shim)은 다음을 수행합니다:

- Anthropic SDK 인터페이스 요청을 OpenAI Chat Completions API 형식으로 변환
- Anthropic의 메시지 블록을 OpenAI 메시지로 변환
- `tool_use`/`tool_result` 형식을 OpenAI의 function calling으로 변환
- OpenAI SSE 스트리밍을 Anthropic 스트림 이벤트로 역변환

환경 변수 3개만 설정하면 바로 사용 가능합니다:

```
export CLAUDE_CODE_USE_OPENAI=1
export OPENAI_API_KEY=sk-your-key
export OPENAI_MODEL=gpt-4o
```

로컬 모델(Ollama) 사용 시에는 `OPENAI_BASE_URL=http://localhost:11434/v1`을 추가하면 됩니다.

### 모델별 성능 비교

| 모델 | 도구 호출 | 코드 품질 | 특징 |
|------|---------|---------|------|
| GPT-4o | Excellent | Excellent | 최고 성능 |
| DeepSeek-V3 | 우수 | 우수 | GPT-4o 추격 |
| Gemini 2.0 Flash | Excellent | Good | 속도 압도적 |
| Llama 3.3 70B | Good | Good | 실사용 가능 |
| Mistral Large | Good | Good | 실사용 가능 |
| 7B 이하 모델 | 제한적 | - | 에이전트 부적합 |

도구 호출 능력이 핵심 성능 지표로, GPT-4o가 가장 우수하고 소형 모델들은 에이전트 작업에 제약이 있습니다.

### 누락된 기능

OpenClaude에서는 Anthropic 고유 기능 일부가 빠져 있습니다:

1. **확장된 사고(Extended Thinking)** 모드
2. **프롬프트 캐싱** — 장시간 에이전트 세션에서 비용 누적 영향
3. Anthropic 전용 베타 기능
4. 최대 출력 토큰이 32K로 기본 설정

### 업계에 대한 함의

**에이전트 프레임워크의 경쟁력 원천 변화**: Claude Code의 진짜 가치는 모델 자체가 아니라 도구 오케스트레이션, 스트리밍 아키텍처, 에이전트 시스템 설계에 있으며, 모델 종속성이 해자(moat)가 될 수 없다는 점을 시사합니다.

**코드 에이전트 상향 평준화**: "어떤 모델을 쓰느냐"보다 "도구 체인을 얼마나 잘 설계했느냐"가 경쟁력의 핵심으로 이동할 가능성을 보여줍니다.

**법적 리스크**: "교육 및 연구 목적"으로 명시되었으나, 공개적으로 접근 가능했다는 것과 사용해도 된다는 것은 전혀 다른 문제입니다.

### 실무적 시사점

- **API 심 패턴**으로 LLM 공급자 교체 가능성 확보
- 도구 정의와 모델 호출의 깔끔한 분리
- 덕 타이핑(duck typing)으로 SDK 인터페이스 추상화
- 단순 작업에는 저비용 모델, 복잡한 작업에는 고성능 모델을 사용하는 **모델 라우팅 전략**이 이론적으로 가능

### 핵심 결론

AI 코딩 도구의 경쟁 축이 **"어떤 모델을 독점하느냐"**에서 **"어떤 도구 경험을 만드느냐"**로 빠르게 이동하고 있다는 점을 OpenClaude가 실증적으로 보여주고 있습니다.
