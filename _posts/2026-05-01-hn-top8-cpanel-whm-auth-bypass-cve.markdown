---
title:  "[2026-05-01 / Top 8] cPanel·WHM 인증 우회 취약점 — CVE-2026-41940"
subtitle: "CVSS 9.8 치명적 취약점, 7천만 개 도메인 영향 — 즉각 패치 필요"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-01 12:07:00
source_url: "https://labs.watchtowr.com/the-internet-is-falling-down-falling-down-falling-down-cpanel-whm-authentication-bypass-cve-2026-41940/"
---

> 원본 기사: [https://labs.watchtowr.com/the-internet-is-falling-down-falling-down-falling-down-cpanel-whm-authentication-bypass-cve-2026-41940/](https://labs.watchtowr.com/the-internet-is-falling-down-falling-down-falling-down-cpanel-whm-authentication-bypass-cve-2026-41940/)

### CVE-2026-41940: cPanel/WHM 인증 완전 우회 취약점

보안 연구 기업 **watchTowr**가 공개한 **CVE-2026-41940**은 cPanel 및 WHM에서 발견된 치명적 인증 우회 취약점입니다. CVSS 점수 **9.8(Critical)**을 받았으며, 약 **7천만 개 도메인**을 관리하는 cPanel의 모든 지원 버전에 영향을 미칩니다.

#### 취약점 작동 원리: CRLF 인젝션

이 취약점은 **CRLF 인젝션(캐리지 리턴/라인 피드 삽입)**을 이용해 로그인 과정을 완전히 우회합니다.

1. 공격자가 악의적인 기본 인증 헤더에 원시 `\r\n` 문자를 삽입
2. cPanel 서비스 데몬(cpsrvd)이 세션 파일을 저장할 때 데이터를 검증하지 않는 점을 악용
3. `user=root` 또는 `tfa_verified=1` 같은 임의 속성을 세션 파일에 주입
4. **2단계 인증(2FA)까지 무력화**하고 루트 권한 획득 가능

#### 영향 범위와 긴급도

- 모든 지원 버전의 cPanel/WHM에 영향
- **2026년 2월부터 제로데이로 실제 공격에 활용**된 정황 확인
- 공개 PoC(개념 증명 코드)도 이미 배포되어 즉각적 위험 수준

#### 권장 조치

- **즉각적인 cPanel/WHM 패치** 적용 (최신 버전으로 업데이트)
- 세션 파일 이상 여부 점검
- 루트 및 WHM 계정 비밀번호 재설정
- 비정상적인 로그인 시도 로그 확인

cPanel을 사용하는 웹 호스팅 제공업체와 독립 서버 운영자는 즉시 패치를 적용해야 합니다.
