from selenium import webdriver

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
