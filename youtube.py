import requests
import re

# YouTube 트렌딩 페이지 URL
url = 'https://www.youtube.com/feed/trending'

# 헤더 설정 (유저 에이전트 포함)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 트렌딩 페이지의 HTML 요청
response = requests.get(url, headers=headers)

# 요청이 성공했는지 확인
if response.status_code != 200:
    print(f"Error fetching the URL: {response.status_code}")
    exit()

# HTML 내용에서 Shorts 비디오 ID를 추출할 수 있는 정규식 패턴
# "vi/{videoId}" 패턴을 찾아 Shorts 비디오 ID를 추출합니다.
pattern = r'vi/([a-zA-Z0-9_-]+)'

# 정규식으로 Shorts 비디오 ID를 추출
shorts_video_ids = re.findall(pattern, response.text)

# Shorts 비디오 URL 출력
if shorts_video_ids:
    print("Found Shorts videos:")
    for video_id in shorts_video_ids:
        video_url = f"https://www.youtube.com/v/{video_id}"
        print(video_url)
else:
    print("No Shorts videos found.")
