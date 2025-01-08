from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

def scrape_twitter(username):
   
    driver = webdriver.Chrome() 
    driver.get(f"https://twitter.com/{username}")
    time.sleep(5) 

   
    for _ in range(3):  
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

   
    tweets = []
    for tweet in soup.find_all("article"):
        content = tweet.find("div", attrs={"data-testid": "tweetText"})
        timestamp_tag = tweet.find("time")
        timestamp = timestamp_tag["datetime"] if timestamp_tag else "No timestamp"
        tweet_text = content.get_text(strip=True) if content else "No content"
        tweets.append({"timestamp": timestamp, "content": tweet_text})

    return tweets

if __name__ == "__main__":
    username = input("Enter Twitter username: ")
    try:
        data = scrape_twitter(username)
        for idx, tweet in enumerate(data, start=1):
            print(f"Tweet {idx}:")
            print(f"Timestamp: {tweet['timestamp']}")
            print(f"Content: {tweet['content']}")
            print("-" * 30)
    except Exception as e:
        print(f"An error occurred: {e}")
