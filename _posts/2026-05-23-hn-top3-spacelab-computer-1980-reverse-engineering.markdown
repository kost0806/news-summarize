---
title:  "[2026-05-23 / Top 3] 1980년 스페이스랩 컴퓨터 회로 역공학"
subtitle: "HN 13점 · 1개 댓글"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-23 12:02:00
source_url: "https://www.righto.com/2026/05/reverse-engineering-spacelab-computer.html"
---

> 원본 기사: [https://www.righto.com/2026/05/reverse-engineering-spacelab-computer.html](https://www.righto.com/2026/05/reverse-engineering-spacelab-computer.html)

> HN 토론: [https://news.ycombinator.com/item?id=48248954](https://news.ycombinator.com/item?id=48248954)

### 개요

Ken Shirriff가 1980년대 스페이스랩(Spacelab) 프로그램에 사용된 Mitra 125 MS 미니컴퓨터의 ALU 보드를 역공학한 과정을 상세히 설명한 기술 블로그 글입니다. 마이크로프로세서 없이 TTL 칩으로 구성된 이 컴퓨터의 내부 구조를 분석했습니다.

### 주요 내용

- **Mitra 125 MS**: 프랑스산 16비트 미니컴퓨터로 NASA 스페이스랩 임무에 탑재
- **마이크로프로세서 없는 설계**: 단일 CPU 칩 대신 74181 ALU 칩 등 개별 TTL 칩들로 구성
- **32비트 ALU**: 놀랍게도 16비트 머신임에도 32비트 ALU를 구현 — 두 보드가 협력하여 처리
- **역공학 방법론**: 회로도 없이 실물 보드의 연결을 추적하여 기능 복원
- **스페이스랩 역할**: 이 컴퓨터는 Spacelab의 중앙 처리 시스템으로 과학 실험 데이터를 관리

### HN 커뮤니티 반응

HN 점수 13점, 댓글 1개. 저자가 직접 댓글로 독자 질문을 환영했습니다. Ken Shirriff는 아폴로 컴퓨터, 8087 수학 보조프로세서 등의 역공학으로 유명한 블로거입니다.

### 시사점

마이크로프로세서가 등장하기 전 시대의 컴퓨터 설계 철학을 엿볼 수 있는 귀중한 역사적 분석입니다. 우주 탐사에 사용된 컴퓨팅 하드웨어의 내부를 들여다보는 드문 기회입니다.
