from actions import Actions
from asserts import Assertions
from base import Base
from finders import Finders

class Element:
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
        Actions().click(self, **kwargs)

    def set_input(self, **kwargs):
        Actions().set_input(self, **kwargs)

    def select(self, **kwargs):
        Actions().select(self, **kwargs)

    def set_checkbox(self, **kwargs):
        Actions().set_checkbox(self, **kwargs)

    def find(self, **kwargs):
        Finders().find(self, **kwargs)
    
    def all(self, **kwargs):
        Finders().all(self, **kwargs)

    def has_text(self, text):
        elem = Actions()._change_to_selenium_elem(self)
        return Assertions().has_text(elem, text)

    def should_has_text(self, text):
        elem = Actions()._change_to_selenium_elem(self)
        return Assertions().should_has_text(elem, text)

    def is_selected(self):
        elem = Actions()._change_to_selenium_elem(self)
        return Assertions().is_selected(elem)

    def should_be_selected(self):
        elem = Actions()._change_to_selenium_elem(self)
        return Assertions().should_be_selected(elem)

    def is_displayed(self):
        elem = Actions()._change_to_selenium_elem(self)
        return Assertions().is_displayed(elem)

    def should_be_displayed(self):
        elem = Actions()._change_to_selenium_elem(self)
        return Assertions().should_be_displayed(elem)

    def is_enabled(self):
        elem = Actions()._change_to_selenium_elem(self)
        return Assertions().is_enabled(elem)

    def should_be_enabled(self):
        elem = Actions()._change_to_selenium_elem(self)
        return Assertions().should_be_enabled(elem)


class Page(Element):
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
        Assertions().page_has_text(self, text)

    def should_be_text_on_page(self, text):
        Assertions().page_has_text(self, text)