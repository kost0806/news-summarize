---
title:  "[2026-05-18 / Top 6] Bitwarden의 조용한 변신: 새 경영진, 달라진 가치관"
subtitle: "M&A 전문가 CEO 교체, 무료 약속 삭제, 투명성 제거까지"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/posts/2026-05-18-hn-top6-the-quiet-renovation-at-bitwarden.jpg"
date:   2026-05-18 12:00:00
source_url: "https://blog.ppb1701.com/the-quiet-renovation-at-bitwarden"
---

> 원본 기사: [https://blog.ppb1701.com/the-quiet-renovation-at-bitwarden](https://blog.ppb1701.com/the-quiet-renovation-at-bitwarden)

> HN 토론: [https://news.ycombinator.com/item?id=48163389](https://news.ycombinator.com/item?id=48163389)

### 개요

오픈소스 패스워드 관리자(password manager)로 신뢰를 받아온 Bitwarden이 보도자료 없이 조용히 여러 중요한 변화를 단행했다. CEO 및 CFO 교체, "영구 무료(Always free)" 문구 삭제, 핵심 가치에서 "투명성(Transparency)"과 "포용성(Inclusion)" 제거 등 변화들이 사용자들의 우려를 불러일으키고 있다. 저자는 이미 자체 호스팅(self-hosted) Vaultwarden으로 이전했다.

### 주요 내용

#### CEO 교체: 기술 창업자에서 M&A 전문가로

2019년부터 재직해온 CEO Michael Crandell이 **Michael Sullivan**으로 교체되었다. Sullivan의 이력:

- Vista Equity에 의한 **10억 달러 Acquia 인수**를 주도
- Hg의 **10억 달러 Insightsoftware 투자** 참여

Sullivan은 제품 비전을 가진 기술 창업자가 아닌, 사모펀드(PE, Private Equity) M&A 전문가다. 이는 Bitwarden의 향후 방향성에 대한 중요한 신호로 해석된다.

#### CFO 교체

CFO Stephen Morrison이 **Michael Shenkman**으로 교체되었다. Shenkman은 디자인 협업 플랫폼 InVision의 전 CEO 출신이다.

#### "영구 무료" 문구 삭제

개인 패스워드 관리자 페이지에서 오랫동안 유지되던 **"Always free(영구 무료)"** 문구가 조용히 삭제되었다. 공식 발표나 설명 없이 이루어진 이 변화는 향후 유료화 가능성에 대한 우려를 낳고 있다.

#### 핵심 가치 변경: GRIT의 재정의

Bitwarden의 핵심 가치 체계인 GRIT가 다음과 같이 변경되었다:

**기존 GRIT**
- **G**ratitude (감사)
- **R**esponsibility (책임)
- **I**nclusion (포용성) ← **삭제**
- **T**ransparency (투명성) ← **삭제**

**새로운 GRIT**
- **G**ratitude (감사)
- **R**esponsibility (책임)
- **I**nnovation (혁신) ← **신규 추가**
- **T**rust (신뢰) ← **신규 추가**

패스워드 관리자 서비스에서 "투명성(Transparency)"을 핵심 가치에서 제거한다는 것은 특히 상징적으로 해석될 수 있다. 모든 이 변화들이 **보도자료나 공식 발표 없이** 이루어졌다는 점도 아이러니다.

#### 저자의 대응

저자는 이러한 변화들을 인지한 후 자체 호스팅 대안인 **Vaultwarden**으로 이전했다. Vaultwarden은 Bitwarden과 호환되는 서버를 Rust로 구현한 오픈소스 프로젝트로, 사용자가 직접 서버를 운영할 수 있다.

### HN 커뮤니티 반응

HN 점수: 462점 | 댓글: 216개

이 게시물은 HN에서 높은 점수와 많은 댓글을 기록하며 큰 파장을 일으켰다:

**대규모 이전 선언**: 많은 댓글이 Bitwarden에서 대안으로 이전할 계획을 밝혔다. Vaultwarden, KeePass, 1Password, Proton Pass 등이 대안으로 언급되었다.

**PE 인수 패턴 우려**: 사모펀드 배경의 경영진 교체가 일반적으로 어떤 결과를 낳는지에 대한 사례 분석이 활발히 이루어졌다. "PE는 수익화를 위해 들어온다"는 패턴 인식이 공유되었다.

**오픈소스 신뢰 논쟁**: 코드는 오픈소스지만 서비스 자체는 변질될 수 있다는 점에서, 오픈소스 패스워드 관리자라도 외부 서비스에 의존하면 취약하다는 논의가 이루어졌다.

**Vaultwarden 추천**: 여러 사용자가 Vaultwarden을 적극 추천하며 설정 가이드와 경험담을 공유했다. 자체 호스팅의 복잡성보다 데이터 통제권이 중요하다는 의견이 많았다.

### 시사점

이 사례는 오픈소스 기반의 신뢰할 수 있는 서비스가 경영진 교체를 통해 어떻게 변화할 수 있는지를 보여주는 교과서적 사례다. 특히 패스워드 관리자처럼 민감한 데이터를 다루는 서비스의 경우, 비즈니스 모델과 가치관의 변화가 사용자에게 직접적인 리스크로 연결된다. 중요한 서비스를 외부 제공자에게 의존할 때는 항상 자체 호스팅 대안을 마련해두는 것이 현명한 전략이다.
