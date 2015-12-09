from base import Base
from errors import NoneElementFound
from errors import ParamIsMissed
from finders import Finders
from selenium.webdriver.support.ui import Select
import pdb

class Assertions(Base):

    def page_has_text(self, text):
        top_level_tags = ['html', 'head', 'meta', 'script', 'link', 'style', 'title', 'body']
        tags = []
        soup = self.get_current_page_html()
        for tag in soup.find_all(True):
            tag_name = tag.name
            if tag_name not in tags and tag_name not in top_level_tags:
                tags.append(tag_name)
        page_text = ''
        for tag in tags:
            for each in soup.find_all(tag):
                page_text = page_text + each.get_text() + ' '
        if text in page_text:
            return True
        else:
            return False

    def should_be_text_on_page(self, text):
        if self.page_has_text(text):
            return True
        else:
            raise CantFindSuchText('No such text on page!')

    def has_text(self, elem, text):
        if text in eval(elem+'.text'):
            return True
        else:
            return False

    def should_has_text(self, elem, text):
        if self.has_text(elem, text):
            return True
        else:
            raise CantFindSuchText('Element doesn\'t contains such text!')

    def is_selected(self, elem):
        if eval(elem+'.is_selected()'):
            return True
        else:
            return False

    def should_be_selected(self, elem):
        if self.is_selected(elem):
            return True
        else:
           raise ElementIsNot('Element is not selected')

    def is_displayed(self, elem):
        if eval(elem+'.is_displayed()'):
            return True
        else:
            return False
    
    def should_be_displayed(self, elem):
        if self.is_displayed(elem):
            return True
        else:
           raise ElementIsNot('Element is not displayed')

    def is_enabled(self, elem):
        if eval(elem+'.is_enabled()'):
            return True
        else:
            return False

    def should_be_enabled(self, elem):
        if self.is_enabled(elem):
            return True
        else:
           raise ElementIsNot('Element is not enabled')
