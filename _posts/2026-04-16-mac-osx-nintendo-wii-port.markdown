---
title:  "닌텐도 Wii에서 Mac OS X가 돌아간다"
subtitle: "개발자 Bryan Keller, 수년간의 역공학 끝에 Mac OS X 10.0 Cheetah를 Wii에 포팅"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-16 09:10:00
source_url: "https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html"
---

> 원본 기사: [https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html](https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html)

### 개요

개발자 Bryan Keller가 Apple의 첫 번째 Mac OS X 버전인 **10.0 Cheetah**를 닌텐도 Wii에 성공적으로 포팅했습니다. 이 프로젝트는 MacRumors, Boing Boing, AppleInsider 등 주요 기술 매체의 집중 조명을 받았으며 Hacker News에서도 큰 화제를 모았습니다.

### 왜 Wii인가? — 하드웨어 호환성

이 포팅이 가능했던 핵심 이유는 **PowerPC 아키텍처**입니다.

Wii의 CPU는 IBM이 설계한 **Broadway** 칩으로, PowerPC 750CL 계열의 직계 후손입니다. 초기 iMac과 PowerBook을 구동했던 PowerPC 750과 같은 혈통이기 때문에 Keller는 이 작업이 가능할 것이라 직감했습니다.

- **Wii CPU**: Broadway (PowerPC 750CL, IBM 설계)
- **Mac OS X 10.0 Cheetah 지원 CPU**: PowerPC 750CXe (G3 iBook, iMac 탑재)

### 포팅 과정

#### 1. 커스텀 부트로더 (wiiMac) 작성

Keller는 Mac OS X에게 Wii의 컴포넌트 사용법을 알려줄 완전히 새로운 부트로더를 작성했습니다. 부트로더에는 **디바이스 트리(device tree)** — 하드웨어 구성과 동작 방식을 기술하는 데이터 — 가 필요했고, Wii Linux 프로젝트의 디바이스 트리에서 영감을 얻어 이를 부트로더에 하드코딩했습니다.

첫 번째로 실행되는 코드는 **PowerPC 어셈블리 `_start` 루틴**으로, 하드웨어를 재설정하고 Wii 전용 설정과 시리얼 디버깅·영상 출력을 비활성화합니다.

#### 2. OS X 커널 패치 및 재컴파일

Mac OS X 커널 소스 코드를 패치하고 수정된 커널 바이너리를 새로 컴파일했습니다. Wii SD 카드 슬롯에서 부팅할 수 있도록 **커스텀 드라이버**를 직접 작성했습니다.

#### 3. 프레임버퍼 드라이버 및 색상 호환성 해결

Wii의 영상 출력과 OS X가 기대하는 색상 포맷 사이의 비호환성을 해결하기 위해 **프레임버퍼 드라이버**를 새로 작성했습니다.

### 결과

수년간의 역공학, 커널 수정, 커스텀 부트로더 개발 끝에 닌텐도 Wii에서 Mac OS X 10.0 Cheetah가 실제로 부팅되어 GUI가 실행됩니다.

소스 코드와 부트로더는 GitHub의 [bryankeller/wiiMac](https://github.com/bryankeller/wiiMac) 저장소에 공개되어 있어 누구나 자신의 Wii에서 시도해볼 수 있습니다.

### HN 반응

HN 커뮤니티는 "불가능한 것을 실제로 완성하는 집착의 결과물"이라는 평가와 함께 PowerPC 호환성의 흥미로운 역사, G4 iMac 외관의 Wii 개조(iMac G3 모드) 가능성에 대한 상상도 이어졌습니다.
