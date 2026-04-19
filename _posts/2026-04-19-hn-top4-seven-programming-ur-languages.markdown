---
title:  "[2026-04-19 / Top 4] 일곱 가지 프로그래밍 원형 언어 (2022)"
subtitle: "모든 프로그래밍 언어의 뿌리, 7가지 원형(ur-language)으로 이해하는 언어 설계의 본질"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-19 12:30:00
source_url: "https://madhadron.com/programming/seven_ur_languages.html"
---

> 원본 기사: [https://madhadron.com/programming/seven_ur_languages.html](https://madhadron.com/programming/seven_ur_languages.html)

### 개요

**madhadron**이 작성한 "The Seven Programming Ur-Languages"가 2022년 작성된 글임에도 불구하고 2026년 4월 HN에서 다시 주목받으며 245포인트를 획득했습니다. 이 글은 오늘날 존재하는 수천 가지 프로그래밍 언어를 단 **7가지 원형(ur-language)**으로 분류할 수 있다는 독창적인 주장을 담고 있습니다.

### "원형 언어(Ur-Language)"란?

저자는 고생물학에서 특정 종을 대표하는 화석 표본(type specimen)을 이름의 기원으로 삼듯이, 프로그래밍 언어도 각 계열의 원형을 대표하는 "ur-language"가 있다고 주장합니다. 같은 원형을 공유하는 언어들 사이의 전환은 쉽지만, 전혀 다른 원형의 언어로 이동하려면 상당한 사고 방식의 전환이 필요합니다.

### 7가지 원형 언어

#### 1. ALGOL (알골)
현대 프로그래밍 언어의 가장 보편적인 원형입니다. 변수 할당, 조건문(`if`/`else`), 반복문(`for`/`while`), 함수로 구성된 순차적 프로그램 구조가 핵심입니다. C, Java, Python, Go, Rust 등 대부분의 주류 언어가 여기에 속합니다.

#### 2. Lisp (리스프)
괄호로 감싸인 전위 표기식(prefix expression)이 기본 단위입니다. 코드 자체가 데이터 구조(S-expression)이며, 매크로 시스템을 통해 컴파일러에 넘기기 전에 코드를 변환할 수 있습니다. Clojure, Scheme, Racket, Emacs Lisp 등이 이 계열입니다.

#### 3. ML
정적 타입 추론과 패턴 매칭이 핵심입니다. 케임브리지 대학에서 정리 증명 프로그램의 메타 언어(metalanguage)로 개발됐습니다. Haskell, OCaml, F#, Elm, 그리고 Rust의 타입 시스템 일부가 ML 계보입니다.

#### 4. Self (셀프)
프로토타입 기반 객체지향의 원형입니다. 객체들이 서로 메시지를 주고받으며 동작하고, 클래스 없이 기존 객체를 복제(clone)하여 새 객체를 만듭니다. JavaScript의 프로토타입 체인이 Self의 직접적인 영향을 받았습니다.

#### 5. Forth (포스) — 스택 언어
HP 역폴란드 표기법(RPN) 계산기의 문법을 따르는 스택 기반 언어들입니다. 리터럴을 입력하면 스택에 쌓이고, 연산자는 스택에서 값을 꺼내 계산한 뒤 결과를 다시 스택에 넣습니다. Factor, Joy, PostScript가 여기에 속하며, WebAssembly의 스택 머신 모델도 이 계보입니다.

#### 6. APL (에이피엘)
배열(array)을 1급 시민으로 다루며, 단일 연산자로 전체 배열을 처리합니다. 수학 표기법에 가까운 특수 기호를 활용하는 극도로 간결한 언어입니다. J, K, Q, numpy의 브로드캐스팅 패러다임이 APL에서 영향을 받았습니다.

#### 7. Prolog (프롤로그)
논리 프로그래밍의 원형입니다. 사실(facts)과 규칙(rules)을 선언하면, 해석기가 목표(goal)를 충족하는 해를 자동으로 탐색합니다. Datalog, Mercury, 그리고 SQL의 선언적 패러다임도 이 계열과 맥을 같이 합니다.

### 왜 이것이 중요한가?

저자의 핵심 주장은: **같은 원형의 언어를 배우는 것은 쉽지만, 다른 원형의 언어를 배우는 것은 완전히 새로운 사고 방식을 요구한다**는 것입니다.

예를 들어:
- Java에서 Kotlin으로 전환 → 쉬움 (둘 다 ALGOL 계열)
- Java에서 Haskell로 전환 → 어려움 (ALGOL → ML, 전혀 다른 사고 방식)
- Python에서 Clojure로 전환 → 어려움 (ALGOL → Lisp)

### Hacker News 반응

- "7가지 분류가 완벽하지는 않지만, 언어 학습의 난이도를 직관적으로 설명하는 좋은 프레임워크"
- "Icon, SNOBOL 같은 문자열 중심 언어나 Erlang의 Actor 모델은 어디에 속하는가?"
- "Rust는 ALGOL과 ML의 혼합체 — 원형 분류의 경계선이 모호해지는 현대 언어들"
- "이 글을 읽고 Prolog를 처음 배우기 시작했다 — 완전히 다른 세상이었다"

이 글이 4년이 지나도 HN 상위에 다시 오를 수 있었던 것은, 프로그래밍 언어의 본질을 꿰뚫는 통찰이 시간이 지나도 유효하기 때문입니다.
