#!/usr/bin/env python3
"""Fetch HN top 10 stories data and save as JSON with og:images. No AI translation needed."""

import json
import os
import re
import sys
import time
import urllib.request
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


def fetch_text_and_image(url):
    try:
        req = urllib.request.Request(
            url, headers={'User-Agent': 'Mozilla/5.0 (compatible; news-bot/1.0)'}
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
        return og_image, text[:5000]
    except Exception as e:
        print(f'  Warning: {e}')
        return None, ''


def download_image(img_url, dest_path):
    try:
        req = urllib.request.Request(
            img_url, headers={'User-Agent': 'Mozilla/5.0 (compatible; news-bot/1.0)'}
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


def main():
    os.makedirs(IMGS_DIR, exist_ok=True)

    print('Fetching HN top stories...')
    top_ids = hn_get('topstories.json')[:50]
    print(f'Fetched {len(top_ids)} story IDs')

    existing_urls, existing_hn_ids = get_existing_refs()
    print(f'Existing refs: {len(existing_urls)} URLs, {len(existing_hn_ids)} HN IDs')

    results = []
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

        if story_url in existing_urls or str(story_id) in existing_hn_ids:
            print(f'  Skipping duplicate: {title_en[:50]}')
            continue

        rank += 1
        score = story.get('score', 0)
        num_comments = story.get('descendants', 0)
        print(f'\nRank {rank}: {title_en[:60]} (score={score}, comments={num_comments})')

        og_image_url = None
        article_text = ''
        img_field = 'img/default.jpg'

        if article_url:
            og_image_url, article_text = fetch_text_and_image(article_url)

            if og_image_url:
                slug = slugify(title_en)
                img_filename = f'{TODAY}-hn-top{rank}-{slug}.jpg'
                img_local_path = f'{IMGS_DIR}/{img_filename}'
                if download_image(og_image_url, img_local_path):
                    img_field = f'img/posts/{img_filename}'
                    print(f'  Image saved: {img_filename}')

        results.append({
            'rank': rank,
            'id': story_id,
            'title': title_en,
            'url': article_url,
            'hn_url': hn_url,
            'story_url': story_url,
            'score': score,
            'descendants': num_comments,
            'by': story.get('by', ''),
            'article_text': article_text,
            'img_field': img_field,
        })

        time.sleep(0.3)

    output_path = 'hn_data.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({'date': TODAY, 'stories': results}, f, ensure_ascii=False, indent=2)

    print(f'\nSaved {len(results)} stories to {output_path}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
