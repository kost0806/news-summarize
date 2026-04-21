#!/usr/bin/env python3
"""Fetch HN top 10 stories and create Jekyll blog posts with Korean summaries."""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

import anthropic

TODAY = datetime.now(timezone.utc).strftime('%Y-%m-%d')
POSTS_DIR = '_posts'
IMGS_DIR = 'img/posts'


def hn_get(path):
    url = f'https://hacker-news.firebaseio.com/v0/{path}'
    req = urllib.request.Request(url, headers={'User-Agent': 'news-summarize/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def get_existing_source_urls():
    urls = set()
    for fname in os.listdir(POSTS_DIR):
        if not fname.endswith('.markdown'):
            continue
        try:
            with open(os.path.join(POSTS_DIR, fname), encoding='utf-8') as f:
                for line in f:
                    m = re.search(r'source_url:\s*"([^"]+)"', line)
                    if m:
                        urls.add(m.group(1))
                        break
        except OSError:
            pass
    return urls


def fetch_text(url, max_chars=5000):
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (compatible; news-bot/1.0)'},
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            html = r.read().decode('utf-8', errors='ignore')
        text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text[:max_chars]
    except Exception as e:
        print(f'  Warning: Could not fetch article text: {e}')
        return ''


def get_og_image_url(url):
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (compatible; news-bot/1.0)'},
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            html = r.read().decode('utf-8', errors='ignore')
        for pat in [
            r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
            r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']',
        ]:
            m = re.search(pat, html)
            if m:
                return m.group(1)
    except Exception:
        pass
    return None


def download_image(img_url, dest_path):
    try:
        req = urllib.request.Request(
            img_url,
            headers={'User-Agent': 'Mozilla/5.0 (compatible; news-bot/1.0)'},
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read()
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


def claude_generate_post(client, title_en, story_url, article_text, score, num_comments):
    prompt = f"""당신은 Hacker News 기사를 한국어로 요약하는 전문 기자입니다.

다음 정보를 바탕으로 블로그 포스트를 작성해주세요:

**제목 (영어)**: {title_en}
**URL**: {story_url}
**HN 점수**: {score}점
**댓글 수**: {num_comments}개

**기사 본문** (일부):
{article_text if article_text else "(본문을 가져올 수 없어 제목과 URL을 바탕으로 작성해주세요)"}

다음을 작성해주세요:

1. **한국어 제목**: 영어 제목을 자연스러운 한국어로 번역 (원문의 의미를 살려서)
2. **부제목(subtitle)**: 한 문장으로 된 카드 요약 (50자 이내, 큰따옴표 없이)
3. **본문**: 마크다운 형식으로 다음 섹션 포함:
   - `### 개요` (2-3문장 요약)
   - `### 주요 내용` (핵심 내용)
   - `### 시사점` (독자에게 주는 인사이트)

기술 용어는 영어 병기. 전문적이고 명확한 한국어 사용.

반드시 다음 JSON 형식으로만 응답 (다른 텍스트 없이):
{{
  "title_ko": "...",
  "subtitle": "...",
  "body": "..."
}}"""

    response = client.messages.create(
        model='claude-opus-4-7',
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


def main():
    client = anthropic.Anthropic()

    os.makedirs(IMGS_DIR, exist_ok=True)

    print('Fetching HN top stories...')
    top_ids = hn_get('topstories.json')[:10]
    print(f'Top 10 IDs: {top_ids}')

    existing_urls = get_existing_source_urls()
    print(f'Existing source URLs: {len(existing_urls)}')

    created = 0
    for rank, story_id in enumerate(top_ids, 1):
        print(f'\n--- Rank {rank}: ID {story_id} ---')

        story = hn_get(f'item/{story_id}.json')
        if not story:
            print('  No story data, skipping')
            continue

        title_en = story.get('title', 'Untitled')
        story_url = story.get('url') or f'https://news.ycombinator.com/item?id={story_id}'
        score = story.get('score', 0)
        num_comments = story.get('descendants', 0)

        print(f'  Title: {title_en}')
        print(f'  URL: {story_url}')

        if story_url in existing_urls:
            print('  DUPLICATE - skipping')
            continue

        article_text = ''
        if story.get('url'):
            print('  Fetching article text...')
            article_text = fetch_text(story.get('url'))

        print('  Generating Korean summary with Claude...')
        title_ko, subtitle, body = claude_generate_post(
            client, title_en, story_url, article_text, score, num_comments
        )
        print(f'  Korean title: {title_ko}')

        slug = slugify(title_en)
        img_filename = f'{TODAY}-hn-top{rank}-{slug}.jpg'
        img_local_path = f'{IMGS_DIR}/{img_filename}'
        img_field = f'img/posts/{img_filename}'

        if story.get('url'):
            print('  Fetching og:image...')
            og_url = get_og_image_url(story.get('url'))
            if og_url:
                if not download_image(og_url, img_local_path):
                    img_field = 'img/default.jpg'
            else:
                img_field = 'img/default.jpg'
        else:
            img_field = 'img/default.jpg'

        filename = f'{TODAY}-hn-top{rank}-{slug}.markdown'
        post_date = f'{TODAY} {rank:02d}:00:00'
        subtitle_safe = subtitle.replace('"', '\\"')

        post_content = f'''---
title:  "[{TODAY} / Top {rank}] {title_ko}"
subtitle: "{subtitle_safe}"
author: "kost0806"
avatar: "img/authors/kost0806.png"
image: "{img_field}"
date:   {post_date}
source_url: "{story_url}"
---

> 원본 기사: [{story_url}]({story_url})

{body}
'''

        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(post_content)

        print(f'  Created: {filename}')
        created += 1

    print(f'\nDone! Created {created} new posts.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
