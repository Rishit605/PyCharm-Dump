from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://it.rgpvonline.org/login/index.php")
print(driver.title)
Username = driver.find_element_by_id("username")
Username.send_keys("0101IT191046")
Pass = driver.find_element_by_id("password")
Pass.send_keys("this is f0r UIT login")
Log_In = driver.find_element_by_id("loginbtn")
Log_In.click()

Course_container_View = driver.find_element_by_id("page")
driver.get("https://it.rgpvonline.org/course/view.php?id=586")
Att = driver.find_element_by_css_selector('a[href^="https://it.rgpvonline.org/mod/attendance/view.php?id=12291"')
Att.click()

Submit_Att = driver.find_element_by_link_text('Submit attendance')
Submit_Att.click()
Status = driver.find_element_by_css_selector('input[id="id_status_4191"]')
Status.click()
Submit = driver.find_element_by_id("id_submitbutton")
Submit.click()

"""LOGOUT DONE NO NEED TAMPERING UNTIL ANYMORE FURTHER OPTIMIZED SOLUTION"""

Log_out_1 = driver.find_element_by_class_name("action-menu-trigger")
Log_out_1.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Log out"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "actionmenuaction-7"))
    )
    element.click()
except:
    driver.quit()

time.sleep(3)
