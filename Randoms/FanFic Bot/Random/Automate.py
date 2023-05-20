from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import os
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.in/")
print(driver.title)


l1 = driver.find_element_by_xpath('//*[@id="gb"]/div/div[2]/a')
l1.click()


l2 = driver.find_element_by_xpath('//*[@id="identifierId"]')
l2.send_keys("princethapak115@gmail.com")

nxt = driver.find_element_by_xpath('//*[@id="identifierNext"]')
nxt.click()

try_a = driver.find_element_by_xpath('//*[@id="next"]')
try_a.click()
