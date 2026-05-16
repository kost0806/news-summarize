---
title:  "[2026-05-16 / Top 10] Tailwind를 떠나며 CSS 구조화 방법을 배우다"
subtitle: "Julia Evans의 Tailwind 탈출기와 바닐라 CSS 구조화 노하우"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-16 12:00:00
source_url: "https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/"
---

> 원본 기사: [https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/](https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/)

> HN 토론: [https://news.ycombinator.com/item?id=48158400](https://news.ycombinator.com/item?id=48158400)

### 개요

개발자이자 인기 블로거인 Julia Evans가 8년간 사용하던 Tailwind CSS를 떠나 시멘틱 HTML과 바닐라 CSS로 마이그레이션한 경험을 공유했습니다. 그녀는 Tailwind가 CSS 구조화의 여러 원칙을 가르쳐 주었고, 이를 토대로 자신만의 CSS 아키텍처를 구축했습니다. 이 마이그레이션은 "정말 재미있고 흥미로운" 경험이었다고 평가합니다.

### 주요 내용

#### Tailwind가 가르쳐 준 것들

Tailwind를 8년간 사용하면서 Julia는 CSS 코드베이스가 관리해야 할 여러 요소들을 자연스럽게 배웠습니다:
- **리셋 스타일시트**: 브라우저 기본 스타일 정규화
- **색상 팔레트**: 일관된 색상 시스템
- **폰트 스케일**: 체계적인 타이포그래피 크기

#### 새로운 CSS 구조화 시스템

Tailwind 없이 구축한 8가지 CSS 아키텍처 요소:

1. **리셋**: Tailwind의 preflight 스타일을 그대로 복사해 사용
2. **컴포넌트**: 각 컴포넌트는 고유한 클래스를 가지며, 한 컴포넌트의 CSS가 다른 컴포넌트를 덮어쓰지 않음. 컴포넌트별 CSS 파일 분리
3. **색상**: `colours.css`에 CSS 변수로 관리
4. **폰트 크기**: Tailwind에서 가져온 변수 사용 (`--size-xs: 0.75rem` 등)
5. **유틸리티 클래스**: 공통 패턴을 위한 재사용 클래스
6. **기본 간격**: 일관된 스페이싱 시스템
7. **반응형 디자인**: 미디어 쿼리 전략
8. **빌드 시스템**: CSS 빌드 파이프라인

#### 마이그레이션의 핵심 인사이트

Tailwind의 유틸리티 클래스 방식이 특정 종류의 CSS 관리 문제를 해결하지만, 모든 CSS 구조화 문제를 해결하지는 않습니다. Tailwind 없이도 그 원칙들을 직접 적용함으로써 더 명확하게 CSS를 이해하고 제어할 수 있게 되었다는 것이 핵심 메시지입니다.

### HN 커뮤니티 반응

점수 389점, 댓글 247개로 이번 Top 10 중 가장 높은 커뮤니티 반응을 얻었습니다. CSS 프레임워크 선택은 개발자들 사이에서 항상 뜨거운 토론 주제입니다. Tailwind 찬성/반대 진영 간의 논쟁, Julia의 접근법에 대한 다양한 평가, BEM이나 CSS Modules 같은 대안적 방법론 제안, 그리고 CSS-in-JS와의 비교 등 폭넓은 토론이 이루어졌을 것입니다. Julia Evans의 높은 인지도도 반응 수에 기여했을 것입니다.

### 시사점

Tailwind의 인기에도 불구하고, 프레임워크에 대한 의존 없이 CSS의 근본 원칙을 이해하는 것이 장기적으로 더 유연한 개발을 가능하게 합니다. Julia의 경험은 도구가 우리에게 좋은 습관을 가르쳐 줄 수 있지만, 그 도구 없이도 동일한 원칙을 적용할 수 있음을 보여줍니다. 웹 개발자라면 특정 프레임워크의 편의성에 안주하기보다 그 이면의 원리를 이해하는 것이 중요합니다.
