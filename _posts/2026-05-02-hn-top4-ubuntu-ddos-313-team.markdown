---
title:  "[2026-05-02 / Top 4] 이란 연계 '313팀', Ubuntu.com DDoS 공격 후 강탈 협박으로 전환"
subtitle: "Ubuntu 26 출시 당일 캐노니컬 인프라에 대한 사이버 공격 — 12시간 넘게 서비스 마비"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-02 12:04:00
source_url: "https://www.theregister.com/2026/05/01/canonical_confirms_ubuntu_infrastructure_under/"
---

> 원본 기사: [https://www.theregister.com/2026/05/01/canonical_confirms_ubuntu_infrastructure_under/](https://www.theregister.com/2026/05/01/canonical_confirms_ubuntu_infrastructure_under/)

### Ubuntu 26 출시일에 기습 당한 캐노니컬

2026년 5월 1일, Ubuntu 26이 출시되는 날 이란과 연계된 핵티비스트 그룹 **313팀(313 Team)**이 캐노니컬의 웹 인프라에 대규모 DDoS 공격을 감행했습니다. 공격은 국경을 초월한 지속적인 분산 서비스 거부(DDoS) 공격으로, 12시간 이상 Ubuntu 관련 서비스를 마비시켰습니다.

#### 313팀이란?

**이슬람 사이버 저항(Islamic Cyber Resistance)**, 일명 **313팀**은 이란 정보보안부(MOIS)와 연계된 것으로 평가되는 이란 친화적 핵티비스트 조직입니다. 이들은 최근 한 달 동안 eBay(일본·미국 지사)와 Bluesky에도 유사한 공격을 감행한 바 있습니다.

#### 피해 범위

공격으로 인해 다음 서비스들이 모두 중단되거나 접근 불가 상태에 빠졌습니다.

- **ubuntu.com** 메인 웹사이트 및 다수 서브도메인
- **Snap 스토어**: 스냅 패키지 다운로드 불가
- **Launchpad**: 버그 트래커·PPA 호스팅 서비스 접근 불가
- **Canonical SSO**: 계정 로그인 차단
- Ubuntu 디스트리뷰션 다운로드 채널 전면 중단

#### 단순 공격에서 강탈로 전환

초기 DDoS 공격 이후, 313팀은 텔레그램 채널을 통해 캐노니컬에 다음과 같은 메시지를 보냈습니다.

> "간단한 해결책이 있습니다. 우리가 이메일로 Session Contact ID를 보냈습니다. 연락하지 않으면 공격을 계속할 것입니다. 최악의 상황에 처해 있으니 어리석게 굴지 마십시오."

보안 기관 VECERT에 따르면 313팀은 공격 종료 대가로 수백만 달러에 달하는 금전적 요구를 포함한 협박 메시지를 캐노니컬 팀에 직접 전달했습니다.

#### 캐노니컬의 공식 입장

캐노니컬 대변인은 "당사의 웹 인프라가 지속적이고 국경을 초월한 DDoS 공격을 받고 있다"고 공식 확인했습니다. Archive 및 Discourse 페이지 등 일부 서비스는 공격 중에도 유지됐습니다.

#### 타이밍의 의도성

보안 전문가들은 Ubuntu 26 출시 당일을 공격 시점으로 선택한 것이 우연이 아니라고 분석합니다. 새 버전 출시일은 다운로드 수요가 극대화되는 시점이므로, 공격의 영향력과 홍보 효과를 극대화하려는 전략적 선택으로 보입니다.
