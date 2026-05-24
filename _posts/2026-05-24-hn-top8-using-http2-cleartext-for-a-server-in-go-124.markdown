---
title:  "[2026-05-24 / Top 8] Go 1.24 에서 서버에 HTTP/2 Cleartext 사용"
subtitle: "HN 36점 · 2개 댓글"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/posts/2026-05-24-hn-top8-using-http2-cleartext-for-a-server-in-go-124.jpg"
date:   2026-05-24 12:00:00
source_url: "https://www.clarityboss.com/blog/go-http2-cleartext-h2c-cloud-run"
---

> 원본 기사: [https://www.clarityboss.com/blog/go-http2-cleartext-h2c-cloud-run](https://www.clarityboss.com/blog/go-http2-cleartext-h2c-cloud-run)

> HN 토론: [https://news.ycombinator.com/item?id=48195698](https://news.ycombinator.com/item?id=48195698)

### 개요

Configuring a Go HTTP Server for Unencrypted HTTP/2 (h2c) | ClarityBoss Clarity Boss C B Home svg]:size-3.5"> Blog svg]:size-3.5"> Configuring a Go HTTP Server for Unencrypted HTTP/2 (h2c) Configuring a Go HTTP Server for Unencrypted HTTP/2 (h2c) Go 1.24 vastly simplified the configuration of a server that supports HTTP/2 cleartext, no longer requiring non-stdlib packages. I'll give a brief outline of how to enable HTTP/2 cleartext (h2c) in a Go API server when you are using Go 1.24 or newer. This is useful in Cloud Run environments, which handles TLS termination but can take advantage of HTTP/2 features. Dan McGee • May 18, 2026 Engineering In our application, we use long-lived server-sent event streams (SSE). These are set up to have a really long timeout and lifetime - 15 minutes in our...

### 주요 내용

원문 기사 링크를 통해 전체 내용을 확인할 수 있습니다.

- **HN 점수**: 36점
- **댓글 수**: 2개
- **원문**: [https://www.clarityboss.com/blog/go-http2-cleartext-h2c-cloud-run](https://www.clarityboss.com/blog/go-http2-cleartext-h2c-cloud-run)

### HN 커뮤니티 반응

HN 점수 36점, 댓글 2개로 커뮤니티의 높은 관심을 받은 글입니다.
HN 토론 링크에서 전체 댓글을 확인하세요.

### 시사점

Hacker News 커뮤니티가 주목한 이슈입니다. 원문과 HN 토론을 함께 읽어보시길 권장합니다.
