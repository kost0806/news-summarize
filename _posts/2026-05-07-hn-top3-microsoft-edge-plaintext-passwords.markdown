---
title:  "[2026-05-07 / Top 3] Microsoft Edge, 저장된 비밀번호를 시작 시 평문으로 메모리에 올린다"
subtitle: "보안 연구원이 발견한 Edge의 설계 결함, Microsoft는 '의도된 동작'이라 해명"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-07 03:00:00
source_url: "https://www.computerworld.com/article/4167430/edge-browser-leaves-passwords-exposed-in-plain-text-says-researcher.html"
---

> 원본 기사: [https://www.computerworld.com/article/4167430/edge-browser-leaves-passwords-exposed-in-plain-text-says-researcher.html](https://www.computerworld.com/article/4167430/edge-browser-leaves-passwords-exposed-in-plain-text-says-researcher.html)

### 개요

보안 연구원 Tom Jøran Sønstebyseter Rønning이 Microsoft Edge가 브라우저 시작 시 저장된 **모든 비밀번호를 평문(cleartext)으로 프로세스 메모리에 로드**하고, 세션 내내 유지한다는 사실을 발견했다. 다른 Chromium 기반 브라우저(Chrome 등)는 필요할 때만 비밀번호를 복호화하는 반면, Edge는 처음부터 전부 올려놓는 방식이다. Microsoft는 이를 "의도된 동작"이라 답변했다.

### 주요 내용

- **발견 내용**: Edge는 시작과 동시에 비밀번호 관리자에 저장된 모든 자격증명을 메모리에 평문으로 로드한다. 세션이 끝날 때까지 암호화 없이 메모리에 상주한다.
- **Chrome과의 차이**: Chrome은 사용자가 비밀번호를 요청할 때만 복호화하며, Application-Bound Encryption 등 추가 방어 레이어를 사용한다. 연구원은 "이 동작을 보이는 유일한 Chromium 기반 브라우저"라고 밝혔다.
- **위험 시나리오**: 터미널 서버 등 공유 컴퓨팅 환경에서 관리자 권한을 가진 공격자가 실행 중인 Edge 프로세스의 메모리를 읽어 다른 사용자의 비밀번호를 취득할 수 있다. PoC(개념 증명 코드)도 공개됐다.
- **Microsoft의 반응**: "보고된 시나리오에서 브라우저 데이터 접근은 이미 기기가 침해된 상황을 전제로 한다"는 입장으로 취약점으로 인정하지 않았다.
- **보도**: Computerworld, CSO Online, PC World, Windows Central, Cybernews, Dark Reading, Proton 등이 일제히 보도했다.

### 시사점

"이미 기기가 침해됐다면 어차피 끝"이라는 Microsoft의 논리는 보안 커뮤니티에서 강한 비판을 받고 있다. 최소 권한 원칙(principle of least privilege)과 깊은 방어 전략(defense-in-depth)의 관점에서, 불필요하게 민감 데이터를 메모리에 평문으로 노출하는 것은 명백한 보안 위험이다. 기업 환경에서 Edge를 기본 브라우저로 사용하는 조직은 이 문제를 주시해야 한다.
