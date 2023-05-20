# from Pro.worker.flip import Serve
#
# inst = Serve()
# inst.first_page()

from selenium import webdriver
import pyautogui

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.flipkart.com")
print(driver.title)

driver.implicitly_wait(5)

try:
    no_btn = driver.find_element_by_css_selector('body > div._2Sn47c > div > div > button')
    no_btn.click()
except:
    print('Nope')

srh = driver.find_element_by_css_selector(
    '#container > div > div._1kfTjk > div._1rH5Jn > div._2Xfa2_ > div._1cmsER > form > div > div > input')
srh.click()
srh.send_keys('gaming laptops')

driver.implicitly_wait(5)

# try:
#     srh_btn = srh.find_element_by_css_selector(
#         '#container > div > div._1kfTjk > div._1rH5Jn > div._2Xfa2_ > div._1cmsER > form > div > button > svg')
#     srh_btn.click()
# except:
#     print("HaH! Got'eem")

pyautogui.hotkey('Enter')

# cat = driver.find_element_by_class_name('_3OwxoU')
# cat.click()
#
# cat1 = driver.find_element_by_css_selector('#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 >
# div._1YokD2._3Mn1Gg.col-2-12 > div > div > div > div > section > div:nth-child(9) > div > a') cat1.click()

star_flit = driver.find_element_by_css_selector(
    '#container > div > div._36fx1h._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-2-12 > div > div '
    '> div > section:nth-child(5) > div._3FPh42 > div > div:nth-child(1) > div > label > div._3879cV')
star_flit.click()

names = driver.find_elements_by_class_name('_13oc-S')
for name in names:
    n = name.find_element_by_css_selector('a.s1Q9rs')
    print(n.text)

# prices = driver.find_elements_by_class_name('_25b18c')
# for price in prices:
#     p = price.find_element_by_css_selector('div._30jeq3')
#     print(prices.text)
