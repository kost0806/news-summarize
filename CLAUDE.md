# News Summarize - Jekyll Blog

이 프로젝트는 Jekyll 기반 GitHub Pages 블로그입니다. `main` 브랜치에 push하면 GitHub Actions가 자동으로 빌드 및 배포합니다.

배포 URL: https://kost0806.github.io/news-summarize/

## 새 포스트 추가 가이드

### 파일 위치 및 네이밍

포스트 파일은 `_posts/` 디렉토리에 아래 형식으로 생성합니다:

```
_posts/YYYY-MM-DD-slug-title.markdown
```

- `YYYY-MM-DD`: 포스트 날짜 (예: `2026-03-31`)
- `slug-title`: URL에 사용될 영문 소문자 슬러그, 단어는 `-`로 구분 (예: `ai-news-summary`)

### Front Matter (필수)

모든 포스트 파일 상단에 아래 YAML front matter를 반드시 포함해야 합니다:

```yaml
---
title:  "포스트 제목"
subtitle: "포스트 부제목 (카드에 표시됨)"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/posts/YYYY-MM-DD-slug.jpg"
date:   2026-03-31 12:00:00
---
```

#### 필드 설명

| 필드 | 필수 | 설명 |
|------|------|------|
| `title` | O | 포스트 제목. 큰따옴표로 감쌈 |
| `subtitle` | O | 부제목. 카드 썸네일에 제목 아래 표시됨 |
| `author` | O | 작성자 이름 |
| `avatar` | O | 작성자 아바타 이미지 경로. `"img/authors/kost0806.png"` 사용 |
| `image` | O | 카드 배경 이미지 경로. 요약 대상 링크의 대표 이미지(og:image)를 다운로드하여 `img/posts/` 디렉토리에 저장 후 해당 경로 지정 |
| `date` | O | `YYYY-MM-DD HH:MM:SS` 형식. 최신 날짜가 먼저 표시됨 |

### 이미지 설정

#### 아바타
- `"img/authors/kost0806.png"` 을 고정으로 사용합니다.

#### 카드 배경 이미지 (image)
- 요약 대상 뉴스 링크의 대표 이미지(og:image 메타태그)를 다운로드합니다.
- 다운로드한 이미지를 `img/posts/` 디렉토리에 `YYYY-MM-DD-slug.jpg` 형식으로 저장합니다.
- front matter의 `image` 필드에 해당 경로를 지정합니다. (예: `"img/posts/2026-03-31-ai-news.jpg"`)
- 대표 이미지를 가져올 수 없는 경우 기존 이미지(`img/a.jpg` ~ `img/f.jpg`) 중 하나를 사용합니다.

### 본문 작성

Front matter 아래에 마크다운으로 본문을 작성합니다. HTML도 사용 가능합니다.

```markdown
---
title:  "AI가 요약한 오늘의 뉴스"
subtitle: "2026년 3월 31일 주요 뉴스"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "img/posts/2026-03-31-ai-news-summary.jpg"
date:   2026-03-31 12:00:00
---

### 주요 뉴스 요약

오늘의 주요 뉴스를 정리했습니다.

#### 1. 첫 번째 뉴스 제목

뉴스 요약 내용...

#### 2. 두 번째 뉴스 제목

뉴스 요약 내용...
```

### 포스트 정렬

포스트는 `date` 필드 기준 최신순으로 정렬됩니다. 홈페이지에 카드 형태로 자동 표시됩니다.

### 배포

`main` 브랜치에 변경사항을 push하면 GitHub Actions(`.github/workflows/deploy.yml`)가 자동으로:
1. Jekyll 빌드 실행
2. GitHub Pages에 배포

별도의 배포 작업이 필요 없습니다.

### 주의사항

- front matter의 모든 문자열 값은 큰따옴표(`"`)로 감싸는 것을 권장합니다
- `date`가 미래 날짜이면 Jekyll 기본 설정에서 포스트가 표시되지 않을 수 있습니다
- 이미지 경로에 `{{ site.baseurl }}`을 포함하지 마세요. `index.html` 템플릿에서 자동으로 추가됩니다
- 파일 인코딩은 UTF-8을 사용합니다
