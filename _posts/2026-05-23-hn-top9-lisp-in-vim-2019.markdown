---
title:  "[2026-05-23 / Top 9] Vim에서 Lisp 사용하기 (2019)"
subtitle: "HN 18점 · 4개 댓글"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-23 12:08:00
source_url: "https://susam.net/lisp-in-vim.html"
---

> 원본 기사: [https://susam.net/lisp-in-vim.html](https://susam.net/lisp-in-vim.html)

> HN 토론: [https://news.ycombinator.com/item?id=48248238](https://news.ycombinator.com/item?id=48248238)

### 개요

Vim에서 Lisp 개발 환경을 구축하는 방법을 상세히 안내하는 튜토리얼입니다. Emacs의 SLIME과 유사한 대화형 개발 경험을 제공하는 두 가지 Vim 플러그인, Slimv와 Vlime을 비교하고 설치 방법을 설명합니다.

### 주요 내용

- **Slimv**: 2009년 Tamas Kovacs가 만든 Vim 플러그인. "Superior Lisp Interaction Mode for Vim"의 약자. Swank 서버를 번들로 포함
- **Vlime**: 2017년 Kay Z가 만든 더 최신 플러그인. Swank 서버를 자동 다운로드하며 더 모던한 설계
- **Swank 서버**: 두 플러그인 모두 TCP 서버(Swank)를 통해 Vim과 Lisp REPL을 연결하는 클라이언트-서버 아키텍처 사용
- **지원 구현체**: SBCL, CLISP, ECL 등 주요 Common Lisp 구현체와 호환
- **대화형 개발**: 코드 평가, 자동완성, 문서 조회 등 SLIME 수준의 대화형 개발 가능

### HN 커뮤니티 반응

HN 점수 18점, 댓글 4개. 커뮤니티에서는 현재 Neovim을 위한 Lisp 플러그인으로는 Conjure가 더 선호된다는 의견이 있었습니다. Conjure는 Clojure, Common Lisp, Fennel 등을 지원하며, Fennel로 Neovim을 설정하는 경험도 공유되었습니다.

### 시사점

Emacs가 아닌 Vim/Neovim을 선호하는 Lisp 개발자들을 위한 실용적인 가이드입니다. 클래식 콘텐츠가 다시 HN에 오르며 주목받은 사례입니다.
