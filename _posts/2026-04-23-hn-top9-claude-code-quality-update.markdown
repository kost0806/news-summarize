---
title:  "[2026-04-23 / Top 9] Claude Code 품질 보고에 관한 최근 업데이트"
subtitle: "Anthropic이 Claude Code, Claude Agent SDK, Claude Cowork에 영향을 미친 세 가지 별도의 변경사항을 추적했습니다."
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-23 17:00:00
source_url: "https://www.anthropic.com/engineering/april-23-postmortem"
---

> 원본 기사: [https://www.anthropic.com/engineering/april-23-postmortem](https://www.anthropic.com/engineering/april-23-postmortem)

### 품질 저하의 원인

3월 4일, Claude Code의 기본 reasoning 난이도를 높음에서 중간으로 변경하여 UI가 멈춘 것처럼 보이는 긴 지연 시간을 줄였습니다. 사용자들은 Claude Code가 덜 똑똑해졌다고 보도했고, Anthropic은 4월 7일 이 결정을 반대했습니다.

3월 26일, 기능 개선으로 의도된 변경을 적용했는데, prompt caching을 사용하여 API 호출을 더 저렴하고 빠르게 만들려 했습니다. 이 버그는 모서리 사례(오래된 세션)에서만 발생하고 문제를 재현하기 어려워 근본 원인을 발견하고 확인하는 데 일주일 이상 걸렸습니다.

4월 16일, 말의 장황함을 줄이기 위해 system prompt 명령어를 추가했지만, 다른 prompt 변경사항과 결합되어 코딩 품질을 손상시켰고 4월 20일에 되돌렸습니다.

### 조치 및 개선사항

모든 세 가지 문제는 4월 20일(v2.1.116)을 기준으로 해결되었습니다. 4월 23일 현재, 모든 구독자의 사용 제한을 재설정하고 있습니다. Anthropic은 이제 모든 system prompt 변경에 대해 더 광범위한 모델별 평가를 실행하며, 새 도구를 구축하여 prompt 변경사항을 감시하고 모델별 변경사항을 엄격하게 관리합니다.
