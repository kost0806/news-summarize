---
title:  "[2026-05-11 / Top 5] Obsidian 플러그인, 원격 접근 트로이목마 배포에 악용됨"
subtitle: "악성 Obsidian 플러그인이 Phantom Pulse RAT 캠페인에 사용된 보안 사고"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-11 05:00:00
source_url: "https://cyber.netsecops.io/articles/obsidian-plugin-abused-in-campaign-to-deploy-phantom-pulse-rat/"
---

> 원본 기사: [https://cyber.netsecops.io/articles/obsidian-plugin-abused-in-campaign-to-deploy-phantom-pulse-rat/](https://cyber.netsecops.io/articles/obsidian-plugin-abused-in-campaign-to-deploy-phantom-pulse-rat/)
> HN 토론: [https://news.ycombinator.com/item?id=48088576](https://news.ycombinator.com/item?id=48088576) | 점수: 37 | 댓글: 16

### 개요

인기 노트 앱 Obsidian의 커뮤니티 플러그인이 "Phantom Pulse RAT(원격 접근 트로이목마)" 배포 캠페인에 악용된 사례를 다룬 사이버보안 보고서입니다. 신뢰받는 오픈소스 생태계를 통한 공급망 공격(Supply Chain Attack)의 위험성을 잘 보여줍니다.

### 주요 내용

- **공격 방식**: 정상적으로 보이는 Obsidian 플러그인에 악성 코드를 삽입하여 배포. 사용자가 설치하면 백그라운드에서 Phantom Pulse RAT가 실행됨
- **Phantom Pulse RAT**: 공격자가 감염된 기기를 원격으로 제어하고, 파일 수집·화면 캡처·키로깅 등의 기능을 수행하는 악성 소프트웨어
- **타겟**: 보안·기술·연구 분야 전문가들이 주로 Obsidian을 사용하는 점을 감안, 고가치 정보를 노린 표적 공격으로 추정
- **탐지 어려움**: 신뢰받는 앱의 플러그인으로 위장하여 보안 솔루션의 탐지를 우회

### 대응 방법

- Obsidian 플러그인 설치 시 공식 커뮤니티 플러그인 목록 및 GitHub 소스 코드 검토
- 알 수 없는 출처의 플러그인 설치 자제
- 정기적인 설치된 플러그인 감사 및 불필요한 플러그인 제거
- 엔드포인트 보안 솔루션 업데이트 및 네트워크 트래픽 모니터링

### 시사점

오픈소스 플러그인 생태계는 강력한 확장성을 제공하지만, 동시에 공급망 공격의 벡터가 됩니다. Obsidian뿐 아니라 VS Code, Vim, Neovim 등 플러그인 기반 도구를 사용하는 모든 개발자는 설치하는 확장 기능의 출처와 코드를 주의 깊게 확인해야 합니다.
