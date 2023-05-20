import Pro as hel
import os
from selenium import webdriver


class Serve(webdriver.Chrome):
    def __init__(self, d_path=r"C:\Program Files (x86)"):
        self.driver_path = d_path
        os.environ['PATH'] += self.driver_path
        super(Serve, self).__init__()

    def first_page(self):
        self.get(hel.main_url)
