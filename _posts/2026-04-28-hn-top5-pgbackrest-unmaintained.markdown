---
title:  "[2026-04-28 / Top 5] Pgbackrest, 유지보수 종료"
subtitle: "13년간 PostgreSQL 백업 솔루션으로 사용되어 온 pgBackRest 프로젝트가 아카이브 처리되었습니다"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-28 12:04:00
source_url: "https://github.com/pgbackrest/pgbackrest"
---

> 원본 기사: [https://github.com/pgbackrest/pgbackrest](https://github.com/pgbackrest/pgbackrest)

### 개요

PostgreSQL을 위한 대표적인 백업 및 복원 솔루션인 pgBackRest가 2026년 4월 27일부로 공식적으로 유지보수를 종료하고 저장소를 아카이브(읽기 전용)로 전환했습니다. 13년간 개발되어 왔으며 현재 최종 안정 릴리스는 2026년 1월에 출시된 v2.58.0입니다.

### 종료 이유

개발자 David Steele은 LinkedIn과 GitHub을 통해 공개한 성명에서 Crunchy Data가 매각된 이후 개인 자격으로 프로젝트를 유지하며 재정적으로 지속 가능한 자리를 찾으려 했지만 성공하지 못했다고 밝혔습니다. 스폰서십 확보 노력도 프로젝트 운영에 필요한 수준에 크게 못 미쳤다고 설명했습니다.

### 커뮤니티 반응

pgBackRest는 PostgreSQL 생태계에서 널리 사용되는 백업 솔루션이었기 때문에 커뮤니티의 충격이 큽니다. 현재 다음과 같은 대안들이 논의되고 있습니다:

- **Percona의 지원 지속:** Percona는 pgBackRest를 계속 지원하겠다고 밝혔으며, 다른 조직들과의 협력 구조를 논의 중입니다.
- **재단 기반 프로젝트 설립:** 독립적인 재단의 후원을 받는 프로젝트로 전환하는 방안
- **다중 벤더 관리 모델:** 여러 회사가 공동으로 유지보수를 담당하는 구조
- **PostgreSQL 코어 통합:** 핵심 기능을 PostgreSQL 생태계에 더 가깝게 이전하는 방안

### 마이그레이션 고려사항

pgBackRest를 현재 사용 중인 팀은 장기적인 대안을 검토해야 합니다. 주요 대안으로는 Barman, wal-g, pg_dump 등이 있으며, 각 솔루션의 기능 비교 및 마이그레이션 경로를 미리 파악해두는 것이 좋습니다.
