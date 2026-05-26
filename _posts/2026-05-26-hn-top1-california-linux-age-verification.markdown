---
title:  "[2026-05-26 / Top 1] 캘리포니아, 반발 이후 연령 인증법에서 리눅스 면제 추진"
subtitle: "동일 법안을 발의한 의원이 직접 수정안 제출, 오픈소스 OS 적용 면제 예정"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-26 12:00:00
source_url: "https://www.tomshardware.com/software/linux/california-moves-to-exempt-linux-from-its-upcoming-age-verification-law-after-backlash-over-forcing-operating-systems-to-collect-users-ages-amendment-proposed-by-the-same-lawmaker-who-wrote-the-original-law"
---

> 원본 기사: [Tom's Hardware](https://www.tomshardware.com/software/linux/california-moves-to-exempt-linux-from-its-upcoming-age-verification-law-after-backlash-over-forcing-operating-systems-to-collect-users-ages-amendment-proposed-by-the-same-lawmaker-who-wrote-the-original-law)

> HN 토론: [https://news.ycombinator.com/item?id=48269961](https://news.ycombinator.com/item?id=48269961)

### 개요

캘리포니아 주의회가 리눅스 및 오픈소스 운영체제를 연령 인증법(AB 1043) 적용 대상에서 면제하는 수정안(AB 1856)을 추진하고 있다. 원래 법안을 발의한 당사자인 의원이 직접 수정안을 제출했다는 점에서 이례적인 사례로 주목받고 있다.

### 주요 내용

캘리포니아는 2025년 후반 '디지털 연령 인증법(Digital Age Assurance Act, AB 1043)'을 통과시켰다. 이 법은 온라인 연령 인증 책임을 개별 웹사이트나 앱이 아닌 **운영체제 레벨**로 옮기는 내용으로, 2027년 1월 1일 발효 예정이었다. 구체적으로는 OS가 기기 설정 시 사용자의 연령이나 생년월일을 수집한 뒤 이를 앱과 앱스토어에 '연령 구간 신호'로 제공하도록 요구한다.

그러나 이 법이 **리눅스 배포판에 적용될 경우** 다음과 같은 심각한 문제가 발생한다는 지적이 잇따랐다:

- Debian, Fedora, Ubuntu, Arch, Mint 등 주요 리눅스 배포판은 수천 명의 자원봉사자가 관리하는 분산된 오픈소스 프로젝트로, 중앙화된 연령 인증 인프라를 구축하기가 사실상 불가능하다.
- 프라이버시 활동가들은 OS가 사용자 연령 정보를 수집하면 감시와 추적의 도구로 악용될 수 있다고 경고했다.
- 개발자들은 이 법이 리눅스를 법적으로 불법화하거나 리눅스 프로젝트를 캘리포니아에서 사용 불가로 만들 수 있다고 우려했다.

이에 따라 수정안 AB 1856이 제출되었다. 이 수정안은 사용자가 "소프트웨어를 복사, 재배포, 수정할 수 있도록 허용하는 라이선스" 하에 배포되는 OS를 법 적용 대상에서 제외한다. 실질적으로 GPL, LGPL, MIT, Apache 등 대부분의 오픈소스 라이선스가 적용된 리눅스 배포판이 면제될 전망이다.

### 경과

- 수정안 최신본: 2026년 5월 18일 버전
- 2026년 5월 19일: 2차 독회 완료, 3차 독회 예정
- 6월 위원회 심의 예정

### HN 커뮤니티 반응

HN에서 905점, 393개 댓글로 오늘의 가장 뜨거운 화제가 되었다. 많은 사용자들이 오픈소스 커뮤니티의 조직적인 반발이 실제로 정책을 바꾼 드문 사례라며 긍정적으로 평가했다. 다만 일부는 상업용 리눅스 배포판(Red Hat Enterprise Linux 등)이 면제 대상에 포함될지 여부를 두고 논쟁을 벌이기도 했다.

### 시사점

이번 사례는 오픈소스 커뮤니티와 프라이버시 활동가들의 집단적 목소리가 실제 입법 과정에서 효과를 발휘할 수 있음을 보여준다. 또한 기술 정책 입안 시 오픈소스 생태계의 특수성을 고려해야 한다는 중요한 선례를 남겼다.
