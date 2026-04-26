---
title:  "[2026-04-26 / Top 9] Turbo Vision 2.0 – 현대적인 포팅"
subtitle: "90년대 Borland TUI 프레임워크가 크로스 플랫폼·유니코드 지원으로 부활"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-26 09:00:00
source_url: "https://github.com/magiblot/tvision"
---

> 원본 기사: [https://github.com/magiblot/tvision](https://github.com/magiblot/tvision)

### 개요

1990년대 Borland가 개발한 텍스트 기반 사용자 인터페이스(TUI) 프레임워크 Turbo Vision 2.0을 현대적으로 포팅한 `tvision` 프로젝트가 Hacker News에서 큰 주목을 받고 있습니다. magiblot이 개발한 이 프로젝트는 기존 API를 유지하면서 크로스 플랫폼 지원과 UTF-8 기반 유니코드를 추가했습니다.

### 주요 내용

- **원본 프레임워크**: Turbo Vision은 Borland Pascal/C++용 TUI 프레임워크로, 1990년대 도스(DOS) 환경에서 메뉴, 대화상자, 창 기반 인터페이스를 쉽게 만들 수 있게 해주었습니다. 당시로서는 혁신적인 컴포넌트 기반 아키텍처를 갖추었습니다.
- **현대화 내용**: 터미널 기능 및 I/O를 라이브러리가 처리하여 개발자는 애플리케이션 동작과 외관에만 집중할 수 있습니다. UTF-8 인코딩을 통한 유니코드 입력·출력이 지원됩니다.
- **크로스 플랫폼**: 리눅스, macOS, Windows 등 다양한 플랫폼에서 동작하며, vcpkg를 통해 설치할 수 있습니다.
- **활용 사례**: magiblot이 직접 제작한 Turbo(텍스트 에디터), tvterm(터미널 에뮬레이터) 외에도 TMBASIC(콘솔 애플리케이션 개발 언어) 등이 tvision 위에 구축되었습니다.

### 시사점

터미널 기반 UI는 SSH 원격 접속, 저사양 환경, 서버 관리 도구 등에서 여전히 강력한 존재감을 유지하고 있습니다. tvision은 현대적인 TUI 애플리케이션 개발에 검증된 프레임워크를 제공하며, 특히 레트로 컴퓨팅 감성을 현대 환경에 재현하려는 개발자들에게 매력적인 선택입니다. 클래식 소프트웨어의 재발견이 이어지는 흐름 속에서 주목할 만한 프로젝트입니다.
