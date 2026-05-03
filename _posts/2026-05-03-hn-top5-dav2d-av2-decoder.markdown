---
title:  "[2026-05-03 / Top 5] Dav2d"
subtitle: "VideoLAN, AV2 코덱의 오픈소스 CPU 디코더 dav2d 초기 프리뷰 버전 공개"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-03 12:04:00
source_url: "https://code.videolan.org/videolan/dav2d"
---

> 원본 기사: [https://code.videolan.org/videolan/dav2d](https://code.videolan.org/videolan/dav2d)

### AV1의 후계자 AV2를 위한 오픈소스 디코더

**VideoLAN** 개발팀이 차세대 비디오 코덱 **AV2**를 위한 오픈소스 CPU 디코더 **dav2d 0.0.1 "Merbanan"**을 공개했습니다. AV1 디코더 **dav1d**의 후속 프로젝트로, 아직 초기 프리뷰 단계입니다.

#### dav2d란?

- **AV2(AOMedia Video 2)** 코덱의 소프트웨어(CPU) 디코더
- 기존의 널리 사용되는 AV1 디코더 **dav1d**를 기반으로 개발
- 크로스 플랫폼 지원을 목표로 설계
- 정확성(correctness)을 최우선으로 하면서도 속도 최적화를 추구

#### 현재 상태

AV2 코덱 자체가 아직 표준화 과정 중에 있기 때문에 dav2d 역시 초기 구현 단계입니다. 개발팀이 현재 집중하고 있는 작업은 다음과 같습니다.

- C 언어 구현 완성
- 사용 가능한 API 제공
- 주요 플랫폼 포팅
- 아키텍처별 최적화(SIMD 등)

#### 배경: dav1d의 성공

dav2d의 전신인 **dav1d**는 현재 Firefox, VLC, Chrome 등 주요 플레이어에 내장된 가장 빠른 AV1 소프트웨어 디코더로 자리 잡았습니다. VideoLAN은 dav1d에서 쌓은 노하우를 바탕으로 AV2 시대를 선점하려 하고 있습니다.

#### 의의

AV2는 AV1보다 약 30% 향상된 압축 효율을 목표로 개발 중인 차세대 오픈 비디오 코덱입니다. 오픈소스 디코더의 조기 개발은 코덱 표준이 완성된 후 빠른 생태계 확산을 가능하게 합니다. Hacker News 커뮤니티에서는 dav1d의 성공 사례를 언급하며 dav2d에 대한 기대감을 표명하는 반응이 많았습니다.
