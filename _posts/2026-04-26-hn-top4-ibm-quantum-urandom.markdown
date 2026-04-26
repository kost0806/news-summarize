---
title:  "[2026-04-26 / Top 4] IBM 양자 컴퓨터 백엔드를 /dev/urandom으로 대체하기"
subtitle: "Q-Day Prize 수상 양자 암호 풀기 코드, 실제 양자 하드웨어 없이도 동일하게 동작"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-26 04:00:00
source_url: "https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md"
---

> 원본 기사: [https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md](https://github.com/yuvadm/quantumslop/blob/25ad2e76ae58baa96f6219742459407db9dd17f5/URANDOM_DEMO.md)

### 개요

IBM 양자 컴퓨터를 이용해 타원 곡선 이산 로그 문제(ECDLP)를 풀었다고 주장하며 1 BTC 상금을 수상한 Q-Day Prize 제출 코드에서, IBM Quantum 백엔드를 단 29줄을 변경해 `/dev/urandom`(무작위 바이트 생성기)으로 대체해도 동일한 결과가 나온다는 것이 증명되었습니다. 이는 해당 코드가 실제 양자 연산이 아닌 고전적 검증 로직에 의존하고 있음을 보여줍니다.

### 주요 내용

- **핵심 발견**: `-29 / +30줄`의 외과적 패치로 IBM Quantum 백엔드를 `os.urandom`으로 교체한 결과, 4비트부터 17비트까지의 모든 도전 과제에서 원 작성자가 보고한 것과 동일한 개인 키를 복원했습니다.
- **수학적 설명**: ECDLP에서 `n`개의 가능한 키가 있을 때, `S`번의 무작위 시도만으로도 충분히 높은 확률로 정답을 찾을 수 있습니다. 특히 4~10비트 도전 과제는 `shots/n` 비율이 1.9~1,170배로, 작성자 자신의 README도 "무작위 노이즈만으로도 높은 확률로 `d`를 복원할 수 있다"고 명시하고 있습니다.
- **17비트 플래그십 결과**: 상금 1 BTC를 받은 17비트 도전에서 `/dev/urandom`이 5번 중 2번 성공(40%)했으며, 이론적 성공 확률은 26.43%입니다.
- **결론**: 양자 회로 설계(ripple-carry 오라클, CDKM 가산기 등)는 기술적으로 진지하지만, "양자 컴퓨터가 ECDLP를 풀었다"는 암호학적 주장은 성립하지 않습니다.

### 시사점

이 사례는 양자 컴퓨팅 주장의 재현성 검증이 얼마나 중요한지를 보여줍니다. 화려한 양자 회로 구현 뒤에서도 실제 양자 우위(Quantum Advantage)가 없을 수 있으며, 무작위 샘플링과 고전적 검증만으로 동일한 결과를 낼 수 있습니다. 양자 컴퓨팅 연구에서 클래식 베이스라인과의 엄밀한 비교 검증이 필수임을 시사합니다.
