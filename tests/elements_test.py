import os
import random
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

    class TestCheckBox:

        def test_check_box_page(self, driver):
            check_box_page = pe.CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.expand_list()
            check_box_page.select_random_checkbox()
            checked_boxes = check_box_page.get_checked_checkboxes()
            result = check_box_page.get_output_result()
            assert checked_boxes in result, f"Items not equal"

    class TestRadioButton:

        def test_select_item(self, driver):
            radio_button_page = pe.RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            status = radio_button_page.select_item("yes")
            output = radio_button_page.check_status()
            assert output == status[0], "'Yes' is not selected from output"
            assert status[1], "'Yes' is not selected from status"
            status = radio_button_page.select_item("impressive")
            output = radio_button_page.check_status()
            assert output == status[0], "'Impressive' is not selected from output"
            assert status[1], "'Impressive' is not selected from status"

    class TestWebTable:
        def test_web_table_add_record(self, driver):
            web_table_page = pe.WebTablesPage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_record()
            table_records = web_table_page.get_table_records()
            assert new_person in table_records, "There is no new person in table"

        # test for add many records
        # def test_web_table_add_records(self, driver):
        #     web_table_page = pe.WebTablesPage(driver, "https://demoqa.com/webtables")
        #     web_table_page.open()
        #     new_persons = web_table_page.add_record()
        #     table_records = web_table_page.check_new_record()
        #     for person in new_persons:
        #         assert person in table_records, f"There is no '{person}' in table"

        def test_web_table_search_record(self, driver):
            web_table_page = pe.WebTablesPage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_record()
            web_table_page.search_record(new_person[random.randint(0, len(new_person) - 1)])
            table_records = web_table_page.get_table_records()
            assert new_person in table_records, "The record was not find fo search key"

        def test_update_record_info(self, driver):
            web_table_page = pe.WebTablesPage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            first_name = web_table_page.add_record()[0]
            web_table_page.search_record(first_name)
            age = web_table_page.update_record_info()
            table_records = web_table_page.get_table_records()
            assert age in table_records[0], "The record has not been changed"

        def test_delete_record(self, driver):
            web_table_page = pe.WebTablesPage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_record()
            table_records = web_table_page.get_table_records()
            assert new_person in table_records, "There is no new person in table"
            web_table_page.search_record(new_person[0])
            web_table_page.delete_record()
            table_records = web_table_page.get_table_records()
            assert new_person not in table_records

        def test_select_row_quantity(self, driver):
            web_table_page = pe.WebTablesPage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            data = web_table_page.select_rows_quantity()
            assert data[0] == data[1], "There is error in select rows quantity"

    class TestButtonsPage:

        def test_click_button(self, driver):
            button_page = pe.ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            result = button_page.one_click()
            assert result, "Button was not clicked"

        def test_double_click_button(self, driver):
            button_page = pe.ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            result = button_page.double_click()
            assert result

        def test_right_click_button(self, driver):
            button_page = pe.ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            result = button_page.right_click()
            assert result

    class TestLinksPage:

        def test_simple_link(self, driver):
            links_page = pe.LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_link = links_page.simple_link()
            assert href_link == current_link, f"Can not open link {href_link}: {current_link}"

        def test_broken_link(self, driver):
            links_page = pe.LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            result = links_page.bad_link("https://demoqa.com/bad-request")
            assert result == 400, f"Unexpected result: {result}"

    class TestUploadDownloadPage:
        def test_download(self, driver):
            upload_download_page = pe.UploadDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            upload_download_page.download()
            file_name = "sampleFile.jpeg"
            file_names = os.listdir(f"{os.getcwd()}/assets/")
            print(f"{os.getcwd()}/assets/")
            print(file_names)
            assert file_name in file_names, "Failed to download file"
            os.remove(f"{os.getcwd()}/assets/{file_name}")

        def test_upload(self, driver):
            upload_download_page = pe.UploadDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            path = f"{os.getcwd()}/assets/uploadFile.jpg"
            uploaded_file_name, file_name = upload_download_page.upload(path)
            assert uploaded_file_name == file_name

    class TestDynamicPropertiesPage:

        def test_enable_button(self, driver):
            dynamic_properties_page = pe.DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            result = dynamic_properties_page.enable_button()
            assert result, "Button is not enable"

        def test_color_button(self, driver):
            dynamic_properties_page = pe.DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.color_button()
            assert color_after != color_before, "Button is not change color"

        def test_visible_button(self, driver):
            dynamic_properties_page = pe.DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            result = dynamic_properties_page.visible_button()
            assert result, "Button is not appear"
