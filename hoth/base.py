import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver


class Base:
    
    DRIVER = None
    PAGE_HTML = None
        
    def start_driver(self, driver_type="Firefox", path=None, remote=False):
        """!
        Method that starts Selenium  webdriver.
        Args:
            driver_type: string, browser type - Firefox, Chrome, etc.;
            path: string, path in your file system to executable driver;
            remote: boolean, trigger driver on remote machine.
        Returns:
            Selenium webdriver instance.
        """
        if remote:
            pass
        else:
            if path:  
                os.environ['webdriver.chrome.driver'] = path
            else:
                path = ''
            global DRIVER
            DRIVER = eval('webdriver.'+driver_type+'('+path+')')
            return DRIVER

    def visit_page(self, page_url):
        """!
        Method that visit page with "page_url" URL.
        Args:
            page_url: string, http(-s) address.
        """
        DRIVER.get(page_url)
        self.get_current_page_html()

    def get_current_page_html(self):
        """!
        Method that returns HTML of current page.
        Returns:
            PAGE_HTML - html of current page.
        """
        html = DRIVER.page_source
        global PAGE_HTML
        PAGE_HTML = BeautifulSoup(html, 'html.parser')
        return PAGE_HTML

    def get_page_html(self):
        return PAGE_HTML

    def get_driver(self):
        return DRIVER

    def close_driver(self):
        DRIVER.close()

    def quit_driver(self):
        DRIVER.quit()

    def maximize_window(self):
        DRIVER.maximize_window()

    def screen(self, location='./tmp/screenshots'):
        """! Saves screenshot."""
        timestamp = time.strftime('%d_%b_%Y_%H_%M')
        filename = timestamp + '.png'
        path = os.path.abspath(location)
        if not os.path.exists(path):
            os.makedirs(path)
        full_path = path + '/' + filename
        DRIVER.get_screenshot_as_file(full_path)
