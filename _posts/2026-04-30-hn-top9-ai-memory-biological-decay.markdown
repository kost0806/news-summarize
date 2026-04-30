---
title:  "[2026-04-30 / Top 9] Show HN: 생물학적 감퇴를 적용한 AI 메모리 (52% 재현율)"
subtitle: "에빙하우스 망각 곡선을 AI 에이전트 메모리에 적용한 YourMemory MCP 서버"
author: "kost0806"
avatar: "img/posts/2026-04-30-yourmemory.png"
image: "img/posts/2026-04-30-yourmemory.png"
date:   2026-04-30 12:06:00
source_url: "https://github.com/sachitrafa/YourMemory"
---

> 원본 기사: [https://github.com/sachitrafa/YourMemory](https://github.com/sachitrafa/YourMemory)

### YourMemory: 인간처럼 기억하고 잊는 AI 메모리

**YourMemory**는 인간의 기억 메커니즘을 모방한 AI 에이전트용 영속 메모리 MCP 서버입니다. 핵심 아이디어는 단순합니다: 인간의 기억처럼, 중요하지 않은 정보는 자연스럽게 희미해지고 자주 참조되는 정보는 더 오래 유지되게 합니다.

#### 핵심 기술: 에빙하우스 망각 곡선

독일 심리학자 헤르만 에빙하우스가 발견한 **망각 곡선**을 AI 에이전트 메모리에 적용했습니다. 기억은 중요도와 회상 빈도에 따라 지수적으로 감퇴하며:

- **중요한 정보:** 오래 지속
- **덜 중요한 정보:** 자연스럽게 희미해짐
- **자주 회상되는 정보:** 강화되어 더 오래 유지
- **자동 24시간 감퇴 및 정리** 실행

#### 성능 벤치마크

- **LoCoMo 벤치마크:** recall@5 **59%** (Zep Cloud 대비 2배 이상)
- **LongMemEval-S:** recall-all@5 **85%**
- **Mem0 대비** LoCoMo에서 16pp 향상

#### 주요 기능

**하이브리드 검색:** 벡터 유사도 + BM25 키워드 검색 + 그래프 확장을 결합한 세 가지 검색 방식

**MCP 도구 3가지:**
- `recall_memory`: 관련 기억 검색
- `store_memory`: 새 기억 저장
- `update_memory`: 기존 기억 업데이트

**기술 스택:**
- DuckDB (벡터 저장)
- NetworkX/Neo4j (그래프)
- sentence-transformers (임베딩)
- spaCy (NLP)
- APScheduler (감퇴 작업)

**공간 컨텍스트 인식:** 파일 경로 기반으로 관련 기억을 우선 순위화

**브라우저 대시보드:** 메모리 시각화 내장

**설치:** 외부 데이터베이스 설정 없이 `pip install`만으로 동작

#### 사용 사례

AI 코딩 에이전트, 개인 AI 비서, 장기 프로젝트 관리 등 세션 간 컨텍스트 유지가 중요한 모든 AI 워크플로에 적합합니다. AI 에이전트가 "잊어버리지 않되, 불필요한 노이즈도 쌓지 않는" 균형잡힌 메모리 시스템을 제공합니다.
