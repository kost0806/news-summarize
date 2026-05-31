---
title:  "[2026-05-31 / Top 6] 폭스바겐, Home Assistant를 클라이언트 인증 요구로 차단"
subtitle: "VW의 새로운 OAuth 요구사항이 오픈소스 커넥티드카 통합을 모두 무력화"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-31 12:00:00
source_url: "https://github.com/robinostlund/homeassistant-volkswagencarnet/issues/967"
---

> 원본 기사: [https://github.com/robinostlund/homeassistant-volkswagencarnet/issues/967](https://github.com/robinostlund/homeassistant-volkswagencarnet/issues/967)

> HN 토론: [https://news.ycombinator.com/item?id=48319509](https://news.ycombinator.com/item?id=48319509)

### 개요

2026년 5월 27일, 폭스바겐이 연결 서비스 API를 조용히 변경하면서 수천 개의 홈 오토메이션 설정이 하룻밤 새 작동을 멈췄습니다. 폭스바겐은 이제 API 요청에 "클라이언트 어서션(client assertion)"을 요구합니다. 이는 공식 VW 앱에서만 발급 가능한 암호화 증명으로, Home Assistant와 오픈소스 EV 충전 컨트롤러 evcc가 즉각 차단됐습니다. HN에서 375점, 181개의 댓글을 기록했습니다.

### 주요 내용

#### 클라이언트 어서션이란

새로운 토큰 엔드포인트는 각 요청이 Google Play 또는 Apple App Store의 공식 VW 그룹 앱에서 발생했음을 암호화적으로 증명하는 어서션을 요구합니다. 기존에 사용자 자격증명만으로 인증하던 커뮤니티 클라이언트들은 이 키를 절대 얻을 수 없습니다. VW 그룹과의 공식 파트너십 계약을 맺지 않는 한 불가능합니다.

#### 피해 범위

이번 변경의 영향을 받는 브랜드는 폭스바겐, 아우디(Audi), 스코다(Škoda), 쿠프라(Cupra)를 포함한 VW 그룹 전체입니다. 영향을 받은 오픈소스 프로젝트는 다음과 같습니다:
- **homeassistant-volkswagencarnet**: Home Assistant용 VW 통합 플러그인
- **evcc**: EV 충전 최적화 오픈소스 컨트롤러

공식 VW 앱과 웹 포털을 통한 접근은 정상 작동하므로, 피해는 서드파티 통합만을 사용하는 사용자에 집중됩니다.

#### EU 데이터 접근법(Data Act)과의 충돌

이 조치는 법적으로도 논란이 됩니다. EU 데이터 접근법(Data Act) 제3조는 2026년 9월 12일부터 사용자가 자신의 데이터에 자유롭게 접근할 권리를 보장합니다. 전문가들은 VW의 이번 API 잠금이 해당 규정에 위배될 가능성이 높다고 분석합니다. 즉, 이 조치는 법적으로 시한부일 수 있습니다.

### HN 커뮤니티 반응

375점, 181개의 댓글로 "오픈소스와 자동차 제조사의 충돌"에 대한 격렬한 토론이 벌어졌습니다. "내 차에서 생성된 데이터인데 왜 내가 마음대로 쓸 수 없냐"는 분노, "결국 서드파티 앱은 언제나 API 변경에 취약하다"는 냉정한 분석, 그리고 EU 데이터법이 어떻게 적용될지에 대한 법적 토론이 이어졌습니다.

### 시사점

커넥티드카 시대에 자동차 제조사들이 자신의 API 생태계를 독점 통제하려는 움직임이 강화되고 있습니다. 이는 스마트홈, EV 충전 최적화, 홈 오토메이션 등 사용자 편의 기능에 직접적인 영향을 미칩니다. EU 데이터법의 시행과 함께 이 갈등이 어떻게 해소될지, 오픈소스 커뮤니티와 자동차 기업 간의 긴장 관계가 주목됩니다.
