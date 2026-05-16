---
title:  "[2026-05-16 / Top 5] WSL9x – 리눅스를 위한 Windows 9x 서브시스템"
subtitle: "Windows 9x 커널 위에서 현대 Linux 6.19을 실행하는 역발상 프로젝트"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/posts/2026-05-16-hn-top5-windows-9x-subsystem-for-linux.jpg"
date:   2026-05-16 12:00:00
source_url: "https://codeberg.org/hails/wsl9x"
---

> 원본 기사: [https://codeberg.org/hails/wsl9x](https://codeberg.org/hails/wsl9x)

> HN 토론: [https://news.ycombinator.com/item?id=48120162](https://news.ycombinator.com/item?id=48120162)

### 개요

WSL9x는 Microsoft의 WSL(Windows Subsystem for Linux)을 뒤집은 역발상 프로젝트입니다. 현대 Linux(WSL)를 Windows에서 실행하는 대신, 현대 Linux 커널(6.19)을 Windows 9x 커널 위에서 협력적으로 실행합니다. 페이징, 메모리 보호, 선점형 스케줄링 등 현대 OS의 기능을 Windows 9x 환경에서도 활용할 수 있게 해주는 이 프로젝트는 "AI 없이 작성되었음"을 자랑스럽게 명시하고 있습니다.

### 주요 내용

#### 세 가지 핵심 구성 요소

WSL9x는 세 가지 컴포넌트로 구성됩니다:

1. **패치된 Linux 커널**: `win9x-um-6.19` 브랜치 - POSIX API 대신 Windows 9x 커널 API를 호출하도록 수정된 User-mode Linux 기반
2. **VxD 드라이버**: WSL9x를 초기화하고, 커널 코드 매핑을 설정하며, 디스크에서 `vmlinux.elf`를 로드
3. **wsl.com 클라이언트 프로그램**: 사용자 인터페이스 역할

#### 기술적 구현 방식

- Linux 커널은 고정 베이스 주소 `0xd0000000`에서 실행
- 시스템 콜은 GPF 핸들러(`int 0x80` 시스템 콜 인터럽트)를 통해 처리
- 링 0(슈퍼바이저 모드)에서 실행
- VxD 드라이버가 커널 초기화와 메모리 매핑을 담당

#### 역사적 의미

Windows 9x는 진정한 메모리 보호나 선점형 멀티태스킹이 없는 레거시 OS입니다. 그 위에서 이를 지원하는 현대 Linux 커널을 실행한다는 것은 놀라운 역공학적 성취로, 시스템 프로그래밍의 한계를 탐구하는 해커 문화의 정수를 보여줍니다.

### HN 커뮤니티 반응

점수 207점, 댓글 92개로 이번 Top 10 중 높은 관심을 받은 게시물입니다. HN 커뮤니티는 이런 기발하고 창의적인 시스템 해킹 프로젝트를 사랑하는 경향이 있어, Windows 9x의 내부 구조에 대한 회고적 토론과 User-mode Linux 구현 방식, VxD 드라이버 작성 경험 등 심층적인 기술 토론이 활발히 이루어졌을 것입니다. "AI 없이 작성"이라는 문구도 관심을 끌었을 것입니다.

### 시사점

WSL9x는 실용적인 목적보다는 기술적 도전과 탐구의 가치를 보여주는 프로젝트입니다. 레거시 시스템에 대한 깊은 이해가 현대 기술 혁신의 기반이 될 수 있음을 상기시켜 줍니다. 또한 AI 도구에 의존하지 않고 순수한 기술적 역량으로 이런 복잡한 프로젝트를 완성할 수 있다는 것을 보여주며, 로우레벨 시스템 프로그래밍의 매력을 다시 환기시킵니다.
