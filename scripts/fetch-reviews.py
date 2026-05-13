#!/usr/bin/env python3
"""
Fetches Google Reviews for Mr Mechanical LP via the Places API and writes
them to content/testimonials.json.

Required environment variables (set as GitHub Actions secrets):
  GOOGLE_PLACES_API_KEY  — Google Cloud API key with Places API enabled
  GOOGLE_PLACE_ID        — Google Place ID for the business listing

If either variable is missing the script exits cleanly without touching the
existing JSON file, so the site continues to show whatever reviews are already
there while the credentials are being set up.
"""

import json
import os
import sys
import urllib.request
import urllib.error

API_KEY  = os.environ.get('GOOGLE_PLACES_API_KEY', '').strip()
PLACE_ID = os.environ.get('GOOGLE_PLACE_ID', '').strip()
OUTPUT   = 'content/testimonials.json'
MIN_STARS = 4   # Only include reviews at or above this rating

if not API_KEY or not PLACE_ID:
    print("GOOGLE_PLACES_API_KEY or GOOGLE_PLACE_ID not set — skipping sync.")
    sys.exit(0)

url = (
    'https://maps.googleapis.com/maps/api/place/details/json'
    f'?place_id={PLACE_ID}'
    '&fields=reviews'
    f'&key={API_KEY}'
)

try:
    with urllib.request.urlopen(url, timeout=15) as resp:
        data = json.loads(resp.read().decode())
except urllib.error.URLError as e:
    print(f"Network error fetching reviews: {e}")
    sys.exit(0)

status = data.get('status')
if status != 'OK':
    print(f"Places API returned status '{status}' — skipping sync.")
    sys.exit(0)

raw_reviews = data.get('result', {}).get('reviews', [])
if not raw_reviews:
    print("No reviews returned — skipping sync.")
    sys.exit(0)

items = []
for r in raw_reviews:
    rating = r.get('rating', 0)
    text   = (r.get('text') or '').strip()
    if rating < MIN_STARS or not text:
        continue
    items.append({
        'name':  r.get('author_name', 'Google Reviewer'),
        'city':  '',          # Google Places API does not expose reviewer city
        'quote': text,
        'stars': int(rating),
    })

if not items:
    print("No qualifying reviews found — skipping sync.")
    sys.exit(0)

output = {'items': items}

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root  = os.path.dirname(script_dir)
out_path   = os.path.join(repo_root, OUTPUT)

with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
    f.write('\n')

print(f"Wrote {len(items)} review(s) to {OUTPUT}")
