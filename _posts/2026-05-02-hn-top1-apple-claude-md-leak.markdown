---
title:  "[2026-05-02 / Top 1] 애플, 서포트 앱에 Claude.md 내부 파일 실수로 포함"
subtitle: "유출된 설정 파일이 애플의 내부 AI 시스템 '주노'와 클로드 코드 사용 사실을 드러내다"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-02 12:00:00
source_url: "https://www.news9live.com/technology/artificial-intelligence/apple-support-app-claude-md-files-leak-claude-code-ai-tools-2966945"
---

> 원본 기사: [https://www.news9live.com/technology/artificial-intelligence/apple-support-app-claude-md-files-leak-claude-code-ai-tools-2966945](https://www.news9live.com/technology/artificial-intelligence/apple-support-app-claude-md-files-leak-claude-code-ai-tools-2966945)

### 애플 서포트 앱 v5.13 업데이트에서 내부 AI 설정 파일 유출

2026년 5월 1일, 애플이 서포트 앱 버전 5.13을 배포하면서 개발 환경에서만 사용해야 할 **CLAUDE.md 파일**이 앱 패키지에 실수로 포함된 사실이 밝혀졌습니다. 연구자 Aaron Perris(@aaronp613)가 가장 먼저 이를 발견해 X(구 트위터)에 공개했습니다.

#### CLAUDE.md 파일이란?

CLAUDE.md는 Anthropic의 AI 코딩 어시스턴트 **Claude Code**가 세션 시작 시 자동으로 읽는 마크다운 설정 파일입니다. 개발자들은 이 파일을 통해 코딩 표준, 아키텍처 결정 사항, 선호 라이브러리 등을 AI에게 사전 지시할 수 있습니다. 원래 공개 앱 빌드에 포함되어서는 안 되는 파일입니다.

#### 유출 파일이 드러낸 내용

유출된 CLAUDE.md 파일에는 애플의 고객 지원 시스템 설계가 상세히 기록되어 있었습니다.

- **이중 백엔드 구조**: '주노 AI(Juno AI)'가 자동 응답을 담당하고, 필요 시 실제 상담원(Live Agent)이 개입하는 하이브리드 모델
- **'주노 AI'**: 애플이 내부적으로 사용하는 대규모 언어 모델 플랫폼의 브랜드명으로 추정되며, Anthropic의 Claude를 기반으로 함
- **비동기 스트리밍, 백엔드 통합, 메시지 처리 역할, 세션 지속성** 등 기술 요소에 대한 구체적 지침 포함

#### 애플의 빠른 대응

발견 직후 몇 시간 안에 애플은 **긴급 패치 버전 5.13.1**을 배포해 해당 파일을 제거했습니다. 그러나 이미 파일 내용이 온라인에 확산된 후였습니다.

#### 업계 반응

이번 사고는 Hacker News에서 큰 화제가 되었습니다. 여러 이유에서 주목을 받았습니다.

- 애플이 공식적으로 AI 파트너십을 인정한 적 없는 Anthropic의 Claude를 내부 개발에 폭넓게 활용하고 있다는 사실이 확인됨
- 빌드 파이프라인에서 개발 전용 파일이 프로덕션에 유출되는 공급망 보안 문제를 시사
- AI 코딩 도구(Claude Code 등)가 빅테크 기업의 내부 개발 흐름에 깊이 통합되고 있다는 방증

#### 의의

이번 유출은 단순한 실수를 넘어, AI 도구가 실리콘밸리 대형 기업들의 소프트웨어 개발 사이클에 얼마나 깊이 침투해 있는지를 보여주는 사건으로 평가받고 있습니다.
