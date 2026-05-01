---
title:  "[2026-05-01 / Top 10] 합성과 블렌딩 — 블렌드 모드의 수학과 직관 탐구"
subtitle: "Porter-Duff 알파 합성 모델로 이해하는 Multiply, Screen 등 블렌드 모드의 원리"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-01 12:09:00
source_url: "https://nik.digital/posts/compositing-blending"
---

> 원본 기사: [https://nik.digital/posts/compositing-blending](https://nik.digital/posts/compositing-blending)

### 합성과 블렌딩: 수학으로 이해하는 블렌드 모드

Niklas Gadermann이 작성한 이 글은 디지털 그래픽스에서 **합성(compositing)**과 **블렌딩(blending)**의 수학적 원리와 직관을 탐구합니다.

#### Porter-Duff 알파 합성 모델

**Porter-Duff 알파 합성 모델**을 기반으로, 두 레이어가 겹치는 영역에서 픽셀이 어떻게 혼합되는지를 수학적으로 설명합니다.

- 블렌딩 단계는 합성 이전에 먼저 수행됨
- 소스(source)와 배경(backdrop)이 **겹치는 영역에서만** 적용됨
- 블렌딩으로 교체된 색상이 합성 단계의 입력값으로 사용됨

#### 주요 블렌드 모드의 수학

**Multiply 모드**
두 채널 값을 서로 곱하여 **어두운 결과**를 만듭니다.
```
결과 = 소스 × 배경
```
두 값 모두 0~1 범위이므로 결과는 항상 더 어두워집니다.

**Screen 모드**
값을 반전한 뒤 곱하고 다시 반전하여 **밝은 결과**를 생성합니다.
```
결과 = 1 - (1 - 소스) × (1 - 배경)
```
Multiply의 반대 효과로, 결과는 항상 더 밝아집니다.

#### 단일 픽셀 시각화의 힘

단일 픽셀의 채널별 동작을 시각화하면 이미지 전체에서 블렌드 모드가 어떻게 작동할지를 폭넓게 예측할 수 있습니다. 블렌드 모드별 수식의 그래프를 보면 각 모드의 특성(밝기 강조, 어둠 강조, 대비 강화 등)을 직관적으로 이해할 수 있습니다.

#### 실용적 구현

Canvas API의 `globalCompositeOperation` 속성을 통해 웹에서도 다양한 합성 모드를 구현할 수 있습니다. 블렌드 모드의 직관을 구축하기 어렵지만, 수학적 접근으로 이를 체계화한 이 글은 그래픽스 프로그래밍을 이해하고자 하는 개발자에게 훌륭한 출발점이 됩니다.
