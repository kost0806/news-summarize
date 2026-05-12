---
title:  "[2026-05-12 / Top 1] TanStack: 여러 npm 최신 릴리즈가 침해됨"
subtitle: "npm 공급망 공격으로 TanStack 패키지가 악성 코드에 감염"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-12 01:00:00
source_url: "https://github.com/TanStack/router/issues/7383"
---

> 원본 기사: [https://github.com/TanStack/router/issues/7383](https://github.com/TanStack/router/issues/7383)
> HN 토론: [https://news.ycombinator.com/item?id=48100706](https://news.ycombinator.com/item?id=48100706) | 점수: 440 | 댓글: 133

### 개요

인기 React 에코시스템 라이브러리 TanStack의 여러 npm 패키지 최신 릴리즈가 공급망 공격(Supply Chain Attack)에 의해 침해되었습니다. TanStack 팀이 직접 GitHub 이슈를 통해 이 보안 사고를 공개하며 조사 경과를 공유했습니다.

### 공격 개요

- **피해 패키지**: TanStack Router를 포함한 여러 npm 패키지의 최신(latest) 릴리즈
- **공격 유형**: 자가 전파형(self-spreading) npm 공급망 공격 — Step Security 블로그에서 "Mini Shai Hulud"로 명명
- **발견 경위**: 사용자들이 이상한 동작을 보고하면서 팀이 조사에 착수
- **대응**: TanStack 팀은 침해된 릴리즈를 신속히 철회하고 포스트모템(사후 분석)을 공개

### TanStack의 공식 발표

TanStack 팀은 `tanstack.com/blog/npm-supply-chain-compromise-postmortem`에 전체 포스트모템을 게시했습니다. 이 문서에는 공격 타임라인, 발견된 정보, 그리고 향후 재발 방지 방안이 포함되어 있습니다.

팀은 이슈 페이지에서 "이 보안 사고를 적극적으로 조사하고 있으며 조사 결과를 여기에 공유하고 있다"고 밝혔습니다.

### 영향 범위 및 권고 사항

- **사용자 행동 권고**: TanStack 패키지를 사용하는 프로젝트는 즉시 `package-lock.json` 또는 `yarn.lock`을 확인하고, 침해된 버전을 사용하고 있다면 업데이트 필요
- **공급망 공격의 위험성**: npm 생태계를 표적으로 한 공급망 공격이 점점 정교해지고 있으며, 신뢰하는 라이브러리도 안전하지 않을 수 있음
- **보안 도구 사용**: Step Security 같은 도구를 활용해 CI/CD 파이프라인의 공급망 보안을 강화할 것을 권장

### HN 반응

HN에서 440점을 기록하며 뜨거운 반응을 얻었습니다. 커뮤니티는 npm 생태계의 구조적 취약성과 공급망 공격에 대한 방어 방법을 논의했습니다.
