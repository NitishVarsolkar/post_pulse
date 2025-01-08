from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

def scrape_instagram(username):
    driver = webdriver.Chrome()  
    driver.get(f"https://www.instagram.com/{username}/")
    time.sleep(5) 

    
    for _ in range(3): 
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

   
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

  
    posts = []
    for post in soup.find_all("div", class_="v1Nh3"):
        link = post.find("a")["href"]
        img_tag = post.find("img")
        image_url = img_tag["src"] if img_tag else None
        caption = img_tag["alt"] if img_tag else "No caption"
        posts.append({"link": f"https://www.instagram.com{link}", "image_url": image_url, "caption": caption})

    return posts

if __name__ == "__main__":
    username = input("Enter Instagram username: ")
    try:
        data = scrape_instagram(username)
        for idx, post in enumerate(data, start=1):
            print(f"Post {idx}:")
            print(f"Link: {post['link']}")
            print(f"Image URL: {post['image_url']}")
            print(f"Caption: {post['caption']}")
            print("-" * 30)
    except Exception as e:
        print(f"An error occurred: {e}")
