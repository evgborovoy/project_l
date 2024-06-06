import time

from pages.elements_page import TextBoxPage

class TestElements:
    class TestTextBox:

        def test_text_box_page(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_name, input_email, input_curr_addr, input_perm_addr = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_addr, output_perm_addr = text_box_page.check_filled_form()
            assert output_name == input_name, "The full name does not match"
            assert output_email == input_email, "The email does not match"
            assert output_curr_addr == input_curr_addr, "The current address does not match"
            assert output_perm_addr == input_perm_addr, "The permanent address does not match"
