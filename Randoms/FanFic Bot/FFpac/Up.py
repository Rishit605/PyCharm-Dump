import os
from selenium import webdriver


class UpDwn(webdriver.Chrome):
    def __init__(self, d_path=r"C:\Program Files (x86)\chromedriver.exe"):
        self.driver_path = d_path
        os.environ['PATH'] += self.driver_path
        super(UpDwn, self).__init__()

    def land_first_page(self):
        self.get("https://www.fanfiction.net")
