from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.fanfiction.net/login.php?cache=bust")
print((driver.title))

Username = driver.find_element_by_id("email")
Username.send_keys("jacksonsamuel129@gmail.com")
Pass = driver.find_element_by_id("password")
Pass.send_keys("FanFiction B0I882")

Submit = driver.find_element_by_id("submitBtn")
Submit.click()