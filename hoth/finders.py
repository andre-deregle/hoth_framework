import element

from base import Base
from errors import NoneElementFound


class Finders(Base):

    """!
    Find methods.
    """

    def find(self, elem=None, **kwargs):
        """!
        Method that finds element in DOM HTML. You can use different
        web element parameters to search element, ex.:
        find(id="id_name"), find(class_="class_name"), find(type="type_name"),
        etc.
        Args:
            elem - object of element.Element class
            kwargs - params to search
        Returns:
            element.Element object
        Raise exception:
            NoneElementFound: if element is not found
        """
        Base().get_current_page_html()
        if 'class_' in kwargs.keys(): kwargs['class'] = kwargs.pop('class_')
        if elem:
            elem = elem.soup_hoth.find(**kwargs)
        else:
            elem = self.get_page_html().find(**kwargs)
        params = {}
        params['dom_tag'] = elem.name
        params['soup_hoth'] = elem
        for key in elem.attrs:
            params[key] = elem[key]
        if elem:
            return element.Element(params)
        else:
            raise NoneElementFound('No such element.')

    def all(self, elem=None, **kwargs):
        """!
        Method that find elements in DOM HTML and put them into list.
        You can use different web element parameters to search element,
        ex.:
        all(id="id_name"), all(class_="class_name"), all(type="type_name"),
        etc.
        Args:
            elem - object of element.Element class
            kwargs - params to search
        Returns:
            list of element.Element objects
        Raise exception:
            NoneElementFound: if any element is found
        """
        Base().get_current_page_html()
        if 'class_' in kwargs.keys():
            kwargs['class'] = kwargs.pop('class_')
        if elem:
            all_elements = elem.soup_hoth.find_all(**kwargs)
        else:
            all_elements = self.get_page_html().find_all(**kwargs)    
        all_classified_elem = []
        for element in all_elements:
            params = {}
            params['dom_tag'] = element.name
            params['soup_hoth'] = element
            for key in element.attrs:
                params[key] = element[key]
            all_classified_elem.append(element.Element(params))
        if all_classified_elem:
            return all_classified_elem
        else:
            raise NoneElementFound('No such element.')
