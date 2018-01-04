from page_objects import PageObject, PageElement


class TestForm(PageObject):
    home_page_title = PageElement(tag_name='h1')
    home_page_title_message = 'Test Form'
    firstname = PageElement(id_='fname')
    firstname_error = PageElement(id_='fname-error')
    lastname = PageElement(id_='lname')
    lastname_error = PageElement(id_='lname-error')
    phone = PageElement(id_='phone')
    phone_error = PageElement(id_='phone-error')
    submit_button = PageElement(id_='submit')
    clear_form_button = PageElement(css='button[onclick="return clearForm();"]')

    success_page_title = PageElement(tag_name='p')
    success_message = 'Form submitted!'
    submitted_firstname = PageElement(id_='fname-submit')
    submitted_lastname = PageElement(id_='lname-submit')
    submitted_phone = PageElement(id_='phone-submit')

    firstname_error_message_empty = 'First name is a required field'
    lastname_error_message_empty = 'Last name is a required field'
    firstname_error_message_char = 'First name can only be characters'
    lastname_error_message_char = 'Last name can only be characters'
    firstname_error_message_length = 'The max length of first name is 20'
    lastname_error_message_length = 'The max length of first name is 20' # To handle an existing bug
    phone_error_message_empty = 'Phone number is a required input'
    phone_error_message_incorrect = 'Phone is incorrect'

    def fill_firstname_field(self, value):
        self.firstname = value

    def fill_lastname_field(self, value):
        self.lastname = value

    def fill_phone_field(self, value):
        self.phone = value

    def submit_form(self):
        self.submit_button.click()

    def clear_form(self):
        self.clear_form_button.click()

    def fillup_form(self, fname, lname, number):
        self.firstname = fname
        self.lastname = lname
        self.phone = number
