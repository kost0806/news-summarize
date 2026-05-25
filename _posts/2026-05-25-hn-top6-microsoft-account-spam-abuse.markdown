---
title:  "[2026-05-25 / Top 6] 사기꾼들이 마이크로소프트 내부 계정을 악용해 스팸 발송"
subtitle: "TechCrunch: 합법적인 MS 인프라 주소에서 발송되는 피싱 이메일, 스팸 필터 우회"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-25 12:05:00
source_url: "https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/"
---

> 원본 기사: [https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/](https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/)

> HN 토론: [https://news.ycombinator.com/item?id=48253186](https://news.ycombinator.com/item?id=48253186)

### 개요

TechCrunch의 2026년 5월 21일 보도에 따르면, 사기꾼들이 마이크로소프트의 공식 인프라 이메일 주소(`msonlineservicesteam@microsoftonline.com`)를 악용해 피싱 이메일을 발송하는 취약점을 발견했다.

### 주요 내용

#### 공격 방식

- 사기꾼들이 마이크로소프트 계정을 생성하고 알림 시스템을 조작하여 실제 마이크로소프트 서버에서 이메일을 발송하는 루프홀을 악용
- 해당 이메일은 마이크로소프트의 진짜 서버에서 발송되므로 **SPF/DKIM 인증**을 모두 통과
- 기존 스팸 필터와 이메일 보안 시스템을 정상적으로 우회

#### 피해 현황

이메일에는 명백한 사기성 내용과 악성 사이트 링크가 포함되어 있지만, 발송 주소의 합법성이 신뢰감을 부여한다:

- 수신자 입장에서 "microsoftonline.com" 도메인에서 온 이메일이므로 스팸으로 의심하기 어려움
- 유사한 알림 인프라 남용이 다른 대형 기업에서도 발견된 사례 있음

#### 마이크로소프트의 대응

보안 연구자들이 이 취약점을 마이크로소프트에 보고했으나, 2026년 5월 기사 작성 시점까지 완전한 수정이 이루어지지 않은 상태였다.

### 시사점

이메일 보안의 핵심인 SPF/DKIM 인증이 도메인 소유자 자신의 인프라가 남용될 때는 무력화된다는 것을 보여준다. 대형 플랫폼의 알림 시스템 설계에 내재된 구조적 취약점이며, 단순히 발신 주소를 확인하는 것만으로는 피싱을 방어할 수 없다는 사실을 다시 한번 상기시킨다.
