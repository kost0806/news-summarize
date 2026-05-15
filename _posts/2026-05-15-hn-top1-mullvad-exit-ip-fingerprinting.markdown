---
title:  "[2026-05-15 / Top 1] Mullvad 출구 IP는 놀랍도록 신원 식별이 가능하다"
subtitle: "VPN을 사용해도 출구 IP만으로 사용자를 추적할 수 있다는 연구 결과"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-05-15 12:00:00
source_url: "https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/"
---

> 원본 기사: [https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/](https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/)

> HN 토론: [https://news.ycombinator.com/item?id=48143880](https://news.ycombinator.com/item?id=48143880)

### Mullvad VPN 출구 IP, 핑거프린팅 벡터로 활용 가능

프라이버시 중심 VPN 서비스인 Mullvad의 출구 IP 주소가 예상보다 훨씬 강력한 사용자 식별 수단이 될 수 있다는 연구 결과가 공개됐다. 이 글은 Mullvad의 출구 IP 주소 분배 방식을 분석해, 개별 사용자를 높은 확률로 식별(fingerprinting)하는 것이 가능함을 실증적으로 보여준다.

#### 문제의 핵심: 출구 IP 분배 패턴

VPN은 사용자의 실제 IP 주소를 숨기기 위해 서버의 출구 IP를 공유한다. 그러나 Mullvad는 특정 서버 노드에 연결된 사용자들이 시간대별로 비교적 일관된 출구 IP 집합을 사용하도록 설계되어 있다. 연구자는 이 패턴을 역이용하면 사이트가 방문자의 출구 IP만을 보고도 해당 사용자가 특정 Mullvad 노드를 사용한다는 사실, 나아가 시간적 상관관계 분석을 통해 동일 사용자임을 추론할 수 있다고 주장한다.

#### 핑거프린팅 벡터로서의 VPN 출구 IP

일반적으로 핑거프린팅은 브라우저 특성(User-Agent, Canvas, 글꼴 목록 등)을 활용하지만, 이 연구는 VPN 출구 IP 자체가 준-고유(quasi-unique) 식별자로 기능할 수 있음을 보인다. Mullvad 서버의 수가 제한적이고 각 서버에 동시 연결되는 사용자 수도 유한하기 때문에, 동일한 출구 IP를 반복적으로 사용하는 패턴이 사용자를 연결하는 데 충분한 엔트로피를 제공한다.

#### HN 커뮤니티의 반응

106개 댓글이 달리며 활발한 토론이 이루어졌다. 커뮤니티에서는 멀티홉 VPN 구성이나 Tor 조합 사용이 이 문제를 완화할 수 있는지, Mullvad 측의 대응 방안은 무엇인지에 대한 논의가 이어졌다. 일부는 이 문제가 Mullvad만의 문제가 아니라 대부분의 VPN 서비스에 공통적으로 적용되는 구조적 한계라고 지적했다.

#### 시사점

이 연구는 VPN이 프라이버시를 완전히 보장하지 않는다는 사실을 다시 한번 상기시킨다. 고도의 프라이버시를 원하는 사용자라면 단순한 VPN 사용을 넘어 Tor, 멀티홉 구성, 또는 정기적인 서버 교체 등의 추가적인 조치를 고려해야 한다.
