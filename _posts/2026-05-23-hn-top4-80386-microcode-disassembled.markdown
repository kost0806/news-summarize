---
title:  "[2026-05-23 / Top 4] 80386 마이크로코드 역어셈블 완성"
subtitle: "HN 149점 · 23개 댓글"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-23 12:03:00
source_url: "https://www.reenigne.org/blog/80386-microcode-disassembled/"
---

> 원본 기사: [https://www.reenigne.org/blog/80386-microcode-disassembled/](https://www.reenigne.org/blog/80386-microcode-disassembled/)

> HN 토론: [https://news.ycombinator.com/item?id=48247004](https://news.ycombinator.com/item?id=48247004)

### 개요

Intel 80386 프로세서의 마이크로코드 ROM을 역어셈블하는 데 성공한 협업 프로젝트를 소개합니다. 94,720비트의 마이크로코드를 사전 문서 없이 고해상도 다이 이미지 분석과 이미지 처리, AI 보조 방법론으로 해독해 냈습니다.

### 주요 내용

- **94,720비트 마이크로코드**: Intel 80386의 ROM에서 이진 데이터를 추출 — 아무런 공식 문서 없이 진행
- **215개 진입점**: 역어셈블 결과 215개의 마이크로코드 엔트리 포인트 발견 (8086의 60개와 비교)
- **40년 묵은 버그 발견**: I/O 권한 비트맵(IOPB) 처리 코드에서 잠재적 버그 발견
- **협업 팀**: Daniel Balsom, Smartest Blob, nand2mario, Ken Shirriff 등이 함께 참여
- **방법론**: 다이 사진의 ROM 패턴에서 0/1 비트를 식별하고, 마이크로아키텍처를 추론하여 역어셈블

### HN 커뮤니티 반응

HN 점수 149점, 댓글 23개로 큰 반응을 얻었습니다. 커뮤니티에서는 이 작업을 "피크 HN(peak Hacker News)"이라 칭하며 찬사를 보냈습니다. 다이 이미지에서 마이크로코드를 추출하는 방법에 대한 기술적 논의도 이어졌으며, nand2tetris나 Petzold의 책 같은 CPU 아키텍처 학습 자료도 추천되었습니다.

### 시사점

40여 년 전에 설계된 x86 아키텍처의 최하위 레이어를 밝혀낸 역사적인 역공학 성과입니다. 이번 성과는 z386 오픈소스 FPGA 프로젝트의 기반이 되기도 했습니다.
