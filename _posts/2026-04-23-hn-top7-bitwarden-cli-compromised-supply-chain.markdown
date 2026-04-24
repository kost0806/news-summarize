---
title:  "[2026-04-23 / Top 7] Checkmarx 공급망 공격 캠페인에서 Bitwarden CLI 손상됨"
subtitle: "공격자들이 Bitwarden의 CI/CD 파이프라인에서 GitHub Action을 악용하여 Bitwarden CLI 2026.4.0을 손상시켰습니다."
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-23 15:00:00
source_url: "https://socket.dev/blog/bitwarden-cli-compromised"
---

> 원본 기사: [https://socket.dev/blog/bitwarden-cli-compromised](https://socket.dev/blog/bitwarden-cli-compromised)

### 공격 개요
4월 22일 93분간 @bitwarden/cli@2026.4.0이 손상되어 배포되었습니다. 악성 페이로드는 손상된 GitHub Action을 통해 bw1.js 파일로 전달되었으며, npm install 실행 시 자동으로 실행되었습니다.

### 탈취된 정보
- SSH 키, 클라우드 시크릿, AI 코딩 도구 자격증명 탈취
- AWS SSM, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager 접근

### 대응 및 위험
조직은 악성 패키지를 즉시 제거하고 GitHub 토큰, npm 토큰, 클라우드 자격증명, SSH 키 등을 회전해야 합니다. Bitwarden은 엔드 사용자 데이터가 액세스되지 않았음을 강조했습니다.
