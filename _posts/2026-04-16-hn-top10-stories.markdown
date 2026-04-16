---
title:  "Hacker News 오늘의 Top 10 (2026-04-16)"
subtitle: "DaVinci Resolve 21 포토, Darkbloom, SDL의 AI 코드 금지, WordPress 백도어 등"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/posts/2026-04-16-hn-top10.jpg"
date:   2026-04-16 12:00:00
source_url: "https://news.ycombinator.com"
---

> 원본: [Hacker News](https://news.ycombinator.com)

2026년 4월 16일 Hacker News 상위 10개 스토리를 요약합니다.

---

#### 1. DaVinci Resolve 21 – Photo 페이지 출시

> 원본 기사: [https://www.blackmagicdesign.com/products/davinciresolve/photo](https://www.blackmagicdesign.com/products/davinciresolve/photo)

Blackmagic Design이 DaVinci Resolve 21을 발표하며 새로운 **Photo 페이지**를 공개했습니다. 할리우드급 색보정 도구를 사진 편집에 그대로 활용할 수 있어 Adobe Lightroom의 강력한 경쟁자로 주목받고 있습니다. Canon, Fujifilm, Nikon, Sony, iPhone ProRAW 등 주요 카메라의 네이티브 RAW 파일을 지원하며, AI IntelliSearch, AI CineFocus, AI Blemish Removal 등 AI 기반 도구도 포함되었습니다. 현재 공개 베타로 무료 다운로드 가능합니다.

---

#### 2. Backblaze, 사용자 통지 없이 클라우드 폴더 백업 조용히 중단

> 원본 기사: [https://rareese.com/posts/backblaze/](https://rareese.com/posts/backblaze/)

클라우드 백업 서비스 Backblaze가 2025년 12월 버전 9.2.2.877 업데이트를 통해 OneDrive, Dropbox, Google Drive 등 클라우드 스토리지 폴더의 백업을 조용히 중단했습니다. 별도의 사용자 통지 없이 릴리스 노트에 "성능 개선" 항목으로만 표기했으며, 파일 복구가 필요한 시점에야 수백 GB 데이터가 백업되지 않았다는 사실을 알게 된 사용자들의 불만이 폭발했습니다. 10년 이상 사용자들도 피해를 입었으며, 클라우드 백업 서비스의 신뢰성 문제가 다시 부각되고 있습니다.

---

#### 3. SDL, LLM/AI 생성 코드 기여 공식 금지

> 원본 기사: [https://www.phoronix.com/news/SDL-Says-No-To-AI-LLMs](https://www.phoronix.com/news/SDL-Says-No-To-AI-LLMs)

크로스플랫폼 오픈소스 게임 개발 라이브러리 SDL(Simple DirectMedia Layer)이 ChatGPT, Claude, Copilot, Grok 등 LLM으로 생성된 코드 기여를 공식 금지했습니다. PR 템플릿과 AGENTS.md 파일을 통해 정책을 명문화했으며, 금지 이유로는 AI 생성 코드의 출처 불명확성으로 인한 Zlib 라이선스 충돌 가능성을 들었습니다. 단, AI를 이용한 문제 식별은 허용하되 해결책은 반드시 사람이 직접 작성해야 합니다.

---

#### 4. 30개 WordPress 플러그인 매입 후 백도어 삽입한 공급망 공격

> 원본 기사: [https://anchor.host/someone-bought-30-wordpress-plugins-and-planted-a-backdoor-in-all-of-them/](https://anchor.host/someone-bought-30-wordpress-plugins-and-planted-a-backdoor-in-all-of-them/)

공격자가 WordPress 플러그인 30개 이상을 Flippa 등 마켓플레이스를 통해 6자리 금액(USD)에 매입한 뒤, 2025년 8월 PHP 역직렬화 백도어를 심고 8개월간 잠복했습니다. 2026년 4월 5~6일 UTC 04:22~11:06 사이 6시간 44분 동안 백도어가 활성화되어 구글봇에만 SEO 스팸을 노출하는 클로킹 방식으로 동작했습니다. 영향받은 플러그인 설치 수는 40만 건 이상이며, WordPress.org는 관련 플러그인을 영구 폐쇄했습니다. 신뢰받는 오픈소스 플러그인도 소유권 이전 후 공격 벡터가 될 수 있음을 보여준 사례입니다.

---

#### 5. IPv6 트래픽, 전 세계 50% 돌파

> 원본 기사: [https://techplanet.today/post/ipv6-adoption-reaches-50-the-long-journey-toward-internets-next-generation](https://techplanet.today/post/ipv6-adoption-reaches-50-the-long-journey-toward-internets-next-generation)

Google 통계 기준 전 세계 IPv6 트래픽 점유율이 처음으로 50%를 초과했습니다. 국가별로는 프랑스 78%, 독일 76%, 인도 72%, 미국 53% 수준이며, 인터넷이 IPv4에서 IPv6으로 전환된 지 약 20년 만의 이정표입니다. 다만 레거시 인프라 투자 비용, IPv4 주소 희소성 관련 경제적 요인, 듀얼스택 운용 복잡성 등으로 인해 완전한 전환은 여전히 더디게 진행되고 있습니다.

---

#### 6. Darkbloom – 유휴 Mac을 활용한 프라이빗 AI 추론 네트워크

> 원본 기사: [https://darkbloom.dev](https://darkbloom.dev)

Eigen Labs가 유휴 Apple Silicon Mac을 분산형 AI 추론 네트워크로 활용하는 **Darkbloom**을 출시했습니다. Azure OpenAI, AWS Bedrock 대비 50~70% 저렴한 비용으로 AI 추론을 처리하며, Mac 운영자는 토큰 수익의 95%를 가져갑니다. 엔드투엔드 암호화와 커널 레벨 디버거 차단으로 노드 운영자조차 처리 데이터를 볼 수 없는 프라이버시 구조를 갖추고 있습니다. 출시 당일 기준 21개 노드로 시작했으며, OpenAI 호환 API를 제공합니다. 아직 감사되지 않은 아키텍처로 테스트 용도로만 권장됩니다.

---

#### 7. Google, '뒤로가기 버튼 하이재킹'을 스팸으로 규정

> 원본 기사: [https://developers.google.com/search/blog/2026/04/back-button-hijacking](https://developers.google.com/search/blog/2026/04/back-button-hijacking)

Google이 브라우저 뒤로가기 버튼을 방해하는 행위를 스팸 정책 위반으로 공식 지정하고, 2026년 6월 15일부터 시행한다고 발표했습니다. 대상은 사용자가 뒤로가기를 눌렀을 때 방문한 적 없는 페이지로 리디렉션하거나 정상 브라우저 탐색을 방해하는 모든 사이트입니다. 위반 시 검색 순위 강등 또는 수동 스팸 조치를 받을 수 있으며, 서드파티 광고 라이브러리에 의한 하이재킹도 사이트 운영자의 책임으로 간주됩니다.

---

#### 8. XOR 스왑 트릭에 관한 과도한 논의 (heather.cafe)

> 원본 기사: [https://heather.cafe/posts/too_much_xor_swap_trick/](https://heather.cafe/posts/too_much_xor_swap_trick/)

프로그래밍 교육에서 XOR 스왑 트릭이 지나치게 강조된다는 내용의 블로그 포스트입니다. `a ^= b; b ^= a; a ^= b;` 형태로 임시 변수 없이 두 변수를 교환하는 이 기법은 현대 컴파일러와 CPU에서는 일반 방식보다 성능 이점이 없으며, 두 포인터가 같은 메모리를 가리킬 경우 데이터 손실이 발생합니다. 실제로 활용되는 사례보다 인터뷰·교육에서 과도하게 소개되는 현상에 대한 비판입니다.

---

#### 9. DNS TXT 레코드 1,966개로 DOOM 실행

> 원본 기사: [https://blog.rice.is/post/doom-over-dns/](https://blog.rice.is/post/doom-over-dns/)

엔지니어 Adam Rice가 DOOM 게임 엔진 전체를 1,966개의 DNS TXT 레코드에 저장하고, 250줄짜리 PowerShell 스크립트로 실행하는 프로젝트를 공개했습니다. 게임 엔진과 WAD 파일을 1.7MB로 압축하고 1.2MB DLL과 함께 Base64로 인코딩하여 Cloudflare DNS TXT 레코드에 저장했습니다. 레코드 취득에 10~20초 소요되며 파일을 디스크에 저장하지 않고 메모리에서 직접 실행됩니다. 창의적인 해킹이면서 동시에 DNS가 멀웨어 페이로드 전달 채널로 악용될 수 있음을 보여주는 보안 시사점도 주목받았습니다.

---

#### 10. 고대 DNA로 밝혀진 서유라시아의 자연선택 가속화 (Nature)

> 원본 기사: [https://www.nature.com/articles/s41586-026-10358-1](https://www.nature.com/articles/s41586-026-10358-1)

Harvard 연구팀이 Nature에 발표한 연구로, 1만 5,836명의 서유라시아 고대 유전체(그 중 1만 16명은 신규 데이터)를 분석했습니다. 지난 1만 년간 479개 유전자 변이가 강한 방향성 선택을 받았으며, 농경 도입 이후 자연선택이 뚜렷하게 가속화된 것으로 나타났습니다. 선택된 유전자들은 면역, 피부색, 행동 등 다양한 형질과 관련되어 있습니다. 기존에는 자연선택이 드문 사건으로 여겨졌으나 이 연구는 그것이 매우 광범위하게 일어났음을 보여주는 획기적인 연구로 평가받고 있습니다.
