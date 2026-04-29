---
title:  "[2026-04-29 / Top 8] GitHub 가용성 업데이트"
subtitle: "머지 큐 커밋 오염, 검색 서비스 다운 등 4월 장애 두 건에 대한 공식 설명"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-29 12:07:00
source_url: "https://github.blog/news-insights/company-news/an-update-on-github-availability/"
---

> 원본 기사: [https://github.blog/news-insights/company-news/an-update-on-github-availability/](https://github.blog/news-insights/company-news/an-update-on-github-availability/)

### 요약

GitHub가 2026년 4월에 발생한 두 건의 주요 장애에 대한 공식 업데이트를 게시했습니다. 머지 큐(Merge Queue) 커밋 오염 문제와 Elasticsearch 검색 다운 사고에 대해 원인과 영향을 설명하고, 향후 인프라 확장 계획도 밝혔습니다.

---

### 사고 1: 머지 큐 커밋 오염 (4월 23일)

**무슨 일이 있었나?**
머지 큐의 squash merge 방식에서 회귀(regression)가 발생했습니다. 두 개 이상의 PR이 동일한 머지 그룹에 포함될 경우, 이전에 병합된 PR의 변경사항이 이후 머지에 의해 **실수로 되돌려지는(reverted)** 문제가 생겼습니다.

**영향 범위:**
- 영향을 받은 저장소: **658개**
- 영향을 받은 PR: **2,092건**

*(GitHub의 초기 발표 수치가 다소 높았던 것은 첫 평가를 보수적으로 잡았기 때문이라고 설명)*

---

### 사고 2: Elasticsearch 검색 서비스 다운 (4월 27일)

GitHub 검색을 지원하는 Elasticsearch 클러스터가 과부하 상태에 빠졌습니다. 원인은 **봇넷 공격**으로 추정되며, 클러스터가 응답 불능이 되어 GitHub 내 검색 기반 기능들이 일시 중단됐습니다.

---

### GitHub 인프라의 현재 상황

**급격한 성장 압력:**
- 2025년 12월 하반기부터 **에이전틱(agentic) 개발 워크플로우**가 급격히 증가
- 저장소 생성, PR 활동, API 사용량, 자동화, 대형 저장소 작업 부하 모두 빠르게 증가

**확장 계획:**
- 2025년 10월, 현재 대비 **10배 용량 확장** 계획 시작
- 그러나 2026년 2월, **30배** 규모의 확장이 필요하다는 판단으로 계획 수정

---

### 시사점

이번 사고는 개발자 도구인 GitHub 자체의 신뢰성 문제를 다시 수면 위로 올렸습니다. 특히 AI 코딩 에이전트의 폭발적인 증가로 GitHub 인프라에 전례 없는 부하가 가해지고 있으며, 이에 대한 충분한 대비가 필요한 상황입니다.
