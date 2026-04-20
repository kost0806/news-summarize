---
title:  "[2026-04-20 / Top 5] 다음 번 워드프레스를 구축하기 위한 경쟁"
subtitle: "Cloudflare의 EmDash 등장으로 새로운 CMS 패러다임이 열리다"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-20 11:30:00
source_url: "https://opencomputer.dev/blog/the-race-to-build-the-next-wordpress/"
---

> 원본 기사: [https://opencomputer.dev/blog/the-race-to-build-the-next-wordpress/](https://opencomputer.dev/blog/the-race-to-build-the-next-wordpress/)

### 개요

OpenComputer.dev의 이 글은 웹 개발 생태계에서 워드프레스(WordPress)의 다음 세대를 차지하려는 경쟁을 분석합니다. AI 에이전트 시대가 도래하면서 기존 CMS의 패러다임이 근본적으로 바뀌고 있으며, 이 공백을 차지하려는 플레이어들이 속속 등장하고 있습니다.

### 시대의 전환

이 글의 핵심 명제는 다음과 같습니다: **AI 에이전트 하니스(agent harness)는 2000년대 초 인터넷에서 워드프레스가 했던 역할을 이 시대에 담당하게 될 것이며, 그 자리를 차지하기 위한 경쟁이 이미 시작됐다.**

또한 AI 에이전트는 새 사이트를 만들 때 워드프레스 플랫폼을 선택하지 않을 것이며, 워드프레스를 구식으로 여기는 새로운 세대의 개발자들이 대거 등장하고 있습니다.

### 핵심 경쟁자: Cloudflare의 EmDash

가장 주목받는 후보는 **Cloudflare가 공개한 EmDash**입니다. Cloudflare는 EmDash를 "워드프레스의 정신적 후계자(spiritual successor to WordPress)"라고 소개하며 다음 특징을 강조합니다:

- **TypeScript로 완전히 새로 작성**되어 현대적 워크플로우에 최적화
- **서버리스(serverless)**로 동작하며 Cloudflare Workers 위에서 실행
- **Astro**를 기반으로 구축
- **워드프레스의 최대 문제인 플러그인 보안 해결**: 플러그인이 독립적인 보안 샌드박스에서 실행되어 사이트 코드와 격리됨
- **내장 AI 에이전트 지원** 및 MCP 서버 연동
- **오픈소스**로 공개

### 플러그인 보안의 혁신

워드프레스의 오랜 아킬레스건은 악성 또는 취약한 플러그인이었습니다. EmDash는 이를 근본적으로 해결합니다:
- 플러그인은 어떤 라이선스도 가질 수 있고 EmDash와 독립적으로 실행됩니다
- 플러그인 코드는 **독립 보안 샌드박스에서 실행**되므로 플러그인 코드를 직접 확인하지 않아도 신뢰할 수 있습니다

### 더 넓은 맥락

헤드리스 CMS(Headless CMS) 시장도 빠르게 성장하고 있습니다. 콘텐츠와 프레젠테이션 레이어를 분리하는 이 방식은 API 우선(API-first) 아키텍처와 AI 에이전트 주도의 콘텐츠 생성에 더 잘 맞습니다.

### 시사점

웹 개발의 지형이 근본적으로 변하고 있습니다. 워드프레스가 지난 20여 년간 차지했던 CMS 생태계의 중심 자리를 누가 대체할 것인가는 단순한 기술적 질문을 넘어, AI 시대 웹의 근본 아키텍처를 결정하는 중요한 싸움입니다. EmDash와 같은 새로운 도전자들이 AI 에이전트 친화적 설계와 보안 혁신을 앞세워 그 자리를 狙いつつ있습니다.
