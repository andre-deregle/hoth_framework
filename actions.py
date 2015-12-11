import element

from selenium.webdriver.support.ui import Select

from base import Base
from errors import ParamIsMissed
from finders import Finders

import pdb


class Actions(Base):

    """!
    Actions that can interact with web elements.
    """

    def click(self, elem=None, **kwargs):
        """!
        Method that clicks element.Element object.
        Args:
            elem - object of element.Element class
            kwargs - params to search
        """
        Base().get_current_page_html()
        selenium_elem = self._change_to_selenium_elem(elem, **kwargs)
        eval(selenium_elem+".click()")

    def set_input(self, elem=None, **kwargs):
        """!
        Method that set input value. Need "txt" as one kwargs to set
        specific text.
        Args:
            elem - object of element.Element class;
            kwargs - params to search.
        Raise exception:
            ParamIsMissed: if missed option "txt_" while calling method.
        """
        Base().get_current_page_html()
        if "txt_" in kwargs.keys():
            value = kwargs["txt_"]
            kwargs.pop('txt_')
        else:
            raise ParamIsMissed('You missed "txt_" param.')
        selenium_elem = self._change_to_selenium_elem(elem, **kwargs)
        eval(selenium_elem+".clear()")
        eval(selenium_elem+".send_keys(\""+value+"\")")

    def select(self, elem=None, **kwargs):
        """!
        Method that select value from dropdown. Need "option_" as one of
        kwargs to select specific option.
        Args:
            elem - object of element.Element class;
            kwargs - params to search.
        Raise exception:
            ParamIsMissed: if missed option "option_" while calling method.
        """
        Base().get_current_page_html()
        if "option_" in kwargs.keys():
            value = kwargs["option_"]
            kwargs.pop('option_')
        else:
            raise ParamIsMissed('You missed "option_" param.')
        selenium_elem = self._change_to_selenium_elem(elem, **kwargs)
        ddl = eval("Select("+selenium_elem+")")
        ddl.select_by_visible_text(value)

    def set_checkbox(self, elem=None, **kwargs):
        """!
        Method that checks checkbox. Need "check_" as one of
        kwargs (True or False) check or uncheck checkbox.
        Args:
            elem - object of element.Element class;
            kwargs - params to search.
        Raise exception:
            ParamIsMissed: if missed option "check_" while calling method.
        """
        Base().get_current_page_html()
        if "check_" in kwargs.keys():
            value = kwargs["check_"]
            kwargs.pop('check_')
        else:
            raise ParamIsMissed('You missed "check_" param.')
        selenium_elem = self._change_to_selenium_elem(elem, **kwargs)
        if value and not eval(selenium_elem+'.is_selected()'):
                eval(selenium_elem+".click()")
        elif not value and eval(selenium_elem+'.is_selected()'):
                eval(selenium_elem+".click()")

    def _change_to_selenium_elem(self, elem=None, **kwargs):
        """!
        Method that changes BeautifulSoup element to Selenium element.
        Args:
            elem - object of element.Element class;
            kwargs - params to search.
        Returns:
            Selenium element.
        """
        if elem:
            soup_element = elem.soup_hoth
        else:
            soup_element = Finders().find(**kwargs).soup_hoth
        if not soup_element.has_attr('id'):
            locator = soup_element['id']
            return "self.get_driver().find_element_by_id(\'"+locator+"\')"
        elif not soup_element.has_attr('class'):
            locator = soup_element['class'][0]
            return "self.get_driver().find_element_by_class_name(\'"+locator+"\')"
        else:
            def find_by_css(element):
                without_text = str(element).replace(element.get_text(), '')
                tag = without_text.split()[0][1:]
                without_front_tag = without_text.replace("<"+tag+" ", "")
                without_tag = ""
                if "</"+tag+">" in without_front_tag:
                    without_tag = without_front_tag.replace("</"+tag+">", "")
                elif "/>" in without_front_tag:
                    without_tag = without_front_tag.replace("/>", "")
                list_of_params = without_tag.split("\" ")
                locator = tag
                for each in list_of_params:
                    if each[-1] != "\"":
                        locator = locator + "[" + each + "\"]"
                    else:
                        locator = locator + "[" + each + "]"
                return "self.get_driver().find_element_by_css_selector(\'"+locator+"\')"
            return find_by_css(soup_element)
