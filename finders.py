from base import Base
from errors import NoneElementFound
import element
import pdb

class Finders(Base):

    def find(self, elem=False, **kwargs):
        if 'class_' in kwargs.keys():
            kwargs['class'] = kwargs.pop('class_')
        if elem:
            elem = self.soup_hoth.find(**kwargs)
        else:
            elem = self.get_page_html().find(**kwargs)
        elem['dom_tag'] = elem.name
        params = {}
        params['soup_hoth'] = elem
        for key in elem.attrs:
            params[key] = elem[key]
        if elem:
            return element.Element(params)
        else:
            raise NoneElementFound('No such element.')

    def all(self, elem=False, **kwargs):
        if 'class_' in kwargs.keys():
            kwargs['class'] = kwargs.pop('class_')
        if elem:
            all_elements = self.soup_hoth.find_all(**kwargs)
        else:
            all_elements = self.get_page_html().find_all(**kwargs)    
        all_classified_elem = []
        for element in all_elements:
            element['dom_tag'] = element.name
            params = {}
            params['soup_hoth'] = element
            for key in element.attrs:
                params[key] = element[key]
            all_classified_elem.append(element.Element(params))
        if all_classified_elem:
            return all_classified_elem
        else:
            raise NoneElementFound('No such element.')

if __name__ == "__main__":
    finder = Finders()
    finder.start_driver()
    finder.visit_page("https://sites.google.com/a/chromium.org/chromedriver/getting-started")
    pdb.set_trace()