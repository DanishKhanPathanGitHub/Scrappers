from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_driver():
    service = Service(r"D:\Python\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", False)  # Keep browser open after script ends
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def get_videos(driver):
    YOUTUBE_URL = "https://www.youtube.com/feed/trending"
    driver.get(YOUTUBE_URL)
    videos = driver.find_elements(By.TAG_NAME, "ytd-video-renderer")
    return videos

def video_parser(video):
    title_tag = video.find_element(By.ID, 'video-title')
    title = title_tag.text
    url = title_tag.get_attribute('href')
    thumbnail = video.find_element(By.TAG_NAME, 'img').get_attribute('src')
    channel_name = video.find_element(By.CLASS_NAME, 'ytd-channel-name').text
    views = video.find_element(By.CLASS_NAME, 'inline-metadata-item').text

    return {
        "title":title,
        "url":url,
        "thumbnail":thumbnail,
        "channel":channel_name,
        "views":views,
    }

def main():
    driver = get_driver()
    videos = get_videos(driver)
    video_data = [video_parser(video) for video in videos[:10]]
    
    with open('video_data.txt', 'w', encoding='utf-8') as f:
        f.write(str(video_data))

    

if __name__=="__main__":
    main()
    

