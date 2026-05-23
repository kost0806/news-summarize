---
title:  "[2026-05-23 / Top 10] Elixir에서의 최고 무작위 가중치 해싱"
subtitle: "HN 35점 · 0개 댓글"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-23 12:09:00
source_url: "https://jola.dev/posts/highest-random-weight-in-elixir"
---

> 원본 기사: [https://jola.dev/posts/highest-random-weight-in-elixir](https://jola.dev/posts/highest-random-weight-in-elixir)

> HN 토론: [https://news.ycombinator.com/item?id=48222492](https://news.ycombinator.com/item?id=48222492)

### 개요

Elixir에서 일관성 해싱(consistent hashing)의 대안으로 최고 무작위 가중치(HRW, Highest Random Weight) 또는 랑데부 해싱(Rendezvous Hashing)을 구현하는 방법을 소개합니다. Discord의 ExHashRing과의 성능 비교 및 최적화 전략까지 담고 있습니다.

### 주요 내용

- **HRW 기본 원리**: 각 키와 노드를 함께 해시하여 가장 높은 점수를 받은 노드에 키를 할당하는 상태 비저장(stateless) 알고리즘
- **최소 구현 예시**:
  ```elixir
  defmodule HRW do
    def owner(key, nodes) do
      Enum.max_by(nodes, fn node -> :erlang.phash2({key, node}) end)
    end
  end
  ```
- **ExHashRing 비교**: Discord의 ExHashRing은 가장 널리 쓰이는 일관성 해시 구현체지만, HRW는 훨씬 단순하고 별도 프로세스 불필요
- **성능**: 기본 HRW는 O(n) 복잡도이지만 소수 노드에서는 ExHashRing과 성능 차이 미미
- **Skeleton 최적화**: O(log n)으로 개선하는 방법 소개 — 10,000개 노드에서도 ExHashRing의 약 3배 수준

### HN 커뮤니티 반응

HN 점수 35점, 댓글 없음. 간결하고 명확한 기술 글로 조용히 주목받은 사례입니다.

### 시사점

분산 시스템에서 키-노드 매핑이 필요할 때 복잡한 라이브러리 없이도 구현 가능한 우아한 알고리즘입니다. Elixir 사용자뿐 아니라 분산 시스템 설계에 관심 있는 개발자 모두에게 유용한 개념입니다.
