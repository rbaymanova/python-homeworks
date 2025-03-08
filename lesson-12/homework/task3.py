from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json
import time

chrome_driver_path = r"C:\chromedriver-win64\chromedriver.exe" 
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.demoblaze.com/")
time.sleep(3)

driver.find_element(By.LINK_TEXT, "Laptops").click()
time.sleep(3)

laptops = []

while True:
    products = driver.find_elements(By.CLASS_NAME, "card-title")
    prices = driver.find_elements(By.CLASS_NAME, "card-block")

    for i in range(len(products)):
        name = products[i].text
        price = prices[i].find_element(By.TAG_NAME, "h5").text
        description = prices[i].find_element(By.TAG_NAME, "p").text
        laptops.append({"name": name, "price": price, "description": description})

    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next")
        next_button.click()
        time.sleep(3)
    except:
        break

with open("laptops.json", "w") as file:
    json.dump(laptops, file, indent=4)

driver.quit()
