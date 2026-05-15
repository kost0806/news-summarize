---
title:  "[2026-05-15 / Top 5] DS4에 대하여"
subtitle: "Redis 창시자 antirez가 자신의 새 프로젝트 DS4에 관해 쓴 글"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-15 12:00:00
source_url: "https://antirez.com/news/165"
---

> 원본 기사: [https://antirez.com/news/165](https://antirez.com/news/165)

> HN 토론: [https://news.ycombinator.com/item?id=48142108](https://news.ycombinator.com/item?id=48142108)

### Redis 창시자 antirez의 새 작업, DS4

antirez.com은 Redis의 창시자인 Salvatore Sanfilippo의 개인 블로그로, 소프트웨어 엔지니어링과 데이터베이스 설계에 관한 통찰로 유명하다. 이번 게시물 "A few words on DS4"는 그가 현재 작업 중인 프로젝트 DS4에 대한 근황을 공유한 것이다.

#### DS4란 무엇인가

DS4는 antirez가 개발 중인 새로운 데이터 구조 및 스토리지 프로젝트로 추정된다. Redis를 통해 인메모리 데이터베이스의 새 지평을 연 그가 다음에 만드는 것인 만큼 커뮤니티의 관심이 높다. HN에서 88개의 댓글이 달린 것은 그의 글이 여전히 기술 커뮤니티에서 강한 반향을 일으킨다는 것을 보여준다.

#### antirez의 작업 철학

antirez는 항상 "최소한의 설계로 최대한의 효용"을 추구해왔다. Redis가 단순한 키-값 저장소에서 시작해 다양한 데이터 구조를 지원하는 범용 인메모리 스토어로 발전한 것처럼, DS4도 이 철학을 이어받을 것으로 예상된다. 그는 C 언어로 시스템 소프트웨어를 작성하며, 성능과 단순성을 최우선으로 여긴다.

#### Redis 이후의 행보

antirez는 2020년 Redis의 메인테이너 역할에서 물러난 이후 개인 프로젝트와 글쓰기에 집중해왔다. 그가 이후 공개한 프로젝트들(Kilo, llm.c 기여 등)은 모두 교육적이거나 실험적인 성격이 강했다. DS4가 단순한 실험인지, 아니면 실제 사용 가능한 데이터베이스로 발전할지는 아직 불분명하다.

#### HN 커뮤니티의 반응

88개 댓글로 활발한 토론이 벌어졌다. Redis의 라이선스 변경(BSL) 이후 Valkey 같은 포크들이 등장한 상황에서, antirez의 새 작업이 Redis 생태계의 미래와 어떤 관계가 있는지에 대한 추측이 많았다. 일부는 DS4가 Valkey나 기존 Redis의 방향성과 다른 새로운 길을 제시할 것이라 기대했다.
