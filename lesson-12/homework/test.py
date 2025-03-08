from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\chromedriver-win64\chromedriver.exe" 

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

time.sleep(60)

driver.quit()
