import sys

import actions
import asserts
import base
import finders


class Hoth:
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf8')

    # Base Selenium Webdriver methods
    def start_driver(self, driver_type="Firefox", path=None, remote=False):
        return base.Base().start_driver(driver_type, path, remote)

    def visit_page(self, page_url):
        base.Base().visit_page(page_url)

    def get_current_page_html(self):
        return base.Base().get_current_page_html()

    def get_page_html(self):
        return base.Base().get_page_html()

    def get_driver(self):
        return base.Base().get_driver()

    def close_driver(self):
        base.Base().close_driver()

    def quit_driver(self):
        base.Base().close_driver()

    def maximize_window(self):
        base.Base().maximize_window()

    def screen(self, location='./tmp/screenshots'):
        base.Base().screen(location)

    # Assertions
    def page_has_text(self, text):
        return asserts.Assertions().page_has_text(text)

    def should_be_text_on_page(self, text):
        return asserts.Assertions().should_be_text_on_page(text)

    def has_text(self, elem, text):
        return asserts.Assertions().has_text(elem, text)

    def should_has_text(self, elem, text):
        return asserts.Assertions().should_has_text(elem, text)

    def is_selected(self, elem):
        return asserts.Assertions().is_selected(elem)

    def should_be_selected(self, elem):
        return asserts.Assertions().should_be_selected(elem)

    def is_displayed(self, elem):
        return asserts.Assertions().is_displayed(elem)

    def should_be_displayed(self, elem):
        return asserts.Assertions().should_be_displayed(elem)

    def is_enabled(self, elem):
        return asserts.Assertions().is_enabled(elem)

    def should_be_enabled(self, elem):
        return asserts.Assertions().should_be_enabled(elem)

    # Actions
    def click(self, elem=None, **kwargs):
        actions.Actions().click(elem, **kwargs)

    def set_input(self, elem=None, **kwargs):
        actions.Actions().set_input(elem, **kwargs)

    def select(self, elem=None, **kwargs):
        actions.Actions().select(elem, **kwargs)

    def set_checkbox(self, elem=None, **kwargs):
        actions.Actions().set_checkbox(elem, **kwargs)

    #Finders
    def find(self, elem=None, **kwargs):
        return finders.Finders().find(elem, **kwargs)

    def all(self, elem=None, **kwargs):
        return finders.Finders().all(elem, **kwargs)
