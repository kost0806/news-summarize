---
title:  "[2026-04-23 / Top 1] 작은 화면을 위한 5x5 픽셀 폰트"
subtitle: "극도로 작은 디스플레이를 위해 설계된 가독성 높은 픽셀 폰트에 대한 심층 분석."
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-23 09:00:00
source_url: "https://maurycyz.com/projects/mcufont/"
---

> 원본 기사: [https://maurycyz.com/projects/mcufont/](https://maurycyz.com/projects/mcufont/)

### 개요
모든 문자가 5 픽셀 정사각형에 맞으며 6x6 그리드에 안전하게 그릴 수 있습니다. 이 설계는 lcamtuf의 5x6 폰트에서 영감을 받았으며, ZX Spectrum의 8x8 폰트에서 유래했습니다.

### 설계 특징
- M, W, N, Q, G, P 같은 더 많은 문자가 가로 세부사항을 가지며, E, F는 세로 세부사항을 가집니다.
- 5x5는 가독성을 타협하지 않는 가장 작은 크기입니다.
- 고정 너비는 프로그래밍을 더 쉽게 만들며, 문자열의 길이는 항상 문자 수의 6배이고 레이아웃을 안전하게 합니다.

### 실제 적용
160x128 또는 128x64 OLED는 실용적이고 저렴하지만 이를 잘 활용하려면 픽셀 효율적인 손글씨 폰트가 필요합니다. 벡터 폰트와 달리 350 바이트의 손으로 제작한 폰트는 더 우수한 성능을 제공합니다.
