---
title:  "[2026-05-23 / Top 1] `<dl>`에 대하여"
subtitle: "HN 203점 · 60개 댓글"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-23 12:00:00
source_url: "https://benmyers.dev/blog/on-the-dl/"
---

> 원본 기사: [https://benmyers.dev/blog/on-the-dl/](https://benmyers.dev/blog/on-the-dl/)

> HN 토론: [https://news.ycombinator.com/item?id=48247325](https://news.ycombinator.com/item?id=48247325)

### 개요

Ben Myers가 작성한 HTML `<dl>`, `<dt>`, `<dd>` 요소에 대한 심층 해설 글입니다. 이름-값 쌍을 마크업하기 위한 설명 목록(Description List)의 구조, 사용법, 그리고 접근성 측면의 이점을 다룹니다. D&D 스탯블록 예시를 포함해 실무에서 이 요소가 얼마나 활용 가능한지 구체적으로 설명합니다.

### 주요 내용

- **설명 목록 구조**: `<dl>`(설명 목록), `<dt>`(용어), `<dd>`(설명)으로 구성된 HTML 시맨틱 구조 해설
- **다중 값 처리**: 하나의 용어에 여러 설명이 붙거나, 여러 용어가 같은 설명을 공유하는 패턴 지원
- **접근성**: 스크린 리더가 목록의 항목 수, 현재 위치 등을 안내해 접근성 향상
- **실용 예시**: D&D 스탯블록, 메타데이터 UI 등 다양한 패턴에 `<dl>` 적용 가능
- **제약사항**: `<dl>` 내부에서 wrapper로는 `<div>`만 허용되며, 레이아웃 유연성이 부족하다는 의견도 존재

### HN 커뮤니티 반응

HN 점수 203점, 댓글 60개로 높은 관심을 받았습니다. 커뮤니티에서는 `<dl>`의 실용성에 대한 찬반 논쟁이 벌어졌습니다. 일부는 현실 레이아웃에 비해 구조가 너무 엄격하다고 비판했고, 다른 쪽에서는 ARIA 속성과의 조합 및 스크린 리더 지원이 생각보다 좋다는 점을 강조했습니다.

### 시사점

흔히 간과되는 HTML 시맨틱 요소인 `<dl>`의 재발견입니다. 접근성과 시맨틱 웹을 중시하는 프론트엔드 개발자라면 주목할 만한 글입니다.
