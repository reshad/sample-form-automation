import os, time
import unittest
from selenium import webdriver

from page import TestForm


class FormTest(unittest.TestCase):
    valid_firstname = 'reshad'
    valid_lastname = 'raihan'
    valid_phone = '1234567890'

    invalid_name_empty = ''
    invalid_name_no_letters = '12345'
    invalid_name_by_length = 'reshadreshadraihanraihan'
    # =========================================================
    # There's a bug in first name and last name fields
    # Both field should allow multiple words with spaces between them
    # 'reshad raihan' should be a valid input for both first and last name fields
    # =========================================================
    invalid_phone_empty = ''
    invalid_phone_no_number = 'asd'
    invalid_phone_mixed = '123456asdf'
    invalid_phone_length1 = '123456'
    invalid_phone_length2 = '1234567890123'

    def setUp(self):
        self.driver = webdriver.Chrome()
        test_file = 'file://{}/{}'.format(os.getcwd(), "QATest.html")
        self.driver.get(test_file)

    def test_firstname_validation(self):
        page = TestForm(self.driver)
        page.fill_firstname_field(self.invalid_name_empty)
        page.submit_form()
        assert page.firstname_error.text == page.firstname_error_message_empty, \
            'Expected error message to be %s instead it shows %s' % (page.firstname_error_message_empty, page.firstname_error.text)
        page.clear_form()

        time.sleep(2)

        page.fill_firstname_field(self.invalid_name_no_letters)
        page.submit_form()
        assert page.firstname_error.text == page.firstname_error_message_char, \
            'Expected error message to be %s instead it shows %s' % (page.firstname_error_message_char, page.firstname_error.text)
        page.clear_form()

        time.sleep(2)

        page.fill_firstname_field(self.invalid_name_by_length)
        page.submit_form()
        assert page.firstname_error.text == page.firstname_error_message_length, \
            'Expected error message to be %s instead it shows %s' % (page.firstname_error_message_length, page.firstname_error.text)
        page.clear_form()

    def test_lastname_validation(self):
        page = TestForm(self.driver)
        page.fill_lastname_field(self.invalid_name_empty)
        page.submit_form()
        assert page.lastname_error.text == page.lastname_error_message_empty, \
            'Expected error message to be %s instead it shows %s' % (page.lastname_error_message_empty, page.lastname_error.text)
        page.clear_form()

        time.sleep(2)

        page.fill_lastname_field(self.invalid_name_no_letters)
        page.submit_form()
        assert page.lastname_error.text == page.lastname_error_message_char, \
            'Expected error message to be %s instead it shows %s' % (page.lastname_error_message_char, page.lastname_error.text)
        page.clear_form()

        time.sleep(2)

        page.fill_lastname_field(self.invalid_name_by_length)
        page.submit_form()
        assert page.lastname_error.text == page.lastname_error_message_length, \
            'Expected error message to be %s instead it shows %s' % (page.lastname_error_message_length, page.lastname_error.text)

        # =========================================================
        # BUG: The validation message should be - 'The max length of last name is 20'
        # instead it shows - The max length of first name is 20
        # =========================================================
        page.clear_form()

    def test_phone_validation(self):
        page = TestForm(self.driver)
        page.fill_phone_field(self.invalid_phone_empty)
        page.submit_form()
        assert page.phone_error.text == page.phone_error_message_empty, \
            'Expected error message to be %s instead it shows %s' % (page.phone_error_message_empty, page.phone_error.text)
        page.clear_form()

        time.sleep(2)

        page.fill_phone_field(self.invalid_phone_mixed)
        page.submit_form()
        assert page.phone_error.text == page.phone_error_message_incorrect, \
            'Expected error message to be %s instead it shows %s' % (page.phone_error_message_incorrect, page.phone_error.text)
        page.clear_form()

        time.sleep(2)

        page.fill_phone_field(self.invalid_phone_length1)
        page.submit_form()
        assert page.phone_error.text == page.phone_error_message_incorrect, \
            'Expected error message to be %s instead it shows %s' % (page.phone_error_message_incorrect, page.phone_error.text)
        page.clear_form()

        page.fill_phone_field(self.invalid_phone_length2)
        page.submit_form()
        assert page.phone_error.text == page.phone_error_message_incorrect, \
            'Expected error message to be %s instead it shows %s' % (page.phone_error_message_incorrect, page.phone_error.text)
        page.clear_form()

    def test_form_validation(self):
        page = TestForm(self.driver)
        page.fillup_form(self.invalid_name_empty, self.invalid_name_by_length, self.invalid_phone_mixed)
        page.submit_form()

        assert page.home_page_title.text == page.home_page_title_message, \
            'Expected page title to be %s' % (page.home_page_title_message, )
        assert page.firstname_error
        assert page.lastname_error
        assert page.phone_error

        page.clear_form()

        page.fillup_form('', '', '')
        page.submit_form()

        assert page.home_page_title.text == page.home_page_title_message, \
            'Expected home page title to be %s' % (page.home_page_title_message)
        assert page.firstname_error
        assert page.lastname_error
        assert page.phone_error

    def test_clear_form_action(self):
        page = TestForm(self.driver)
        page.fillup_form(self.valid_firstname, self.valid_lastname, self.valid_phone)
        page.clear_form()

        assert page.firstname.text == '', 'Expected firstname to be empty instead it shows %s' % (page.firstname.text)
        assert page.lastname.text == '', 'Expected last name to be empty instead it shows %s' % (page.lastname.text)
        assert page.phone.text == '', 'Expected phone to be empty instead it shows %s' % (page.phone.text)

    def test_successful_form_submission(self):
        page = TestForm(self.driver)
        page.fillup_form(self.valid_firstname, self.valid_lastname, self.valid_phone)
        page.submit_form()
        time.sleep(2)

        assert page.success_page_title.text == page.success_message, \
            'Expected success page title to be %s instead it shows %s' % (page.success_message, page.success_page_title.text)
        assert page.submitted_firstname.text == self.valid_firstname, \
            'Expected first name to be %s instead it shows %s' % (self.valid_firstname, page.submitted_firstname.text)
        assert page.submitted_lastname.text == self.valid_lastname, \
            'Expected last name to be %s instead it shows %s' % (self.valid_lastname, page.submitted_lastname.text)
        assert page.submitted_phone.text == self.valid_phone, \
            'Expected phone to be %s instead it shows %s' % (self.valid_phone, page.submitted_phone.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
