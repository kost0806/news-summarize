---
title:  "[2026-05-16 / Top 4] Kioxia와 Dell, 2U 서버에 10PB 올플래시 스토리지 구현"
subtitle: "2U 슬림 서버에 10PB 올플래시, 랙 하나에 196PB 가능"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/posts/2026-05-16-hn-top4-kioxia-and-dell-cram-10-pb-into-slim-2ru-server.jpg"
date:   2026-05-16 12:00:00
source_url: "https://www.blocksandfiles.com/flash/2026/05/14/kioxia-and-dell-cram-10-pb-into-slim-2ru-server/5240574"
---

> 원본 기사: [https://www.blocksandfiles.com/flash/2026/05/14/kioxia-and-dell-cram-10-pb-into-slim-2ru-server/5240574](https://www.blocksandfiles.com/flash/2026/05/14/kioxia-and-dell-cram-10-pb-into-slim-2ru-server/5240574)

> HN 토론: [https://news.ycombinator.com/item?id=48161997](https://news.ycombinator.com/item?id=48161997)

### 개요

Kioxia의 LC9 고용량 QLC SSD를 활용하여 Dell이 단 2U(2 Rack Unit) 높이의 서버에 9.8PB에 달하는 올플래시 스토리지를 탑재하는 데 성공했습니다. 245.76TB 용량의 NVMe SSD 40개를 AMD EPYC 9005 기반의 PowerEdge R7725xd 서버에 장착한 결과물로, 단일 랙에 이런 서버 20대를 넣으면 이론상 196PB의 스토리지 용량을 달성할 수 있습니다.

### 주요 내용

#### 핵심 구성 사양

- **SSD**: Kioxia LC9 E3.L 폼팩터 QLC NVMe SSD, 단일 드라이브 245.76TB
- **드라이브 수**: 서버 1대당 40개
- **총 용량**: 약 9.8PB (10PB에 근접)
- **서버**: Dell PowerEdge R7725xd (AMD EPYC 9005 탑재)
- **폼팩터**: 2RU (2 Rack Unit)
- **네트워크**: 최대 5x 400Gbps NIC 지원

#### 랙 밀도의 혁신

이 서버 20대를 단일 랙에 채우면 196PB의 스토리지 용량을 확보할 수 있습니다. 이는 기존 하드 드라이브 기반 스토리지와 비교했을 때 공간 효율성과 성능 모두에서 획기적인 수치입니다. 데이터센터 운영자 입장에서 물리적 공간 비용을 대폭 절감할 수 있는 기회입니다.

#### 경쟁 제품 동향

256TB급 SSD를 개발 중인 업체는 Kioxia 외에도 여럿 있습니다. Micron 6600 ION, Sandisk UltraQLC SN670, SK Hynix AIN D, Solidigm 등이 경쟁하고 있으며, Scality는 Samsung의 미래 근거리 클래스 SSD(용량 로드맵상 1PB)를 지원하기 위한 작업을 진행 중입니다.

### HN 커뮤니티 반응

이 게시물은 점수 101점, 댓글 67개로 비교적 활발한 토론이 이루어졌습니다. 커뮤니티에서는 QLC SSD의 내구성과 쓰기 수명에 대한 우려, 이런 밀도의 스토리지가 실제로 어떤 워크로드에 적합한지(주로 읽기 집약적 콜드 스토리지), 그리고 가격 대비 용량 비교 등이 논의되었을 것입니다. HDD 대비 올플래시의 경제성에 대한 논쟁도 있었을 것으로 보입니다.

### 시사점

QLC 기술의 발전으로 플래시 스토리지의 용량 밀도가 HDD에 근접하거나 일부 구성에서는 앞서기 시작했습니다. 특히 AI 학습 데이터, 미디어 아카이브, 백업 스토리지 등 대용량 데이터를 다루는 기업들에게 이 기술은 데이터센터 설계 패러다임을 바꿀 수 있는 중요한 전환점입니다. 1PB SSD 로드맵까지 이어지는 기술 발전 속도를 주목할 필요가 있습니다.
