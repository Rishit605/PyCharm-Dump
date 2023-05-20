from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/')
browser = webdriver.Firefox(firefox_binary=binary)