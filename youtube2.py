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

# HTML 내용에서 일반 비디오 ID를 추출할 수 있는 정규식 패턴
# "watch?v={videoId}" 패턴을 찾아 일반 비디오 ID를 추출합니다.
pattern = r'watch\?v=([a-zA-Z0-9_-]+)'

# 정규식으로 비디오 ID를 추출
video_ids = re.findall(pattern, response.text)

# 일반 비디오 URL 출력
if video_ids:
    print("Found regular videos:")
    for video_id in video_ids:
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        print(video_url)
else:
    print("No regular videos found.")
