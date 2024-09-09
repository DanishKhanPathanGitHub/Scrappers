import requests
from bs4 import BeautifulSoup

YOUTUBBE_URL =  "https://www.youtube.com/feed/trending"
response = requests.get(YOUTUBBE_URL)

print(response.status_code)

with open('trending.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page title:', doc.title.text)

video_divs = doc.find_all('div', class_='ytd-video-renderer')
print(f'Found {len(video_divs)} videos')