from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

def facebook_login(driver, email, password):
    """Logs into Facebook using Selenium."""
    driver.get("https://www.facebook.com/login")
    time.sleep(3)

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "pass")
    login_button = driver.find_element(By.NAME, "login")

    email_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()
    time.sleep(5) 

def scrape_facebook_profile(username, email, password):
    """Scrapes a Facebook public profile for posts."""
    driver = webdriver.Chrome()  
    facebook_login(driver, email, password)

    
    driver.get(f"https://www.facebook.com/{username}")
    time.sleep(5)

   
    for _ in range(3): 
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

  
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

   
    posts = []
    for post in soup.find_all("div", class_="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"):
        content = post.find("div", class_="ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a")
        timestamp_tag = post.find("a", class_="oajrlxb2")
        timestamp = timestamp_tag["aria-label"] if timestamp_tag else "No timestamp"
        post_text = content.get_text(strip=True) if content else "No content"
        posts.append({"timestamp": timestamp, "content": post_text})

    return posts

if __name__ == "__main__":
    username = input("Enter Facebook username or profile ID: ")
    email = input("Enter your Facebook email: ")
    password = input("Enter your Facebook password: ")

    try:
        data = scrape_facebook_profile(username, email, password)
        for idx, post in enumerate(data, start=1):
            print(f"Post {idx}:")
            print(f"Timestamp: {post['timestamp']}")
            print(f"Content: {post['content']}")
            print("-" * 30)
    except Exception as e:
        print(f"An error occurred: {e}")
