---
title:  "[2026-04-19 / Top 8] Emacs에 대한 신뢰를 향하여"
subtitle: "Eshel Yaron의 trust-manager 패키지 — Emacs 30의 신뢰 시스템을 실용적으로 만드는 도구"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-19 13:10:00
source_url: "https://eshelyaron.com/posts/2026-04-15-towards-trust-in-emacs.html"
---

> 원본 기사: [https://eshelyaron.com/posts/2026-04-15-towards-trust-in-emacs.html](https://eshelyaron.com/posts/2026-04-15-towards-trust-in-emacs.html)

### 개요

Emacs 기여자 **Eshel Yaron**이 2026년 4월 15일 발표한 "Towards Trust in Emacs" 글이 Hacker News 상위 8위에 올랐습니다. 이 글은 Emacs 30에 도입된 신뢰(trust) 시스템의 필요성과 한계, 그리고 이를 보완하는 **trust-manager** 패키지를 소개합니다.

### Emacs의 보안 문제 배경

Emacs는 강력한 확장성을 자랑하지만, 이 확장성은 보안 취약점의 원천이기도 합니다:

- Emacs Lisp로 작성된 파일은 열 때 자동으로 **코드를 실행**할 수 있음
- 디렉토리 로컬 변수(`.dir-locals.el`), 파일 로컬 변수 등이 임의 코드 실행 벡터
- **CVE-2024-53920**: 이를 악용한 실제 임의 코드 실행 취약점이 발견됨

Emacs 30 이전까지는 모든 파일을 **신뢰된(trusted)** 것으로 간주했습니다. 이는 편의를 위한 설계였지만, 보안 측면에서 큰 구멍이었습니다.

### Emacs 30의 신뢰 시스템

Emacs 30은 파일에 대한 **명시적 신뢰 개념**을 도입했습니다:

- 기본적으로 모든 파일을 **신뢰하지 않음(untrusted)**으로 설정
- 신뢰하지 않는 파일에서는 잠재적으로 위험한 기능(로컬 변수 실행 등)을 비활성화
- 사용자가 명시적으로 파일이나 디렉토리를 신뢰 목록에 추가해야 함

이론적으로는 훌륭한 보안 설계이지만, **실제 사용에서 마찰**이 발생했습니다.

### 문제점: 보안과 편의성의 충돌

기본 신뢰 시스템에는 실용적인 문제가 있습니다:

1. 새 프로젝트를 클론할 때마다 신뢰를 명시적으로 부여해야 함
2. 여러 하위 디렉토리가 있는 대형 프로젝트는 개별 신뢰 설정이 번거로움
3. 많은 사용자들이 결국 보안 설정을 **비활성화**하여 구형 동작으로 돌아감

Yaron은 이를 "보안 기능이 불편하면 사람들이 우회한다"는 고전적인 보안 딜레마로 분석합니다.

### trust-manager 패키지

이 문제를 해결하기 위해 Yaron은 **trust-manager** 패키지를 개발했습니다:

#### 주요 기능

- **MELPA**에서 설치 가능 (`M-x package-install RET trust-manager`)
- 신뢰된 디렉토리/파일 목록을 **중앙에서 관리**하는 인터페이스 제공
- 프로젝트 단위로 신뢰를 일괄 부여하는 편의 기능
- 신뢰 상태를 시각적으로 확인하는 버퍼(buffer)

#### 사용 예시

```
M-x trust-manager-list    ; 신뢰된 항목 목록 보기
M-x trust-manager-add     ; 현재 파일/디렉토리를 신뢰 목록에 추가
M-x trust-manager-remove  ; 신뢰 목록에서 제거
```

### 더 큰 그림: Emacs의 보안 미래

Yaron의 글은 단순한 패키지 소개를 넘어, Emacs 보안의 근본적인 긴장 관계를 다룹니다:

- **강력한 확장성** ↔ **보안 격리(sandboxing)**
- **사용자 경험 편의성** ↔ **명시적 보안 설정**
- **신뢰할 수 있는 패키지 생태계** 구축의 필요성

저자는 trust-manager가 완벽한 해결책은 아니지만, Emacs 30의 신뢰 시스템을 **실용적으로 사용 가능하게 만드는 다리 역할**을 한다고 설명합니다.

### Hacker News 반응

- "Emacs를 사용한 지 20년인데 처음으로 보안에 대해 진지하게 생각하게 됐다"
- "Lisp 기반의 완전한 프로그래밍 환경을 가진 텍스트 에디터에서 신뢰 문제는 구조적"
- "VSCode와 비교하면 Emacs는 익스텐션 샌드박싱이 없는데, 이게 큰 차이"
- "trust-manager가 Emacs 코어에 통합될 가능성은? Yaron이 이미 GNU Emacs 기여자이니 가능성이 있어 보인다"
- LWN의 관련 글(코드 완성이 시스템 침해를 유발할 수 있다는 내용)을 함께 공유하며 Emacs 보안 논의가 확장

이 글은 수십 년 된 소프트웨어도 보안 현대화가 가능하며, 그 과정에서 **사용자 경험과 보안의 균형**을 찾는 것이 얼마나 중요한지 잘 보여주는 사례입니다.
