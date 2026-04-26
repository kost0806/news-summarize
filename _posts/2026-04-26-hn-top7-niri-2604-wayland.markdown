---
title:  "[2026-04-26 / Top 7] Niri 26.04: 스크롤 가능한 타일링 Wayland 컴포지터"
subtitle: "오랫동안 요청된 블러(Blur) 지원과 다양한 개선 사항을 담은 Niri 26.04 출시"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-26 07:00:00
source_url: "https://github.com/niri-wm/niri/releases/tag/v26.04"
---

> 원본 기사: [https://github.com/niri-wm/niri/releases/tag/v26.04](https://github.com/niri-wm/niri/releases/tag/v26.04)

### 개요

스크롤 가능한 타일링(Scrollable-tiling) 방식의 Wayland 컴포지터 Niri가 2026년 4월 25일 버전 26.04를 출시했습니다. 이번 릴리즈의 하이라이트는 GitHub에서 가장 많은 요청을 받아온 기능인 투명 창 블러(Window Blur) 지원이며, 렌더링 아키텍처 리팩터링 등 다양한 개선 사항이 포함되었습니다.

### 주요 내용

- **블러 지원**: "단연코 가장 많이 요청된 Niri 기능"으로, GitHub에서 최다 추천을 받은 이슈였습니다. 이번 릴리즈에서 드디어 투명 창 블러 렌더링이 가능해졌습니다.
- **포인터 기능 개선**: 스크롤 중 포인터 워핑(Pointer Warping) 지원, 창 스크린캐스트에서의 포인터 지원 추가, 기타 스크린캐스트 개선이 포함되었습니다.
- **렌더링 리팩터링**: Pull 기반 이터레이터 렌더링에서 Push 기반 방식으로 아키텍처를 전환하여 성능과 유지 보수성을 개선했습니다.
- **기타 주요 개선**: `ext-foreign-toplevel-list` 프로토콜 지원, 중복 키 바인딩 오류 메시지 개선, 중첩 Niri를 위한 DMA-BUF 지원, ARM Mac에서의 자동 GPU 선택 개선, USB-C 도크 연결 해제 후 스테일 출력 문제 수정 등이 포함됩니다.
- **설정 개선**: 옵셔널 include 지원으로, 파일이 없어도 Niri가 계속 로드될 수 있습니다.

### 시사점

Niri는 기존의 격자 기반 타일링과 달리 창을 좌우로 스크롤하는 독특한 방식을 채택하여 멀티모니터 환경이나 넓은 가상 공간을 직관적으로 탐색하는 데 강점이 있습니다. 블러 지원 추가로 시각적 완성도가 높아지면서, 더 많은 Wayland 사용자들의 주목을 받을 것으로 기대됩니다.
