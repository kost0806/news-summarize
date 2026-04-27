---
title:  "[2026-04-27 / Top 2] 아사히 리눅스 7.0 진행 보고서"
subtitle: "M3 알파 지원, VRR 디스플레이, 전력 관리 개선 등 Apple Silicon Linux의 새 이정표"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-27 02:00:00
source_url: "https://asahilinux.org/2026/04/progress-report-7-0/"
---

> 원본 기사: [https://asahilinux.org/2026/04/progress-report-7-0/](https://asahilinux.org/2026/04/progress-report-7-0/)

### 개요

아사히 리눅스(Asahi Linux) 팀이 Linux 7.0을 기반으로 한 최신 진행 보고서를 공개했습니다. Apple Silicon Mac에서 Linux를 구동하기 위한 이 프로젝트는 M3 하드웨어 지원 진입, VRR 디스플레이, 전력 관리 개선 등 여러 주요 이정표를 달성했습니다.

### 주요 내용

- **M3 하드웨어 지원 (알파 단계)**: PCIe, MacBook 키보드·트랙패드, SMC 기반 실시간 클럭·재부팅 컨트롤러, NVMe 스토리지 컨트롤러 등 M3 기기용 패치가 아사히 커널 트리에 통합되었습니다. 현재 수준은 M1 초기 알파와 비슷하며, GPU 가속은 아직 미지원입니다.
- **VRR (가변 주사율) 지원**: Apple DCP 펌웨어가 VRR을 활성화하는 방법을 파악하고, 외부 VRR 디스플레이와 MacBook Pro ProMotion 패널에서 테스트를 완료했습니다. 커널 모듈 옵션으로 VRR 강제 활성화를 제공할 계획입니다.
- **전력 관리 개선**: Pro, Max, Ultra급 Apple Silicon 시스템의 전력 관리 프로세서(PMP)용 새 드라이버가 추가되어 14인치 M1 Pro MacBook Pro 기준 대기 전력이 약 0.5W(약 20%) 감소했습니다.
- **오디오 지원 확장**: CS42L84 헤드폰 잭이 44.1, 88.2, 176.4, 192kHz 추가 샘플레이트를 지원합니다.
- **인스톨러 업데이트**: v0.8.0은 m1n1 stage 1 바이너리를 1.5.2로 업그레이드하고, Mac Pro 설치 지원과 펌웨어 업데이트 모드를 추가했습니다.

### 시사점

아사히 리눅스는 Apple의 폐쇄적인 하드웨어에서 완전한 Linux 경험을 제공하기 위해 꾸준히 역엔지니어링을 진행 중입니다. M3 지원이 알파 단계에 접어들면서, Apple Silicon Mac에서 Linux를 사용하고자 하는 개발자와 연구자들에게 점점 더 실용적인 옵션이 되고 있습니다.
