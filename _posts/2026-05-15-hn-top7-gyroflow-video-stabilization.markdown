---
title:  "[2026-05-15 / Top 7] Gyroflow: 자이로스코프 데이터를 활용한 동영상 손떨림 보정"
subtitle: "GoPro·DJI·Sony 등 액션캠의 자이로 데이터로 전문가급 영상 안정화를 구현하는 오픈소스 도구"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-15 12:00:00
source_url: "https://github.com/gyroflow/gyroflow"
---

> 원본 기사: [https://github.com/gyroflow/gyroflow](https://github.com/gyroflow/gyroflow)

> HN 토론: [https://news.ycombinator.com/item?id=48107766](https://news.ycombinator.com/item?id=48107766)

### Gyroflow: 오픈소스 동영상 손떨림 보정 프로젝트

Gyroflow는 카메라에 내장된 자이로스코프와 가속도계 데이터를 이용해 동영상의 손떨림을 정밀하게 보정하는 오픈소스 도구다. GitHub에서 8,700개 이상의 스타를 받은 이 프로젝트는 GoPro, DJI, Sony, Insta360 등 주요 액션 카메라를 광범위하게 지원한다.

#### 핵심 작동 원리

일반적인 소프트웨어 기반 손떨림 보정은 영상을 분석해 움직임 벡터를 추출하지만, Gyroflow는 카메라가 기록한 실제 움직임 데이터(자이로스코프/IMU 데이터)를 직접 활용한다. 이 방식은 훨씬 더 정밀하고 안정적인 결과를 낸다. 특히 고속 움직임이 많은 드론 FPV 영상이나 익스트림 스포츠 촬영에서 기존 방식보다 월등히 나은 성능을 발휘한다.

#### 주요 기능

- **롤링 셔터 보정**: CMOS 센서의 고유한 왜곡 현상을 정밀하게 보정
- **수평 보정**: 촬영 중 기울어진 화면을 자동으로 수평으로 맞춤
- **GPU 가속 처리**: DirectX, OpenGL, Metal, Vulkan을 통한 고속 렌더링
- **광학 교정 지원**: 어안렌즈 등 다양한 렌즈 왜곡 자동 보정
- **전문 NLE 플러그인**: Adobe Premiere Pro, DaVinci Resolve, Final Cut Pro 통합
- **10비트 HDR 지원**: ProRes, H.265, OpenEXR 등 다양한 고품질 포맷 처리

#### 기술 스택

Rust(66.8%)와 QML UI(22.9%)를 주력 언어로 사용하며, 그래픽 처리에는 Qt와 wgpu를 활용한다. OpenCV는 최소한으로 사용하며, CPU 폴백도 지원한다. Windows, macOS, Linux는 물론 Android와 iOS도 지원하는 크로스플랫폼 도구다.

#### 지원 카메라 및 기기

30개 이상의 카메라 모델을 공식 지원한다. GoPro Hero 시리즈, DJI 드론, Sony FX/A 시리즈, Insta360, BlackMagic, Runcam 등이 포함되며, 외부 IMU 로거나 FC(Flight Controller) 로그도 사용할 수 있다.

#### 라이선스 및 커뮤니티

GPLv3 라이선스로 배포되며, App Store 예외 조항이 포함되어 있다. 421개의 포크가 있을 만큼 활발한 커뮤니티를 보유하고 있다. HN에서 이 프로젝트가 재조명된 것은 최근 액션 카메라와 드론 영상 제작에 대한 관심 증가와 맞물린 것으로 보인다.
