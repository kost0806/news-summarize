---
title:  "[2026-05-29 / Top 10] Show HN: LINQ CLI – 커맨드라인에서 사용할 수 있는 iMessage API"
subtitle: "터미널에서 iMessage를 전송·관리하는 개발자용 CLI 도구"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-29 12:00:00
source_url: "https://linqapp.com/s/cli"
---

> 원본 기사: [https://linqapp.com/s/cli](https://linqapp.com/s/cli)

> HN 토론: [https://news.ycombinator.com/item?id=48313364](https://news.ycombinator.com/item?id=48313364)

### 개요

Linq가 커맨드라인에서 iMessage를 완전히 제어할 수 있는 CLI 도구 'LINQ CLI'를 공개했습니다. 메시지 전송·수신, 그룹 채팅 관리, 웹훅 구독 등 iMessage의 주요 기능을 터미널 명령어로 수행할 수 있으며, 20개 연락처까지는 무료로 사용 가능합니다.

### 주요 내용

- **설치**: `npm install -g @linqapp/cli`로 간편 설치
- **메시지 기능**: 텍스트, 컨페티·불꽃놀이 같은 효과, 탭백(tapback) 반응 전송 지원
- **실시간 수신**: 웹훅 구독 또는 내장 리스너로 수신 메시지 즉시 처리
- **멀티 계정**: AWS CLI 프로필처럼 여러 전화번호·계정 전환 지원
- **탭 완성**: bash·zsh·fish 쉘 전체 탭 완성 지원
- **무료 티어**: 최대 20개 연락처 관리 무료 제공
- **Claude Code 연동**: Linq CLI와 Claude Code를 함께 사용해 iMessage 기반 AI 에이전트를 수 분 만에 배포 가능

### HN 커뮤니티 반응

개발자 커뮤니티에서 높은 관심을 받았습니다. "맥이 있어야 작동하는 것 아닌가"라는 플랫폼 제한 질문이 첫 번째로 올라왔고, Linq 팀이 클라우드 기반 iMessage 인프라를 직접 운영해 맥 없이도 동작한다고 답변했습니다. 자동화 스크립트, 알림 시스템, AI 챗봇 구축 사용 사례가 다양하게 소개됐습니다.

### 시사점

iMessage는 여전히 강력한 사용자 기반을 가진 플랫폼이지만, 공식 API가 없어 개발자들의 접근이 제한적이었습니다. Linq CLI는 이 공백을 메우는 도구로, 특히 Claude Code와의 통합을 통해 Apple 생태계에서 AI 에이전트를 구현하는 새로운 경로를 열어줍니다.
