---
title:  "코드 읽기 전에 실행하는 Git 명령어들"
subtitle: "2262 포인트를 받은 HN 1위: 새 코드베이스의 건강 상태를 파악하는 5가지 git 진단 명령어"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/default.jpg"
date:   2026-04-16 09:00:00
source_url: "https://piechowski.io/post/git-commands-before-reading-code/"
---

> 원본 기사: [https://piechowski.io/post/git-commands-before-reading-code/](https://piechowski.io/post/git-commands-before-reading-code/)

### 개요

Ally Piechowski가 작성한 이 글은 Hacker News에서 **2,262 포인트**를 획득하며 이번 주 최고 인기 포스트로 등극했습니다. 새로운 코드베이스를 처음 접할 때, 파일을 직접 열기 전에 git 히스토리를 통해 "어디가 아픈지"를 파악하는 5가지 진단 명령어를 소개합니다.

### 1. 가장 많이 변경된 파일 찾기 (Churn Hotspot)

```bash
git log --format=format: --name-only --since="1 year ago" \
  | sort | uniq -c | sort -nr | head -20
```

최근 1년간 가장 많이 변경된 파일 20개를 보여줍니다. 맨 위에 있는 파일이 거의 항상 "경고가 많이 붙은 파일"입니다. 변경 빈도가 높다는 것은 해당 파일이 지속적으로 수정되어야 하거나 설계 문제를 안고 있다는 신호입니다.

### 2. 버스 팩터(Bus Factor) 확인

```bash
# 전체 기여자 비율
git shortlog -sn --no-merges | head -10

# 최근 6개월 기여자 비율
git shortlog -sn --no-merges --since="6 months ago" | head -10
```

한 명이 전체 커밋의 60% 이상을 담당하고 있다면 버스 팩터 1 — 그 사람이 6개월 전에 떠났다면 위기입니다. 전체 shortlog의 최다 기여자가 최근 6개월 창에 보이지 않으면 즉시 클라이언트에게 알립니다.

### 3. 버그 밀집 파일 찾기

```bash
git log --oneline --all | grep -iE "fix|bug|hotfix|patch|issue" \
  | awk '{print $1}' \
  | xargs -I{} git diff-tree --no-commit-id -r --name-only {} \
  | sort | uniq -c | sort -nr | head -20
```

"fix", "bug" 등의 키워드가 포함된 커밋들에서 자주 등장하는 파일을 추려냅니다. **고 변경(churn) + 고 버그** 파일이 가장 큰 리스크입니다.

### 4. 위기 패턴 탐지

```bash
git log --format="%ad %s" --date=short | \
  awk '{print $1}' | sort | uniq -c | sort -nr | head -20
```

특정 날짜에 커밋이 폭발적으로 증가한 날은 "사고의 날"일 가능성이 높습니다. 릴리즈 전날 밤 또는 인시던트 대응 시 발생하는 급격한 커밋 급증 패턴을 잡아냅니다.

### 5. 오래된 TODO·FIXME 파악

```bash
git log -S "TODO\|FIXME" --oneline --diff-filter=A \
  | awk '{print $1}' \
  | xargs git show --stat 2>/dev/null | grep -E "TODO|FIXME|\.py|\.js|\.go" \
  | head -30
```

처음 추가된 이후 한 번도 해결되지 않은 TODO/FIXME가 집중된 파일을 확인합니다. 기술 부채의 위치를 빠르게 파악할 수 있습니다.

### 활용 방법

저자는 새 프로젝트를 시작할 때마다 이 명령어들을 실행해 코드를 읽기 전에 다음 질문에 답한다고 합니다:

- 어떤 파일이 가장 많이 바뀌는가?
- 해당 지식을 한 사람이 독점하고 있지는 않은가?
- 버그가 반복해서 생기는 영역은 어디인가?
- 언제 위기가 있었는가?
- 기술 부채는 어디에 쌓여 있는가?

코드 리뷰나 컨설팅 첫날에 이 진단만 해도 "어디부터 봐야 하는가"를 명확히 알 수 있습니다.

### HN 반응

이 포스트는 HN에서 487개 댓글을 받았으며 커뮤니티는 `git blame`을 활용한 저자 분석, `git log --follow`를 통한 파일 이름 변경 추적, `tokei`나 `cloc` 조합 등 다양한 추가 팁을 공유했습니다.
