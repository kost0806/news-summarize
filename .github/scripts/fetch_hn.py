#!/usr/bin/env python3
"""Fetch HN top 10 stories and create Jekyll blog posts with Korean summaries.

If ANTHROPIC_API_KEY is set, uses Claude for full Korean summaries.
Otherwise falls back to MyMemory translation API + structured excerpt posts.
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse
from datetime import datetime, timezone

TODAY = datetime.now(timezone.utc).strftime('%Y-%m-%d')
POSTS_DIR = '_posts'
IMGS_DIR = 'img/posts'
HN_ITEM_BASE = 'https://news.ycombinator.com/item?id='


def hn_get(path):
    url = f'https://hacker-news.firebaseio.com/v0/{path}'
    req = urllib.request.Request(url, headers={'User-Agent': 'news-summarize/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def get_existing_refs():
    source_urls = set()
    hn_ids = set()
    for fname in os.listdir(POSTS_DIR):
        if not fname.endswith('.markdown'):
            continue
        try:
            with open(os.path.join(POSTS_DIR, fname), encoding='utf-8') as f:
                content = f.read()
            for m in re.finditer(r'source_url:\s*"([^"]+)"', content):
                source_urls.add(m.group(1))
            for m in re.finditer(r'news\.ycombinator\.com/item\?id=(\d+)', content):
                hn_ids.add(m.group(1))
        except OSError:
            pass
    return source_urls, hn_ids


def fetch_page(url, max_chars=6000):
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (compatible; news-bot/1.0)'},
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            html = r.read().decode('utf-8', errors='ignore')

        og_image = None
        for pat in [
            r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
            r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']',
            r'<meta[^>]+name=["\']twitter:image["\'][^>]+content=["\']([^"\']+)["\']',
        ]:
            m = re.search(pat, html, re.IGNORECASE)
            if m:
                og_image = m.group(1)
                if og_image.startswith('//'):
                    og_image = 'https:' + og_image
                break

        text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return og_image, text[:max_chars]
    except Exception as e:
        print(f'  Warning: Could not fetch page: {e}')
        return None, ''


def download_image(img_url, dest_path):
    try:
        req = urllib.request.Request(
            img_url,
            headers={'User-Agent': 'Mozilla/5.0 (compatible; news-bot/1.0)'},
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read()
        if len(data) < 500:
            return False
        with open(dest_path, 'wb') as f:
            f.write(data)
        return True
    except Exception as e:
        print(f'  Warning: Could not download image: {e}')
        return False


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text[:50]


def translate_mymemory(text):
    """Translate English to Korean using MyMemory free API."""
    try:
        encoded = urllib.parse.quote(text[:500])
        url = f'https://api.mymemory.translated.net/get?q={encoded}&langpair=en|ko'
        req = urllib.request.Request(url, headers={'User-Agent': 'news-bot/1.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        if data.get('responseStatus') == 200:
            translated = data['responseData']['translatedText']
            if translated and translated != text:
                return translated
    except Exception as e:
        print(f'  Warning: MyMemory translation failed: {e}')
    return text


def claude_generate_post(client, title_en, story_url, hn_url, article_text, score, num_comments):
    prompt = f"""당신은 Hacker News 기사를 한국어로 요약하는 전문 기자입니다.

다음 정보를 바탕으로 블로그 포스트를 작성해주세요:

**제목 (영어)**: {title_en}
**URL**: {story_url}
**HN 링크**: {hn_url}
**HN 점수**: {score}점
**댓글 수**: {num_comments}개

**기사 본문** (일부):
{article_text if article_text else "(본문을 가져올 수 없어 제목과 URL을 바탕으로 작성해주세요)"}

다음을 작성해주세요:

1. **한국어 제목**: 영어 제목을 자연스러운 한국어로 번역 (원문의 의미를 살려서)
2. **부제목(subtitle)**: 한 문장으로 된 카드 요약 (50자 이내, 큰따옴표 없이)
3. **본문**: 마크다운 형식으로 다음 섹션 포함:
   - `### 개요` (2-3문장 요약)
   - `### 주요 내용` (핵심 내용을 소제목과 함께 상세히)
   - `### HN 커뮤니티 반응` ({score}점, {num_comments}개 댓글 언급 및 주요 토론 포인트)
   - `### 시사점` (독자에게 주는 인사이트)

기술 용어는 영어 병기. 전문적이고 명확한 한국어 사용.
본문에 원본 링크나 HN 링크는 포함하지 마세요 (별도로 추가됨).

반드시 다음 JSON 형식으로만 응답 (다른 텍스트 없이):
{{
  "title_ko": "...",
  "subtitle": "...",
  "body": "..."
}}"""

    response = client.messages.create(
        model='claude-opus-4-8',
        max_tokens=2000,
        messages=[{'role': 'user', 'content': prompt}],
    )

    text = response.content[0].text.strip()
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        try:
            data = json.loads(json_match.group())
            return (
                data.get('title_ko', title_en),
                data.get('subtitle', ''),
                data.get('body', ''),
            )
        except json.JSONDecodeError:
            pass

    return title_en, '', text


def simple_generate_post(title_en, story_url, hn_url, article_text, score, num_comments):
    """Generate a post without AI: translate title via MyMemory, build structured body."""
    title_ko = translate_mymemory(title_en)
    subtitle = f"HN {score}점 · {num_comments}개 댓글"

    excerpt = ''
    if article_text:
        sentences = re.split(r'(?<=[.!?])\s+', article_text.strip())
        excerpt = ' '.join(sentences[:5]).strip()
        if len(excerpt) > 800:
            excerpt = excerpt[:800] + '...'

    body = f"""### 개요

{excerpt if excerpt else "원문 기사를 참고해주세요."}

### 주요 내용

원문 기사 링크를 통해 전체 내용을 확인할 수 있습니다.

- **HN 점수**: {score}점
- **댓글 수**: {num_comments}개
- **원문**: [{story_url}]({story_url})

### HN 커뮤니티 반응

HN 점수 {score}점, 댓글 {num_comments}개로 커뮤니티의 높은 관심을 받은 글입니다.
HN 토론 링크에서 전체 댓글을 확인하세요.

### 시사점

Hacker News 커뮤니티가 주목한 이슈입니다. 원문과 HN 토론을 함께 읽어보시길 권장합니다."""

    return title_ko, subtitle, body


def main():
    api_key = os.environ.get('ANTHROPIC_API_KEY', '')
    use_claude = bool(api_key)

    if use_claude:
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            print('Using Claude API for Korean summaries.')
        except ImportError:
            print('anthropic package not installed, falling back to simple mode.')
            use_claude = False
            client = None
    else:
        print('ANTHROPIC_API_KEY not set — using MyMemory translation + excerpt mode.')
        client = None

    os.makedirs(IMGS_DIR, exist_ok=True)

    print('Fetching HN top stories...')
    top_ids = hn_get('topstories.json')[:50]
    print(f'Fetched {len(top_ids)} story IDs')

    existing_urls, existing_hn_ids = get_existing_refs()
    print(f'Existing refs: {len(existing_urls)} source URLs, {len(existing_hn_ids)} HN IDs')

    created = 0
    rank = 0
    for story_id in top_ids:
        if rank >= 10:
            break

        story = hn_get(f'item/{story_id}.json')
        if not story or story.get('type') not in ('story', 'job', 'poll'):
            continue

        title_en = story.get('title', 'Untitled')
        article_url = story.get('url', '')
        hn_url = f'{HN_ITEM_BASE}{story_id}'
        story_url = article_url or hn_url
        score = story.get('score', 0)
        num_comments = story.get('descendants', 0)

        if story_url in existing_urls or str(story_id) in existing_hn_ids:
            print(f'  Skipping duplicate: {title_en[:60]}')
            continue

        rank += 1
        print(f'\nRank {rank}: {title_en[:70]} (score={score}, comments={num_comments})')

        og_image_url, article_text = None, ''
        if article_url:
            og_image_url, article_text = fetch_page(article_url)

        if use_claude:
            title_ko, subtitle, body = claude_generate_post(
                client, title_en, story_url, hn_url, article_text, score, num_comments
            )
        else:
            title_ko, subtitle, body = simple_generate_post(
                title_en, story_url, hn_url, article_text, score, num_comments
            )
            time.sleep(0.5)  # respect MyMemory rate limit

        print(f'  Korean title: {title_ko}')

        slug = slugify(title_en)
        img_filename = f'{TODAY}-hn-top{rank}-{slug}.jpg'
        img_local_path = f'{IMGS_DIR}/{img_filename}'
        img_field = 'img/default.jpg'

        if og_image_url:
            if download_image(og_image_url, img_local_path):
                img_field = f'img/posts/{img_filename}'
                print(f'  Image saved: {img_filename}')

        if article_url:
            links_block = (
                f'> 원본 기사: [{article_url}]({article_url})\n'
                f'\n'
                f'> HN 토론: [{hn_url}]({hn_url})'
            )
        else:
            links_block = f'> HN 토론: [{hn_url}]({hn_url})'

        subtitle_safe = subtitle.replace('"', '\\"')
        filename = f'{TODAY}-hn-top{rank}-{slug}.markdown'
        post_content = f'''---
title:  "[{TODAY} / Top {rank}] {title_ko}"
subtitle: "{subtitle_safe}"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "{img_field}"
date:   {TODAY} 12:00:00
source_url: "{story_url}"
---

{links_block}

{body}
'''

        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(post_content)

        print(f'  Created: {filename}')
        created += 1
        time.sleep(0.3)

    print(f'\nDone! Created {created} new posts.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
