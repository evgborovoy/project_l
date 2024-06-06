import time

from pages.elements_page import TextBoxPage

class TestElements:
    class TestTextBox:

        def test_text_box_page(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_name, input_email, input_curr_addr, input_perm_addr = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_addr, output_perm_addr = text_box_page.check_filled_form()
            assert output_name == input_name, "There is different full name"
            assert output_email == input_email, "There is different email"
            assert output_curr_addr == input_curr_addr, "There is different current address"
            assert output_perm_addr == input_perm_addr, "There is different permanent address"
