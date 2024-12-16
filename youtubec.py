import requests
import re

# YouTube 트렌딩 페이지 URL
TRENDING_URL = 'https://www.youtube.com/feed/trending'

# 헤더 설정 (유저 에이전트 포함)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


def get_shorts_video_urls():
    """트렌딩 페이지에서 Shorts 비디오 URL을 추출하는 함수"""
    # 트렌딩 페이지의 HTML 요청
    response = requests.get(TRENDING_URL, headers=headers)

    # 요청이 성공했는지 확인
    if response.status_code != 200:
        print(f"Error fetching the URL: {response.status_code}")
        return []

    # HTML 내용에서 Shorts 비디오 ID를 추출할 수 있는 정규식 패턴
    pattern = r'(v/|shorts/)([a-zA-Z0-9_-]+)'

    # 정규식으로 Shorts 비디오 ID를 추출
    shorts_video_ids = re.findall(pattern, response.text)

    # Shorts 비디오 URL 리스트 생성
    shorts_video_urls = [f"https://www.youtube.com/{prefix}{video_id}" for prefix, video_id in shorts_video_ids]

    return shorts_video_urls


def get_comments_from_video(video_url):
    """주어진 비디오 URL에서 댓글을 추출하는 함수"""
    # 비디오 페이지의 HTML 요청
    response = requests.get(video_url, headers=headers)

    # 요청이 성공했는지 확인
    if response.status_code != 200:
        print(f"Error fetching the video page: {response.status_code}")
        return []

    # 댓글을 포함하는 HTML 패턴 정의
    # 댓글은 ytd-comment-thread-renderer 태그 안에 존재합니다.
    comment_pattern = r'<ytd-comment-thread-renderer.*?>(.*?)</ytd-comment-thread-renderer>'

    # 정규식을 사용하여 댓글 부분을 추출
    comments = re.findall(comment_pattern, response.text, re.DOTALL)

    # 각 댓글에서 작성자와 내용을 추출할 수 있는 패턴
    author_pattern = r'<a.*?href="/@([a-zA-Z0-9_]+)"'
    text_pattern = r'<yt-pdg-comment-chip-renderer.*?>(.*?)</yt-pdg-comment-chip-renderer>'

    comment_data = []

    for comment in comments:
        # 댓글 작성자 추출
        author = re.search(author_pattern, comment)
        author = author.group(1) if author else "Unknown"

        # 댓글 내용 추출
        text = re.search(text_pattern, comment)
        text = text.group(1).strip() if text else "No text found"

        comment_data.append((author, text))

    return comment_data


def main():
    """메인 함수 - 트렌딩 Shorts 비디오에서 댓글 추출"""
    # 1. Shorts 비디오 URL 리스트 가져오기
    shorts_video_urls = get_shorts_video_urls()

    if not shorts_video_urls:
        print("No Shorts videos found.")
        return

    print(f"Found {len(shorts_video_urls)} Shorts videos.")

    # 2. 각 비디오에서 댓글 추출하기
    for video_url in shorts_video_urls:
        print(f"\nFetching comments from {video_url}...")
        comments = get_comments_from_video(video_url)

        if comments:
            print(f"Found {len(comments)} comments:")
            for author, text in comments:
                print(f"{author}: {text}")
        else:
            print("No comments found.")


if __name__ == '__main__':
    main()
