---
title:  "[2026-05-29 / Top 4] 가위바위보의 비밀 정원"
subtitle: "가위바위보를 확장하면 드러나는 게임 이론의 숨겨진 세계"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-29 12:00:00
source_url: "https://theshamblog.com/the-secret-garden-of-rock-paper-scissors/"
---

> 원본 기사: [https://theshamblog.com/the-secret-garden-of-rock-paper-scissors/](https://theshamblog.com/the-secret-garden-of-rock-paper-scissors/)

> HN 토론: [https://news.ycombinator.com/item?id=48323266](https://news.ycombinator.com/item?id=48323266)

### 개요

The Shamblog의 이 글은 가위바위보(RPS)를 선택지 3개 이상으로 확장할 경우 나타나는 다채로운 게임 구조를 탐구합니다. 일부 결과를 무승부로 허용하면 단순해 보이는 게임 뒤에 풍부한 수학적 정원이 숨어 있음을 발견할 수 있습니다. 저자는 Claude Code를 활용해 유효한 게임 구조를 탐색하는 코드를 작성했습니다.

### 주요 내용

- **기본 RPS**: 3가지 선택, 각 선택이 하나를 이기고 하나에 지며, 전체 게임의 1/3이 무승부
- **RPSLS(가위바위보-도마뱀-스팍)**: 5가지 선택, 각 선택이 두 개를 이기고 두 개에 지며, 무승부 비율 1/5로 감소
- **비대칭 구조 허용**: 이기는 수와 지는 수를 같게 하지 않아도 유효한 게임이 가능 → 더욱 다양한 전략 구조 출현
- **'무승부 포함 RPS'의 발견**: 일부 결과를 무승부로 허용하면 n=3, 4, 5 개의 선택지에서 수십 가지의 서로 다른 게임 동역학이 존재함
- **분류 기준**: 궤도(orbit) 수, 무승부 비율, 지니 계수(Gini coefficient)로 게임 구조 정렬
- **Claude Code 활용**: 저자가 AI의 도움 없이 글을 직접 작성했으나, 유효한 게임을 탐색하는 코드는 Claude Code로 바이브 코딩(vibe coding)

### HN 커뮤니티 반응

HN 독자들은 게임 이론과 수학적 우아함이 결합된 이 글에 높은 관심을 보였습니다. "완전히 공정한 게임은 대칭적 구조를 가져야 한다"는 직관에 도전하는 내용이 흥미롭다는 반응이 많았습니다. 보드게임 및 카드게임 설계에 응용할 수 있다는 댓글도 달렸습니다.

### 시사점

단순해 보이는 규칙 시스템도 파라미터를 조금만 바꾸면 드러나지 않던 복잡성을 품고 있습니다. Claude Code 같은 AI 도구가 수학적·알고리즘적 탐구를 빠르게 코드로 연결해 주면서, 연구자와 호기심 많은 개인이 더 깊은 탐구를 손쉽게 수행할 수 있게 됐습니다.
