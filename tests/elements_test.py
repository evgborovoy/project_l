import time

import pages.elements_page as pe


class TestElements:
    class TestTextBox:

        def test_text_box_page(self, driver):
            text_box_page = pe.TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_name, input_email, input_curr_addr, input_perm_addr = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_addr, output_perm_addr = text_box_page.check_filled_form()
            assert output_name == input_name, "The full name does not match"
            assert output_email == input_email, "The email does not match"
            assert output_curr_addr == input_curr_addr, "The current address does not match"
            assert output_perm_addr == input_perm_addr, "The permanent address does not match"

    class TestCheckBox():

        def test_check_box_page(self, driver):
            check_box_page = pe.CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.expand_list()
            check_box_page.select_random_checkbox()
            checked_boxes = check_box_page.get_checked_checkboxes()
            result = check_box_page.get_output_result()
            assert checked_boxes in result, f"Items not equal"





