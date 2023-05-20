from selenium import webdriver
import pyautogui
import os
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://youtube.com/")
print(driver.title)

# sear = driver.find_element_by_id("search")

driver.get('https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620')
e = driver.find_element_by_id('identifierId')

time.sleep(5)
pyautogui.hotkey(os.getenv())