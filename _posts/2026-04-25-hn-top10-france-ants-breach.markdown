---
title:  "[2026-04-25 / Top 10] 프랑스 신분증 관리 기관, 1,170만 건 데이터 침해 확인"
subtitle: "프랑스 국가 공인 문서 기관(ANTS)이 해킹으로 1,170만 개의 시민 계정이 노출되었음을 공식 확인했습니다"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-25 12:09:00
source_url: "https://techcrunch.com/2026/04/22/france-confirms-data-breach-at-government-agency-that-manages-citizens-ids/"
---

> 원본 기사: [https://techcrunch.com/2026/04/22/france-confirms-data-breach-at-government-agency-that-manages-citizens-ids/](https://techcrunch.com/2026/04/22/france-confirms-data-breach-at-government-agency-that-manages-citizens-ids/)

### 개요

프랑스 내무부 산하 국가 공인 문서 기관 **ANTS(Agence nationale des titres sécurisés)**가 해킹으로 인해 1,170만 개의 시민 계정 정보가 유출되었음을 공식 확인했습니다. ANTS는 운전면허증, 여권, 국가 신분증, 체류 허가증 등 주요 신분 문서를 관리하는 기관입니다.

### 사건 경위

- **4월 15일**: ANTS가 ants.gouv.fr 포털에서 개인 및 법인 계정 데이터 유출 관련 보안 사고 감지
- **4월 16일**: 'breach3d'라는 닉네임의 위협 행위자가 해커 포럼에서 최대 1,900만 건의 기록을 탈취했다고 주장하며 매각 제안
- **4월 24일**: ANTS가 공식 업데이트에서 1,170만 개 계정이 피해를 입었음을 확인

### 유출된 정보

유출된 데이터에는 다음 정보가 포함될 수 있습니다.

- 성명, 생년월일, 출생지
- 집 주소, 이메일, 전화번호
- 계정 메타데이터
- 성별 및 혼인 상태

### 취약점

기술 분석에 따르면 공격자는 ANTS API의 **IDOR(Insecure Direct Object Reference)** 취약점을 악용했습니다. 공격자는 API 요청의 파라미터 하나만 조작하면 다른 사용자의 데이터에 무단 접근할 수 있었습니다. 공격자 스스로 이 취약점을 "정말 어리석은(really stupid)" 결함이라고 묘사했을 정도로 기초적인 보안 결함이었습니다.

### 조치 현황

ANTS는 데이터 보호 기관(CNIL), 파리 공공검찰청, 국가 사이버보안 기관(ANSSI)에 이 사건을 신고하고 협력하고 있습니다. 탈취된 데이터는 현재 매각 시도 중이며 아직 광범위하게 유포되지는 않은 것으로 알려졌습니다.

### 맥락

프랑스는 최근 수년간 공공 기관을 대상으로 한 대규모 사이버 공격이 잇따르고 있습니다. 2026년 2월에는 국가 은행 계좌 데이터베이스(FICOBA)에 대한 무단 접근도 공개된 바 있습니다.
