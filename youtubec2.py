import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 헤더 설정 (유저 에이전트 포함)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

def get_video_urls():
    """트렌딩 페이지에서 일반 비디오 URL을 추출하는 함수"""
    # Selenium을 사용하여 동적으로 페이지를 로드
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.youtube.com/feed/trending')

    # 페이지가 로드될 때까지 잠시 대기
    time.sleep(3)  # 대기시간을 조정할 수 있습니다

    # 트렌딩 비디오 링크 추출
    video_urls = []
    video_elements = driver.find_elements(By.XPATH, '//a[@id="video-title"]')
    for video in video_elements:
        video_urls.append(video.get_attribute('href'))

    driver.quit()
    return video_urls


def get_comments_from_video(video_url):
    """주어진 비디오 URL에서 댓글을 추출하는 함수"""
    # Selenium을 사용하여 비디오 페이지 로드
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(video_url)

    # 페이지가 로드될 때까지 잠시 대기
    time.sleep(5)  # 페이지 로드 후 충분한 시간 대기

    # 댓글 부분이 로드될 때까지 대기 (최대 20초)
    driver.implicitly_wait(20)

    # 댓글 내용 추출
    comments = []
    comment_elements = driver.find_elements(By.XPATH, '//span[@class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"]')

    for comment_element in comment_elements:
        comment_text = comment_element.text.strip()
        if comment_text:
            comments.append(comment_text)

    driver.quit()
    return comments


def main():
    """메인 함수 - 트렌딩 일반 비디오에서 댓글 추출"""
    # 1. 일반 비디오 URL 리스트 가져오기
    video_urls = get_video_urls()

    if not video_urls:
        print("No regular videos found.")
        return

    print(f"Found {len(video_urls)} regular videos.")

    # 2. 각 비디오에서 댓글 추출하기
    for video_url in video_urls:
        print(f"\nFetching comments from {video_url}...")
        comments = get_comments_from_video(video_url)

        if comments:
            print(f"Found {len(comments)} comments:")
            for comment in comments:
                print(comment)
        else:
            print("No comments found.")


if __name__ == '__main__':
    main()
