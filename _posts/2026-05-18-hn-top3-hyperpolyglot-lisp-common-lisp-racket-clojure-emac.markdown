---
title:  "[2026-05-18 / Top 3] 4가지 Lisp 방언 한눈에 비교: Common Lisp, Racket, Clojure, Emacs Lisp"
subtitle: "Lisp 계열 언어 문법과 기능을 나란히 놓은 완전 비교표"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-18 12:00:00
source_url: "https://hyperpolyglot.org/lisp"
---

> 원본 기사: [https://hyperpolyglot.org/lisp](https://hyperpolyglot.org/lisp)

> HN 토론: [https://news.ycombinator.com/item?id=48184322](https://news.ycombinator.com/item?id=48184322)

### 개요

Hyperpolyglot.org가 4가지 주요 Lisp 방언(dialect) — Common Lisp, Racket, Clojure, Emacs Lisp — 을 문법부터 매크로(macro), Java 상호운용(interop)까지 나란히 비교하는 포괄적인 참조 시트(reference sheet)를 공개했다. 프로그래밍 언어 학습자와 Lisp 생태계 탐색자들에게 빠른 교차 참조 자료로 활용될 수 있다.

### 주요 내용

#### Hyperpolyglot 프로젝트 소개

Hyperpolyglot은 동일한 기능을 여러 언어로 어떻게 구현하는지 나란히(side-by-side) 보여주는 비교 참조 사이트다. 언어 간 개념을 빠르게 매핑할 수 있어, 새로운 언어를 배울 때 특히 유용하다. 이번 Lisp 비교표는 그중에서도 가장 상세한 편에 속한다.

#### 비교되는 4가지 Lisp 방언

**Common Lisp**
- 1984년 표준화된 다목적 범용 Lisp
- ANSI 표준 언어로 강력한 매크로 시스템(CLOS, MOP 포함)
- SBCL, CCL 등 고성능 구현체 다수 존재

**Racket**
- 교육 및 언어 연구에 특화된 Lisp 계열
- 언어 설계 도구로서의 메타프로그래밍(metaprogramming) 강점
- DrRacket IDE와 함께 교육 현장에서 많이 사용

**Clojure**
- JVM(Java Virtual Machine) 위에서 동작하는 현대적 Lisp
- 함수형 프로그래밍(functional programming)과 불변 데이터 구조(immutable data structures) 강조
- Java 생태계와의 원활한 상호운용성

**Emacs Lisp**
- GNU Emacs 편집기의 확장 언어
- Emacs의 모든 기능을 프로그래밍으로 제어 가능
- 실용적이지만 다른 Lisp들에 비해 현대적 기능은 제한적

#### 비교표 커버 범위

총 17개 카테고리에 걸쳐 상세히 비교:

1. **문법/실행(Grammar/Execution)**: 기본 실행 방식, REPL 사용법
2. **변수(Variables)**: 바인딩(binding), 스코프(scope), 변경 가능성
3. **산술(Arithmetic)**: 숫자 타입, 연산자, 정밀도
4. **문자열(Strings)**: 생성, 조작, 포매팅
5. **정규식(Regex)**: 패턴 매칭 방식
6. **날짜/시간(Dates)**: 날짜 처리 라이브러리
7. **리스트(Lists)**: car/cdr, cons, map/filter/reduce
8. **딕셔너리(Dictionaries)**: 해시테이블(hash table), 연관 리스트(association list)
9. **함수(Functions)**: 정의 방식, 클로저(closure), 고차함수
10. **제어 흐름(Control Flow)**: 조건문, 반복문, 꼬리재귀(tail recursion)
11. **예외 처리(Exceptions)**: 에러 처리 메커니즘
12. **파일(Files)**: I/O 처리
13. **프로세스(Processes)**: 외부 프로세스 실행
14. **라이브러리(Libraries)**: 패키지 관리, 임포트
15. **OOP(객체지향 프로그래밍)**: 클래스, 메서드, 다형성
16. **매크로(Macros)**: 구문 변환(syntax transformation), 코드 생성
17. **반영/Java 상호운용(Reflection/Java Interop)**: 런타임 내성, Java 클래스 호출

### HN 커뮤니티 반응

HN 점수: 99점 | 댓글: 19개

**실용적 가치에 대한 공감**: Lisp 학습자들이 언어 간 차이를 빠르게 파악할 수 있는 자료라는 점에서 긍정적인 반응이 많았다. 특히 Common Lisp에서 Clojure로, 혹은 그 반대로 이동하는 개발자들에게 유용하다는 댓글이 이어졌다.

**각 방언에 대한 논쟁**: Emacs Lisp을 다른 범용 Lisp들과 함께 비교하는 것이 적절한지에 대한 의견이 나뉘었다. Emacs Lisp은 편집기 확장 언어로서 다른 목적을 가지므로, 비교 맥락에서 다소 이질적이라는 지적이 있었다.

**누락된 방언**: Scheme, Fennel, Janet, Hy 등 다른 Lisp 방언들이 포함되지 않은 것에 대한 아쉬움을 표명하는 댓글도 있었다. 특히 Scheme은 Racket의 전신이자 교육 현장에서 널리 쓰이므로 포함되어야 한다는 의견이 있었다.

**비교표의 한계**: 나란히 비교하는 형식은 각 언어의 관용구(idiom)와 철학적 차이를 충분히 전달하지 못한다는 시각도 제시되었다. Clojure의 불변성(immutability) 강조나 Racket의 언어 설계 철학은 단순한 문법 비교로는 파악하기 어렵다는 점이 지적되었다.

### 시사점

Lisp 계열 언어들은 AI, 함수형 프로그래밍, 메타프로그래밍 분야에서 다시 주목받고 있다. Common Lisp의 성숙한 생태계, Clojure의 JVM 통합 및 함수형 패러다임, Racket의 교육적 강점, Emacs Lisp의 생산성 도구로서의 가치는 각기 다른 맥락에서 활용 가능하다. 이 비교표는 Lisp 입문자는 물론 여러 Lisp 방언 사이를 오가는 숙련 개발자들에게도 빠른 참조 자료로 가치가 있다.
