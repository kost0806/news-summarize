---
title:  "[2026-05-23 / Top 6] PHP의 기이한 점들"
subtitle: "HN 29점 · 28개 댓글"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-23 12:05:00
source_url: "https://flowtwo.io/post/php%27s-oddities"
---

> 원본 기사: [https://flowtwo.io/post/php%27s-oddities](https://flowtwo.io/post/php%27s-oddities)

> HN 토론: [https://news.ycombinator.com/item?id=48199314](https://news.ycombinator.com/item?id=48199314)

### 개요

PHP를 사용하면서 마주칠 수 있는 두 가지 주요 이상 동작을 심층 분석한 글입니다. 배열의 실제 동작 방식과 타입 지정 클래스 속성의 숨겨진 "미초기화(uninitialized)" 상태에 대해 다룹니다.

### 주요 내용

- **배열 = 순서 있는 딕셔너리**: PHP 배열은 실제로 순서 있는 키-값 딕셔너리로, `array_filter()` 등으로 원소를 제거해도 키가 자동 재인덱싱되지 않아 예상치 못한 버그 발생 가능
- **미초기화 속성 상태**: 타입이 지정된 클래스 속성은 NULL과 별개인 "uninitialized" 상태가 존재하며, 접근 시 치명적 오류(fatal error) 발생
- **방어 코드의 어려움**: `is_null()`, `isset()`, `property_exists()`, `empty()` 중 어느 것을 써야 하는지 모호함
- **현대 PHP의 개선**: PHP는 동적 속성 deprecated 등 점진적으로 개선 중이지만 하위 호환성 문제가 여전히 남아 있음

### HN 커뮤니티 반응

HN 점수 29점, 댓글 28개. 커뮤니티는 대체로 현대 PHP가 평판보다 낫다는 데 동의했습니다. 배열의 동작이 맥락을 알면 예측 가능하다는 옹호 의견과, PHP의 느슨한 타입 비교와 강제 변환에 대한 비판이 함께 나왔습니다.

### 시사점

PHP는 오랜 이력만큼 설계 상의 모순을 안고 있습니다. 이 글은 PHP 개발자라면 알아야 할 함정들을 명확히 짚어줍니다.
