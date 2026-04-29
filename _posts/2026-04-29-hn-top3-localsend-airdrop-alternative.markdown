---
title:  "[2026-04-29 / Top 3] Localsend: AirDrop의 오픈소스 크로스플랫폼 대안"
subtitle: "인터넷 없이 로컬 네트워크로 안전하게 파일을 공유하는 무료 앱"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-29 12:02:00
source_url: "https://github.com/localsend/localsend"
---

> 원본 기사: [https://github.com/localsend/localsend](https://github.com/localsend/localsend)

### 요약

**LocalSend**는 무료 오픈소스 앱으로, 인터넷 연결 없이 로컬 네트워크를 통해 주변 기기와 파일 및 메시지를 안전하게 공유할 수 있습니다. Apple의 AirDrop과 Google의 Quick Share를 대체하는 크로스플랫폼 솔루션입니다.

---

### 주요 특징

- **완전 크로스플랫폼**: Windows, macOS, Linux, Android, iOS 모두 지원
- **로컬 네트워크 전용**: 인터넷 불필요, 같은 Wi-Fi 또는 이더넷 네트워크 내에서 작동
- **엔드-투-엔드 암호화**: REST API와 HTTPS 암호화 사용
- **중앙 서버 없음**: 파일이 서버를 거치지 않아 데이터 프라이버시 보장

---

### 편의 기능

- **다양한 공유 형식**: 파일, 폴더, 텍스트, 클립보드 내용 공유 지원
- **즐겨찾기 기기**: 자주 연결하는 기기를 즐겨찾기로 저장 가능
- **PIN 보호**: 수신 시 PIN 인증으로 보안 강화
- **링크/QR 코드**: LocalSend가 설치되지 않은 기기와도 링크나 QR 코드로 공유 가능

---

### AirDrop과의 비교

| 항목 | AirDrop | LocalSend |
|------|---------|-----------|
| 플랫폼 | Apple 기기 전용 | 모든 OS |
| 오픈소스 | X | O |
| 무료 | O | O |
| 인터넷 필요 | X | X |
| 서버 경유 | X | X |

---

### 한계

같은 네트워크(Wi-Fi 또는 이더넷)에 연결된 기기 간에만 작동합니다. 다른 네트워크의 기기와는 링크/QR 코드 방식을 이용해야 합니다.

GitHub에서 오픈소스로 개발되고 있으며, 현재 HN에서 다시 큰 주목을 받고 있습니다.
