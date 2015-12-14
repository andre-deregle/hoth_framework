import actions
import asserts
from base import Base
from finders import Finders

class Element:

    """!
    WebElement which is basicaly BeautifulSoup tag element.
    """
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def has_attr(self, attr):
        if attr in self.__dict__:
            return True
        else:
            return False

    def click(self, **kwargs):
        actions.Actions().click(self, **kwargs)

    def set_input(self, **kwargs):
        actions.Actions().set_input(self, **kwargs)

    def select(self, **kwargs):
        actions.Actions().select(self, **kwargs)

    def set_checkbox(self, **kwargs):
        actions.Actions().set_checkbox(self, **kwargs)

    def find(self, **kwargs):
        Finders().find(self, **kwargs)
    
    def all(self, **kwargs):
        Finders().all(self, **kwargs)

    def has_text(self, text):
        elem = actions.Actions()._change_to_selenium_elem(self)
        return asserts.Assertions().has_text(elem, text)

    def should_has_text(self, text):
        elem = actions.Actions()._change_to_selenium_elem(self)
        return asserts.Assertions().should_has_text(elem, text)

    def is_selected(self):
        elem = actions.Actions()._change_to_selenium_elem(self)
        return asserts.Assertions().is_selected(elem)

    def should_be_selected(self):
        elem = actions.Actions()._change_to_selenium_elem(self)
        return asserts.Assertions().should_be_selected(elem)

    def is_displayed(self):
        elem = actions.Actions()._change_to_selenium_elem(self)
        return asserts.Assertions().is_displayed(elem)

    def should_be_displayed(self):
        elem = actions.Actions()._change_to_selenium_elem(self)
        return asserts.Assertions().should_be_displayed(elem)

    def is_enabled(self):
        elem = actions.Actions()._change_to_selenium_elem(self)
        return asserts.Assertions().is_enabled(elem)

    def should_be_enabled(self):
        elem = actions.Actions()._change_to_selenium_elem(self)
        return asserts.Assertions().should_be_enabled(elem)


class Page(Element):

    """!
    BeautifulSoup html element.
    """

    def __init__(self):
        page = Base().get_current_page_html()
        page['dom_tag'] = "page"
        params = {}
        params["soup_hoth"] = page
        for key in page.attrs:
            params[key] = page[key]
        for param in params:
            setattr(self, param, params[param])

    def page_has_text(self, text):
        asserts.Assertions().page_has_text(self, text)

    def should_be_text_on_page(self, text):
        asserts.Assertions().page_has_text(self, text)
