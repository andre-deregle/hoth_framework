from base import Base
from errors import NoneElementFound
from errors import ParamIsMissed
from finders import Finders
import element
from selenium.webdriver.support.ui import Select
import pdb

class Actions(Base):

    def click(self, elem=False, **kwargs):
        selenium_elem = self._change_to_selenium_elem(elem, **kwargs)
        eval(selenium_elem+".click()")


    def set_input(self, elem=False, **kwargs):
        if "txt_" in kwargs.keys():
            value = kwargs["txt_"]
            kwargs.pop('txt_')
        else:
            raise ParamIsMissed('You missed "txt_" param.')
        selenium_elem = self._change_to_selenium_elem(elem, **kwargs)
        eval(selenium_elem+".clear()")
        eval(selenium_elem+".send_keys(\""+value+"\")")

    def select(self, elem=False, **kwargs):
        if "option_" in kwargs.keys():
            value = kwargs["option_"]
            kwargs.pop('option_')
        else:
            raise ParamIsMissed('You missed "option_" param.')
        selenium_elem = self._change_to_selenium_elem(elem, **kwargs)
        ddl = eval("Select("+selenium_elem+")")
        ddl.select_by_visible_text(value)

    def set_checkbox(self, elem=False, **kwargs):
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

    def _change_to_selenium_elem(self, elem=False, **kwargs):
        if elem:
            soup_element = elem.soup_hoth
        else:
            soup_element = Finders().find(**kwargs).soup_hoth
        if soup_element.has_attr('id'):
            locator = soup_element['id']
            return "self.get_driver().find_element_by_id(\""+locator+"\")"
        elif soup_element.has_attr('class'):
            locator = soup_element['class'][0]
            return "self.get_driver().find_element_by_class_name(\""+locator+"\")"
        else:
            return self._find_by_css(soup_element)

    def _find_by_css(self, element): 
        without_text  =str(element).replace('>'+element.get_text(), '')
        tag = without_text.split()[0][1:]
        without_tag = without_text.replace("<"+tag+" ", "").replace("</"+tag+">", "")
        list_of_params = without_tag.split("\" ")
        locator = tag
        for each in list_of_params:
            if each[-1] != "\"":
                locator = locator + "[" + each + "\"]"
            else:
                locator = locator + "[" + each + "]"
        return "self.get_driver().find_element_by_css_selector(\""+locator+"\")"

if __name__ == "__main__":
    clicker = Actions()
    clicker.start_driver()
    clicker.visit_page("https://www.facebook.com/?_rdr=p")
    pdb.set_trace()