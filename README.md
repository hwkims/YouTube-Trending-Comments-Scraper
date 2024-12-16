# YouTube-Trending-Comments-Scraper
![image](https://github.com/user-attachments/assets/a7b41298-78ea-40f2-a766-ccf3f2f6c6ff)
Here's a **README.md** file template for your project:

```markdown
# YouTube Trending Comments Scraper

This project uses **Selenium** to scrape comments from YouTube's trending page. It dynamically loads video URLs from the trending section and extracts the comments for each video.

## Features

- Scrapes the trending YouTube page for video links.
- Navigates to each video and extracts the comments.
- Extracts the text of each comment and prints it out.

## Requirements

Before running the project, ensure that you have the following dependencies installed:

- Python 3.x
- **Selenium**
- **WebDriver Manager** (for automatic WebDriver installation)

You can install the required Python packages by running the following command:

```bash
pip install selenium webdriver-manager
```

## Setup

### 1. Install Dependencies

Ensure you have the necessary libraries installed:

```bash
pip install selenium webdriver-manager
```

### 2. WebDriver Installation

This script uses **Chrome WebDriver**, and it automatically installs the appropriate version of the driver using the `webdriver-manager` library.

### 3. Running the Script

To start the script, run the following command:

```bash
python youtube_trending_comments.py
```

This will:
- Scrape the YouTube trending page for video links.
- Extract and print the comments from each video.

## Code Explanation

### `get_video_urls()`
- This function loads the YouTube Trending page and extracts video URLs.
- It uses Selenium to interact with the page, waiting for it to load completely before scraping the video links.

### `get_comments_from_video(video_url)`
- This function navigates to a specific YouTube video page and extracts the comments.
- It uses Selenium to interact with the page and waits for the comments section to load before scraping the comment texts.

### `main()`
- The main function calls the above functions to scrape the trending page and fetch comments from each video.

## Notes

- **Dynamic Loading**: Since YouTube loads content dynamically (e.g., comments and video links), this script uses Selenium to interact with the page and wait for elements to load before extracting the necessary information.
- **Rate Limiting**: Be cautious when scraping too many pages in a short period to avoid rate-limiting from YouTube.
- **Headless Mode**: If you prefer not to open a browser window, you can configure Selenium to run in headless mode by adding options like `--headless` to the `webdriver.Chrome()` call.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Selenium** for automating the browser interaction.
- **WebDriver Manager** for automatically managing the Chrome WebDriver version.
```

### Notes on the README:

1. **Installation Instructions**: It includes the necessary dependencies and how to install them via `pip`.
2. **Project Explanation**: A description of what the script does and how it works.
3. **Code Breakdown**: A brief breakdown of the important functions in the script to help users understand the logic.
4. **Running Instructions**: Clear instructions on how to run the script.
5. **Additional Notes**: Important points such as dynamic loading of content and headless mode usage are mentioned.
6. **License**: A placeholder for the license if applicable.

Let me know if you'd like to adjust or add anything specific!
