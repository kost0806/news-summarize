---
title:  "[2026-05-13 / Top 7] 구글에서의 IDE 역사"
subtitle: "2011년 IDE 혼돈에서 내부 웹 기반 IDE '사이더(Cider)'까지"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-13 11:00:00
source_url: "https://laurent.le-brun.eu/blog/a-history-of-ides-at-google"
---

> 원본 기사: [https://laurent.le-brun.eu/blog/a-history-of-ides-at-google](https://laurent.le-brun.eu/blog/a-history-of-ides-at-google)

> HN 토론: [https://news.ycombinator.com/item?id=48073979](https://news.ycombinator.com/item?id=48073979)

### 구글의 IDE 진화사

2011년부터 2024년까지 구글에서 근무했던 Laurent Le Brun이 구글의 내부 개발 환경 변천사를 정리한 글이다. 구글의 메인 모노레포(google3) 개발에 초점을 맞췄다.

#### 2011년: IDE 혼돈의 시대

당시 구글 엔지니어들은 각자 선호하는 IDE를 자유롭게 사용했다. Vim, Emacs, Eclipse, IntelliJ 등 다양한 도구가 혼용됐다. 2011년 구글 시니어 엔지니어들에게 "모든 구글러가 통일된 IDE를 쓸 수 있는 방법이 있을까?"라고 물었을 때 답은 사실상 "없다"였다.

#### 사이더(Cider)의 탄생

2016년경, 일부 팀이 **Cider**라는 웹 기반 편집기를 만들기 시작했다. "Cloud IDE"의 약자에 "r"을 붙여 더 기억하기 좋게 만든 이름이다.

Cider의 핵심 설계 원칙:
- **라이트 클라이언트**: 브라우저에서 실행되며 기존 IDE보다 훨씬 빠르게 시작됨
- **백엔드 집중 처리**: 코드 인덱싱, 자동완성, 분석 등 무거운 작업은 전체 코드베이스를 인덱싱하는 백엔드 서버에서 처리
- **모노레포 최적화**: google3라는 수십억 줄 규모의 모노레포에 특화됨

#### 주요 이점

- 코드베이스 전체에 대한 정확한 코드 탐색 (Find Definition, Find References)
- 어떤 컴퓨터에서든 동일한 개발 환경
- 즉각적인 도구 업데이트 (모든 엔지니어가 동시에 최신 버전 사용)

#### HN 커뮤니티 반응

구글 전·현직 엔지니어들이 활발히 댓글을 달았다. "Cider는 처음엔 투박했지만 결국 놀랍도록 강력해졌다"는 평가와 함께, 모노레포 규모에서 IDE를 만드는 것이 얼마나 어려운 일인지에 대한 기술적 토론이 이어졌다. Google의 개발 문화와 내부 도구에 대한 희귀한 내부자 관점으로 주목받았다.
