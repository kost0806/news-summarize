---
title:  "[2026-05-13 / Top 8] AWS로 돌아왔더니 떠났던 이유가 다시 떠올랐다"
subtitle: "15년 만에 AWS로 복귀한 개발자가 마주한 복잡성과 비용의 현실"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-13 10:50:00
source_url: "http://fourlightyears.blogspot.com/2026/05/i-returned-to-aws-and-was-reminded-hard.html"
---

> 원본 기사: [http://fourlightyears.blogspot.com/2026/05/i-returned-to-aws-and-was-reminded-hard.html](http://fourlightyears.blogspot.com/2026/05/i-returned-to-aws-and-was-reminded-hard.html)

> HN 토론: [https://news.ycombinator.com/item?id=48073201](https://news.ycombinator.com/item?id=48073201)

### AWS의 초기 열성 지지자가 15년 후 다시 마주한 현실

초기 AWS 열혈 지지자였던 개발자가 오랜만에 AWS로 돌아왔다가, 결국 AWS를 떠났던 이유들을 다시 한번 뼈저리게 경험했다는 블로그 글이다.

#### 무엇이 문제였나

**1. 기하급수적으로 복잡해진 서비스 체계**
AWS는 수백 개의 서비스를 제공하며, 각 서비스마다 수십 개의 설정 옵션이 있다. 단순한 웹 애플리케이션을 배포하는 데도 EC2, VPC, IAM, Security Groups, Load Balancer, RDS 등 수많은 개념을 이해해야 한다. 초기에는 단순했던 AWS가 거대한 복잡성의 미로가 됐다.

**2. 예측하기 어려운 비용**
AWS의 과금 모델은 매우 복잡하다. 데이터 전송 비용, API 호출 비용, 스토리지 비용, 컴퓨팅 비용이 뒤엉켜 청구서를 예측하기 어렵다. 실수로 수천 달러를 청구받는 일도 흔하다.

**3. 벤더 종속(Vendor lock-in)**
AWS의 독자적 서비스(Lambda, DynamoDB, SQS 등)에 깊이 의존할수록 다른 클라우드나 온프레미스로 이전하는 비용이 천문학적으로 커진다.

#### 저자의 결론

완벽한 클라우드는 없지만, AWS는 대규모 엔터프라이즈 환경에 최적화된 반면 중소 규모 프로젝트에는 과도하게 복잡하다. 저자는 더 단순한 대안을 찾아가기로 했다.

#### HN 커뮤니티 반응

이 글은 개발자들의 강한 공감을 얻었다. "AWS의 복잡성은 의도적인 것"이라는 주장과 "복잡성이 곧 유연성"이라는 반론이 맞섰다. Fly.io, Hetzner, Railway 등 더 단순한 클라우드 대안들을 추천하는 댓글도 많았다. "AWS는 규모가 커질 것을 대비한 것이고, 처음부터 쓰기엔 너무 무겁다"는 의견도 공감을 받았다.
