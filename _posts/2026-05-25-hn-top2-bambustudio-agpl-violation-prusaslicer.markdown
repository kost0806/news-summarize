---
title:  "[2026-05-25 / Top 2] BambuStudio, PrusaSlicer AGPL 라이선스 위반 4년 확인"
subtitle: "소프트웨어 자유 보존 위원회(SFC), Bambu Lab의 4년간 오픈소스 라이선스 위반을 공식 확인"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-25 12:01:00
source_url: "https://sfconservancy.org/news/2026/may/18/bambu-studio-3d-printer-agpl-violation-response/"
---

> 원본 기사: [https://sfconservancy.org/news/2026/may/18/bambu-studio-3d-printer-agpl-violation-response/](https://sfconservancy.org/news/2026/may/18/bambu-studio-3d-printer-agpl-violation-response/)

> HN 토론: [https://news.ycombinator.com/item?id=48245862](https://news.ycombinator.com/item?id=48245862)

### 개요

소프트웨어 자유 보존 위원회(Software Freedom Conservancy, SFC)가 Bambu Lab이 PrusaSlicer를 포크한 이후 4년간 AGPLv3 오픈소스 라이선스를 위반해왔음을 공식 확인했다.

### 주요 내용

SFC는 Bambu Lab의 위반 사항을 다음과 같이 정리했다:

1. **핵심 위반**: BambuStudio에는 `libbambu_networking`이라는 독점 폐쇄 소스 네트워킹 라이브러리가 포함되어 있으며, 이는 모든 클라우드 통신을 처리하지만 소스 코드가 공개되지 않는다. 이는 AGPL-3.0의 직접적인 위반이다.

2. **이중 위반**: Bambu가 OrcaSlicer 포크 개발자에게 법적 경고장을 발송한 것 자체도 AGPLv3 위반이다. AGPL 라이선스는 다른 사용자에게 추가적인 제한을 부과하는 것을 금지하기 때문이다.

3. **SFC의 대응**: SFC는 Bambu Lab의 독점 네트워킹 시스템을 대체할 오픈소스 솔루션을 구축하기 위한 **"baltobu"** 프로젝트에 자금을 지원하기로 발표했다.

### 오픈소스 라이선스의 중요성

AGPLv3는 네트워크를 통해 소프트웨어를 제공하는 경우에도 소스 코드를 공개해야 하는 "카피레프트" 라이선스다. Bambu는 PrusaSlicer(자체가 AGPLv3)에서 파생된 코드를 가져다 쓰면서도 네트워킹 스택을 비공개로 유지했다.

### 시사점

이 사건은 하드웨어 기업들이 오픈소스 소프트웨어를 상업적 이익을 위해 이용하면서도 그 의무를 이행하지 않는 행태에 대한 경각심을 일깨운다. SFC의 적극적인 개입과 "baltobu" 프로젝트는 기업의 라이선스 위반에 맞서는 오픈소스 커뮤니티의 새로운 전략이 될 수 있다.
