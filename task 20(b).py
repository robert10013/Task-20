import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()

driver.get("https://labour.gov.in/")
time.sleep(3)
documents_menu = driver.find_element(By.XPATH, "//a[text()='Documents']")
ActionChains(driver).move_to_element(documents_menu).perform()
monthly_progress_report_link = driver.find_element(By.XPATH, "//a[text()='Monthly Progress Report']")
monthly_progress_report_link.click()
time.sleep(3)
report_link = driver.find_element(By.XPATH, "(//a[contains(@href, 'download')])[1]")
report_url = report_link.get_attribute('href')
report_response = requests.get(report_url)
with open('monthly_progress_report.pdf', 'wb') as file:
    file.write(report_response.content)
print("Monthly Progress Report downloaded.")
media_menu = driver.find_element(By.XPATH, "//a[text()='Media']")
ActionChains(driver).move_to_element(media_menu).perform()
photo_gallery_menu = driver.find_element(By.XPATH, "//a[text()='Photo Gallery']")
photo_gallery_menu.click()
if not os.path.exists('photo_gallery'):
    os.makedirs('photo_gallery')


photos = driver.find_elements(By.XPATH, "//div[contains(@class, 'photo-gallery')]//img")[:10]


for index, photo in enumerate(photos):
    photo_url = photo.get_attribute('src')
    photo_response = requests.get(photo_url)
    with open(f'photo_gallery/photo_{index + 1}.jpg', 'wb') as file:
        file.write(photo_response.content)

    print(f"Downloaded photo {index+1}")
