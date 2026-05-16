---
title:  "[2026-05-16 / Top 8] Halt and Catch Fire – CPU를 멈추게 만드는 전설의 명령어"
subtitle: "실제로 CPU를 멈추거나 불태웠던 불법 명령어의 역사"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-16 12:00:00
source_url: "https://unstack.io/halt-and-catch-fire"
---

> 원본 기사: [https://unstack.io/halt-and-catch-fire](https://unstack.io/halt-and-catch-fire)

> HN 토론: [https://news.ycombinator.com/item?id=48162468](https://news.ycombinator.com/item?id=48162468)

### 개요

"Halt and Catch Fire(HCF)"는 CPU가 유용한 동작을 멈추게 만드는 기계어 명령어를 가리키는 유머적 표현으로, ADD, CMP, JMP 같은 세 글자 어셈블리 니모닉 형식을 흉내낸 것입니다. 이 글은 Motorola 6800 프로세서의 미문서 불법 명령어와 IBM System/360에서 실제로 CPU를 과열시켜 불을 붙인 명령어의 역사적 사례들을 탐구합니다.

### 주요 내용

#### Motorola 6800의 기이한 불법 명령어

Motorola 6800은 256개의 단일 바이트 명령어 공간 중 59개의 미정의 비트 패턴을 가지고 있었습니다. 그 중 `$9D`와 `$DD` 두 바이트는 일반적인 fetch-decode-execute 사이클을 벗어난 기이한 동작을 보였습니다. 이 명령어들은 프로그램 카운터가 계속 증가하면서 주소 라인이 하드웨어 카운터처럼 메모리를 순회하며 읽기 동작을 반복합니다. 1985년 IEEE Design & Test 논문에서 Daniels와 Bruce는 MC6800의 내부적으로 HACOF로 불리던 불법 명령어를 기술했는데, 이 명령어는 리셋될 때까지 프로그램 카운터를 무한히 증가시킬 수 있었습니다.

#### IBM System/360 – 실제로 불을 붙인 명령어

IBM System/360은 특정 잘못된 명령어를 만나면 자기 코어 메모리의 특정 위치에 지속적으로 접근했습니다. 자기 코어 메모리는 읽기 동작으로 인해 열이 발생하는데, 이 위치에 반복적으로 접근하면 매우 뜨거워져 실제로 불이 붙는 사고가 발생했습니다. 이것이 "Halt and Catch Fire"라는 표현의 실제 물리적 근거입니다.

#### 현대적 의미

HCF는 이제 CPU 설계의 역사적 일화를 넘어, TV 드라마 제목으로도 사용되었고, 소프트웨어 개발에서 예측 불가능한 치명적 오류를 가리키는 은유로도 쓰입니다.

### HN 커뮤니티 반응

점수 54점, 댓글 32개를 기록한 이 게시물은 레트로 컴퓨팅과 하드웨어 역사에 관심 있는 HN 커뮤니티 독자들의 관심을 끌었습니다. 각자가 알고 있는 레거시 CPU의 이상한 불법 명령어 경험담, 자기 코어 메모리 시대의 하드웨어 특성, 그리고 현대 CPU에서 유사한 취약점이 존재하는지 등에 대한 토론이 이루어졌을 것입니다.

### 시사점

컴퓨터 하드웨어의 초창기에는 미문서 동작과 하드웨어 버그가 예상치 못한 결과를 초래했습니다. 현대의 CPU와 소프트웨어 개발에서도 정의되지 않은 동작(undefined behavior)은 여전히 보안 취약점과 예측 불가능한 버그의 원인이 됩니다. 이런 역사적 사례들은 하드웨어와 소프트웨어 모두에서 명세의 완전성과 경계 조건 처리의 중요성을 상기시켜 줍니다.
