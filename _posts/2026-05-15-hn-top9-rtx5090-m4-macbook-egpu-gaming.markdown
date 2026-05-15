---
title:  "[2026-05-15 / Top 9] RTX 5090과 M4 MacBook Air: 게임이 가능할까?"
subtitle: "RTX 5090 eGPU를 M4 MacBook Air에 연결해 게이밍 성능을 실험한 결과"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-15 12:00:00
source_url: "https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/"
---

> 원본 기사: [https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/)

> HN 토론: [https://news.ycombinator.com/item?id=48137145](https://news.ycombinator.com/item?id=48137145)

### M4 맥북에 RTX 5090 eGPU를 붙이면 게임이 될까?

이 글은 NVIDIA의 최신 플래그십 GPU인 RTX 5090을 Thunderbolt를 통해 M4 MacBook Air에 외장 GPU(eGPU)로 연결해 게이밍 성능을 측정한 실험기다. 140개의 댓글을 받으며 맥 게이밍과 eGPU에 관심 있는 커뮤니티의 주목을 받았다.

#### 실험의 배경

M4 MacBook Air는 전력 효율이 뛰어난 Apple Silicon을 탑재했지만, 게이밍에서는 전통적인 데스크톱 GPU에 비해 한계가 있다. RTX 5090은 2026년 기준 소비자용 최고 사양 GPU로, 이 조합이 실제로 게이밍에 활용 가능한 성능을 낼 수 있는지가 핵심 질문이다.

#### 기술적 제약

Thunderbolt 4/5는 최대 40~120Gbps의 대역폭을 제공하지만, PCIe x16 슬롯에 비해 GPU와의 데이터 전송에서 병목이 발생한다. 특히 GPU가 처리한 결과를 화면에 출력하는 과정에서 추가 지연이 생긴다. 또한 macOS의 GPU 지원 구조는 NVIDIA GPU에 대해 기본적으로 드라이버를 제공하지 않아, 실제로 NVIDIA GPU를 macOS에서 사용하기 위해서는 가상화(VM) 또는 대안적 방법이 필요하다.

#### 실험 결과와 결론

저자는 다양한 게임과 워크로드에서 RTX 5090 + M4 MacBook Air 조합의 성능을 측정했다. eGPU 연결이 가능한 환경에서는 인상적인 그래픽 성능을 보여줬지만, Thunderbolt 대역폭 제한과 macOS의 NVIDIA 지원 부재가 주요 병목이었다. 저자는 이 조합이 특정 사용 사례에서는 의미 있는 선택이 될 수 있지만, 일반적인 게이밍 목적으로는 여전히 Windows 데스크톱이 더 합리적이라고 결론 내렸다.

#### HN 커뮤니티 토론

140개의 댓글에서는 macOS와 NVIDIA의 역사적 관계, Apple Silicon의 게이밍 생태계 발전 방향, 그리고 eGPU의 실용성에 대한 폭넓은 토론이 이루어졌다. 일부는 이런 실험보다 Windows에서 게임하는 것이 훨씬 나은 경험이라고 주장한 반면, 맥 생태계에 머물면서 최고의 게이밍 성능을 원하는 사용자의 고민을 이해한다는 의견도 있었다.
