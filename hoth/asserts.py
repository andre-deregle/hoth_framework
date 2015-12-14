from base import Base
from errors import CantFindSuchText
from errors import NoneElementFound
from errors import ParamIsMissed
from finders import Finders
from selenium.webdriver.support.ui import Select
import pdb

class Assertions(Base):

    """!
    Different kind of assertions.
    """

    def page_has_text(self, text):
        """!
        Check if page has specific "text"
        Args:
            text: string, text to find on page.
        Returns:
            True if find text, False - if not.
        """
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
        """! Raise CantFindSuchText if "text" not on the page"""
        if self.page_has_text(text):
            return True
        else:
            raise CantFindSuchText('No such text on page!')

    def has_text(self, elem, text):
        """!
        Check if element has specific "text"
        Args:
            elem: element.Element, web element;
            text: string, text to find within element.
        Returns:
            True if find text, False - if not.
        """
        if text in eval(elem+'.text'):
            return True
        else:
            return False

    def should_has_text(self, elem, text):
        """! Raise CantFindSuchText if "text" not within element."""
        if self.has_text(elem, text):
            return True
        else:
            raise CantFindSuchText('Element doesn\'t contains such text!')

    def is_selected(self, elem):
        """!
        Check if element is selected (radiobutton or checkbox).
        Args:
            elem: element.Element, web element.
        Returns:
            True if element selected, False - if not.
        """
        if eval(elem+'.is_selected()'):
            return True
        else:
            return False

    def should_be_selected(self, elem):
        """! Raise ElementIsNot if "elem" is not selected."""
        if self.is_selected(elem):
            return True
        else:
           raise ElementIsNot('Element is not selected')

    def is_displayed(self, elem):
        """!
        Check if element is displayed.
        Args:
            elem: element.Element, web element.
        Returns:
            True if element displayed, False - if not.
        """
        if eval(elem+'.is_displayed()'):
            return True
        else:
            return False
    
    def should_be_displayed(self, elem):
        """! Raise ElementIsNot if "elem" is not displayed."""
        if self.is_displayed(elem):
            return True
        else:
           raise ElementIsNot('Element is not displayed')

    def is_enabled(self, elem):
        """!
        Check if element is enabled.
        Args:
            elem: element.Element, web element.
        Returns:
            True if element enabled, False - if not.
        """
        if eval(elem+'.is_enabled()'):
            return True
        else:
            return False

    def should_be_enabled(self, elem):
        """! Raise ElementIsNot if "elem" is not enabled."""
        if self.is_enabled(elem):
            return True
        else:
           raise ElementIsNot('Element is not enabled')
