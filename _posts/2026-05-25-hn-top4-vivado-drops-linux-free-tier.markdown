---
title:  "[2026-05-25 / Top 4] Vivado 2026.1, 무료 티어에서 Linux 지원을 중단하는 이유는?"
subtitle: "AMD(Xilinx)가 Vivado 무료 Basic 라이선스를 Windows 전용으로 제한, 학생·오픈소스 FPGA 개발자 직격"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-25 12:03:00
source_url: "https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-"
---

> 원본 기사: [https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-](https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-)

> HN 토론: [https://news.ycombinator.com/item?id=48254309](https://news.ycombinator.com/item?id=48254309)

### 개요

AMD(구 Xilinx)가 Vivado 2026.1부터 무료 "Basic" 라이선스 티어를 Windows 전용으로 제한했다. Linux 지원은 연간 약 1,200~1,800달러 수준의 유료 "Core" 티어부터만 제공된다.

### 주요 내용

Vivado는 AMD의 FPGA(필드 프로그래머블 게이트 어레이) 설계를 위한 핵심 EDA(전자 설계 자동화) 도구다. 지금까지는 무료 Basic 라이선스로 Linux에서도 사용할 수 있었기 때문에 학생, 취미 개발자, 오픈소스 FPGA 프로젝트의 필수 도구로 자리잡았다.

**이번 변경의 영향:**
- 학생과 연구자들이 무료로 Linux에서 FPGA 개발을 할 수 없게 됨
- 오픈소스 FPGA 프로젝트(예: OpenXC7 등)의 개발 환경 위협
- AMD 지원 포럼 담당자는 Vivado 2025.2를 계속 사용하라는 제안만 제시

**커뮤니티 반응:**
- 개발자들은 이를 "미끼 후 전환(bait-and-switch)" 전술로 비판
- Slashdot, It's FOSS 등 다수의 미디어에서 비판적 보도
- AMD는 2026년 5월 25일 기준 결정을 번복하지 않음

### 배경

FPGA 개발 도구 시장에서 AMD(Xilinx)의 Vivado와 Intel(Altera)의 Quartus는 사실상 양대 독점을 이루고 있다. 경쟁 대안인 오픈소스 Yosys/nextpnr 체인은 일부 FPGA 패밀리에서만 동작하기 때문에 AMD의 이번 결정은 특히 타격이 크다.

### 시사점

유료 소프트웨어 기업들이 무료 계층으로 개발자 생태계를 유인한 후 기능을 제거하는 패턴이 반복되고 있다. FPGA 개발 커뮤니티는 오픈소스 대안 도구 체인에 대한 투자를 가속화하는 계기가 될 수 있다.
