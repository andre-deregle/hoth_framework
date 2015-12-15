#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import unittest

from hoth import Hoth
import pdb


class PresentationLITS(unittest.TestCase):

    def setUp(self):
        test = Hoth()
        test.start_driver()
        test.maximize_window()

    def test_check_required(self):
        test = Hoth()
        test.visit_page('http://lits.com.ua/')
        test.click(class_='icon-mail')

        contact_form = test.find(id='cntctfrm_contact_form')
        contact_form.should_has_text('Запитання')
        contact_form.should_has_text('Ім\'я')
        contact_form.should_has_text('Email')
        contact_form.should_has_text('Captcha')

        name_input = contact_form.find(id='cntctfrm_contact_name')
        email_input = contact_form.find(id='cntctfrm_contact_email')
        q_input = contact_form.find(id='cntctfrm_contact_message')

        name_input.should_be_displayed()
        email_input.should_be_displayed()
        q_input.should_be_displayed()

        assert name_input.value == ''
        assert email_input.value == ''

        send_button = contact_form.find(type='submit')
        send_button.click()
        test.should_be_text_on_page('Please fill required fields!')
        test.close_driver()

    def test_check_captcha(self):
        test = Hoth()
        test.visit_page('http://lits.com.ua/')
        test.click(class_='icon-mail')
        test.should_be_text_on_page('Captcha *')
        element = test.find(class_='cptch_block')
        text_of_the_el = element.soup_hoth.get_text()
        equation = self.leave_only_equation(text_of_the_el)
        input_captcha = str(self.find_input_captcha(equation))
        captcha_input = test.find(class_='cptch_input')
        captcha_input.set_input(txt_=input_captcha)

        name_input = contact_form.find(id='cntctfrm_contact_name')
        email_input = contact_form.find(id='cntctfrm_contact_email')
        q_input = contact_form.find(id='cntctfrm_contact_message')

        name_input.set_input(txt_="Andriy Bondarev")
        email_input.set_input(txt_="bondarev.andriy@gmail.com")
        q_input.set_input(txt_="Python the King!")
        test.screen()
        #send_button = contact_form.find(type='submit')
        #send_button.click()
        test.close_driver()

        Дякуємо Вам!

    def leave_only_equation(self, text):
        captcha_text = text.replace('Captcha *\n\n', '')
        captcha_text = self.convert_opertation(captcha_text)
        number = " ".join(re.findall('[a-zA-Z]+', captcha_text))
        captcha_text = captcha_text.replace(number,
                                            self.convert_words_into_number(number))
        return captcha_text.replace(' ', '')

    def convert_opertation(self, text):
        operations = {u'+': '+', u'\u2212': '-', u'\xd7': '*'}
        for each in operations.keys():
            if each in text:
                text = text.replace(each, operations[each])
                break
        return text

    def convert_words_into_number(self, word):
        numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                   'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                   'nine': '9', 'ten': '10', 'eleven': '11', 'twelve': '12',
                   'thirteen': '13', 'fourteen': '14', 'fifteen': '15',
                   'sixteen': '16', 'seventeen': '17', 'eighteen': '18',
                   'nineteen': '19', 'twenty': '20', 'twenty one': '21',
                   'twenty two': '22', 'twenty three': '23', 'twenty four': '24',
                   'twenty five': '25', 'twenty six': '26', 'twenty seven': '27',
                   'twenty eight': '28', 'twenty nine': '29', 'thirty': '30',
                   'thirty one': '31', 'thirty two': '32', 'thirty three': '33',
                   'thirty four': '34', 'thirty five': '35', 'thirty six': '36',
                   'thirty seven': '37', 'thirty eight': '38',
                   'thirty nine': '39', 'forty': '40', 'forty one': '41',
                   'forty two': '42', 'forty three': '43', 'forty four': '44',
                   'forty five': '45', 'forty six': '46', 'forty seven': '47',
                   'forty eight': '48', 'forty nine': '49', 'fifty': '50',
                   'fifty one': '51', 'fifty two': '52', 'fifty three': '53',
                   'fifty four': '54', 'fifty five': '55', 'fifty six': '56',
                   'fifty seven': '57', 'fifty eight': '58', 'fifty nine': '59',
                   'sixty': '60', 'sixty one': '61', 'sixty two': '62',
                   'sixty three': '63', 'sixty four': '64', 'sixty five': '65',
                   'sixty six': '66', 'sixty seven': '67', 'sixty eight': '68',
                   'sixty nine': '69', 'seventy': '70', 'seventy one': '71',
                   'seventy two': '72', 'seventy three': '73',
                   'seventy four': '74', 'seventy five': '75',
                   'seventy six': '76', 'seventy seven': '77',
                   'seventy eight': '78', 'seventy nine': '79', 'eighty': '80',
                   'eighty one': '81', 'eighty two': '82', 'eighty three': '83',
                   'eighty four': '84', 'eighty five': '85', 'eighty six': '86',
                   'eighty seven': '87', 'eighty eight': '88',
                   'eighty nine': '89', 'ninety': '90', 'ninety one': '91',
                   'ninety two': '92', 'ninety three': '93', 'ninety four': '94',
                   'ninety five': '95', 'ninety six': '96', 'ninety seven': '97',
                   'ninety eight': '98', 'ninety nine': '99',
                   'one hundred': '100', 'zero': '0'}
        return numbers[word]

    def find_input_captcha(self, equation):
        before_eq = equation.split('=')[0]
        after_eq = equation.split('=')[-1]
        if after_eq == '':
            return eval(before_eq)
        else:
            operations = {'+': '-', '-': '', '*': '/'}
            for each in operations.keys():
                if each in before_eq:
                    if each == '-':
                        if before_eq[0] == '-':
                            input_c = eval(after_eq+'+'+before_eq.replace(each, ''))
                        elif before_eq[-1] == '-':
                            input_c = eval(before_eq+after_eq)
                    else:
                        input_c = eval(after_eq+operations[each]+before_eq.replace(each, ''))
                    break
            return input_c

    def tearDown(self):
        Hoth().close_driver()
        Hoth().quit_driver()

if __name__ == "__main__":
    unittest.main()