from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

def linkedin_login(driver, email, password):
    """Logs into LinkedIn using Selenium."""
    driver.get("https://www.linkedin.com/login")
    time.sleep(3)

    email_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    email_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()
    time.sleep(5) 

def scrape_linkedin_profile(username, email, password):
    """Scrapes a LinkedIn public profile."""
    driver = webdriver.Chrome()  
    linkedin_login(driver, email, password)

    driver.get(f"https://www.linkedin.com/in/{username}/")
    time.sleep(5)

    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

   
    profile_name = soup.find("h1", class_="text-heading-xlarge").get_text(strip=True) if soup.find("h1", class_="text-heading-xlarge") else "No name"
    headline = soup.find("div", class_="text-body-medium").get_text(strip=True) if soup.find("div", class_="text-body-medium") else "No headline"
    about = soup.find("section", class_="pv-about-section").get_text(strip=True) if soup.find("section", class_="pv-about-section") else "No about section"

    return {
        "name": profile_name,
        "headline": headline,
        "about": about,
    }

if __name__ == "__main__":
    username = input("Enter LinkedIn profile username (e.g., 'john-doe'): ")
    email = input("Enter your LinkedIn email: ")
    password = input("Enter your LinkedIn password: ")

    try:
        data = scrape_linkedin_profile(username, email, password)
        print(f"Name: {data['name']}")
        print(f"Headline: {data['headline']}")
        print(f"About: {data['about']}")
    except Exception as e:
        print(f"An error occurred: {e}")
