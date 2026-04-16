---
title:  "60년 된 DRAM 설계 결함을 우회하다 — Tailslayer"
subtitle: "구글 리서처 LaurieWired, 1966년부터 이어온 DRAM 리프레시 지연을 최대 93% 줄이는 Tailslayer 공개"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-16 09:20:00
source_url: "https://github.com/LaurieWired/tailslayer"
---

> 원본 기사: [https://github.com/LaurieWired/tailslayer](https://github.com/LaurieWired/tailslayer)

> 관련 보도: [Tom's Hardware](https://www.tomshardware.com/software/ambitious-hacker-reduces-worst-case-memory-latency-by-up-to-93-percent-but-with-severe-downsides-1960s-bottleneck-overcome-by-hedging-memory-accesses-to-avoid-running-into-dram-refresh-stalls)

### 개요

구글 엔지니어이자 보안 연구자인 **LaurieWired**가 1966년 Robert Dennard 박사가 설계한 이후 60년 동안 이어온 DRAM의 구조적 문제를 우회하는 라이브러리 **Tailslayer**를 공개했습니다. Intel, AMD, Graviton 등 주요 x86/ARM 플랫폼에서 DDR4/DDR5 기반으로 **최악 케이스(p99.99) 읽기 지연을 최대 93% 감소**시킵니다.

### DRAM의 60년 된 설계 문제

현대 DRAM은 **1T1C (트랜지스터 1개 + 커패시터 1개)** 구조를 기반으로 합니다. 커패시터는 본질적으로 누전이 심해 저장된 전하가 지속적으로 방전되므로, DRAM은 수십 마이크로초마다 **리프레시(refresh)** 를 통해 전하를 재충전해야 합니다.

문제는 리프레시가 메모리 접근과 **비동기적으로** 일어난다는 점입니다. 시스템이 특정 메모리 주소에 접근을 시도하는 순간 마침 해당 행이 리프레시 중이라면, 요청은 리프레시가 완료될 때까지 스톨(stall)됩니다. 이것이 곧 "꼬리 지연(tail latency)" — 통상적인 지연보다 훨씬 긴 최악 케이스 지연 — 의 원인입니다.

### Tailslayer의 해법: 헤지드 읽기(Hedged Read)

Tailslayer는 **헤지(hedge) 전략**으로 이 문제를 우회합니다.

1. **쓰기 시**: 데이터를 여러 독립 DRAM 채널의 복수 주소에 중복 기록합니다.
2. **읽기 시**: 모든 복사본에 동시에 읽기 명령을 전송하고, 가장 먼저 응답하는 데이터를 사용합니다.

이렇게 하면 한 채널의 행이 리프레시 중이더라도 다른 채널에서 데이터를 즉시 읽을 수 있습니다. 복수의 채널이 동시에 리프레시되지 않는 한 스톨이 발생하지 않습니다.

### 성능 결과

| 지표 | 개선폭 |
|------|--------|
| p99.99 꼬리 지연 감소 | 최대 **93%** |
| 일반 지연 개선 | 약 **15배** 감소 (일부 구성) |
| 지원 환경 | Intel · AMD · Graviton / DDR4 · DDR5 / x86 · ARM |

LaurieWired는 **(문서화되지 않은) 채널 스크램블링 오프셋**을 활용해 독립 채널 간 주소 매핑을 파악했습니다.

### 단점

Tom's Hardware 보도에 따르면 이 접근법은 상당한 부작용도 존재합니다.

- **메모리 대역폭 소비 증가**: 각 쓰기에 대해 복수 채널에 데이터를 복제하므로 실효 쓰기 대역폭이 감소합니다.
- **추가 메모리 용량 필요**: 복제된 데이터만큼 저장 공간이 더 필요합니다.
- **미문서화 하드웨어 동작 의존**: 채널 스크램블링 오프셋이 공식 스펙에 없으므로 하드웨어/펌웨어 업데이트 시 동작이 달라질 수 있습니다.

### HN 반응

Hacker News에서 이 포스트는 하드웨어 아키텍처에 관심 있는 개발자들 사이에서 큰 반향을 일으켰습니다. Hackaday는 "DRAM에 'refresh'가 필요하다는 것은 결함이 아닌 설계 선택"이라며 제목의 과장을 지적했지만, 꼬리 지연 문제 자체와 헤지 기법의 참신함은 높이 평가했습니다. 소스 코드는 GitHub의 [LaurieWired/tailslayer](https://github.com/LaurieWired/tailslayer)에서 확인할 수 있습니다.
