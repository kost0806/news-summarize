---
title:  "[2026-04-26 / Top 2] Firefox, Brave의 광고 차단 엔진 통합"
subtitle: "Mozilla가 Brave의 Rust 기반 adblock-rust 엔진을 Firefox 149에 조용히 탑재"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-26 02:00:00
source_url: "https://itsfoss.com/news/firefox-ships-brave-adblock-engine/"
---

> 원본 기사: [https://itsfoss.com/news/firefox-ships-brave-adblock-engine/](https://itsfoss.com/news/firefox-ships-brave-adblock-engine/)

### 개요

Mozilla Firefox가 Brave의 오픈소스 Rust 기반 광고 차단 엔진인 `adblock-rust`를 Firefox 149에 별도 공지 없이 통합했습니다. 릴리즈 노트에도 언급되지 않은 이 변화는 Bugzilla Bug 2013888을 통해 조용히 추가되었으며, 현재는 기본적으로 비활성화 상태이고 UI나 기본 필터 목록도 포함되어 있지 않습니다.

### 주요 내용

- **엔진 정보**: `adblock-rust`는 Brave가 개발한 Rust 기반 광고·트래커 차단 라이브러리로, MPL-2.0 라이선스 하에 공개되어 있습니다. 네트워크 요청 차단, 코스메틱 필터링, uBlock Origin 호환 필터 목록 구문을 지원합니다.
- **현재 상태**: 기본적으로 비활성화되어 있으며, Firefox 149 이상에서 `about:config`를 통해 수동으로 활성화할 수 있습니다. 사용자 인터페이스나 기본 필터 목록은 아직 포함되지 않았습니다.
- **파급 효과**: Firefox 포크인 Waterfox가 이미 Mozilla의 구현을 기반으로 `adblock-rust`를 채택했습니다.
- **담당자**: Mozilla 엔지니어 Benjamin VanderSloot가 "프로토타입 리치 콘텐츠 차단 엔진 추가"라는 이름으로 해당 버그를 작성하고 처리했습니다.

### 시사점

이 변화는 Mozilla가 Firefox의 기본 광고 차단 기능을 네이티브로 강화할 준비를 하고 있다는 신호로 해석됩니다. 구글의 Manifest V3 정책으로 크롬 기반 브라우저의 확장 차단 기능이 약화되는 시점에, Firefox가 내장 광고 차단으로 차별화 포인트를 강화하려는 전략적 움직임일 수 있습니다. 향후 정식 활성화 시점과 UI 구현이 주목됩니다.
