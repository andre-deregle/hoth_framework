import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pdb


class Base:
    
    DRIVER = None
    PAGE_HTML = None
        
    def start_driver(self, driver_type="Firefox", path=None, remote=False):
        if remote:
            pass
        else:
            if path:  
                os.environ["webdriver.chrome.driver"] = path
            else:
                path = ""
            global DRIVER
            DRIVER = eval("webdriver."+driver_type+"("+path+")")
            return DRIVER

    def visit_page(self, page_url):
        DRIVER.get(page_url)
        self.get_current_page_html()

    def get_current_page_html(self):
        html = DRIVER.page_source
        global PAGE_HTML
        PAGE_HTML = BeautifulSoup(html, 'html.parser')
        return PAGE_HTML

    def get_page_html(self):
        return PAGE_HTML

    def get_driver(self):
        return DRIVER

if __name__ == "__main__":
    base = Base()
    base.start_driver()
    base.visit_page("https://sites.google.com/a/chromium.org/chromedriver/getting-started")
    pdb.set_trace()