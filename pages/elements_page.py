import random
import time

import requests
from selenium.common import TimeoutException

from generator.generator import generated_person
import locators.element_page_lockators as epl
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select


class TextBoxPage(BasePage):
    locators = epl.TextBoxPageLocators

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.go_to_element(self.element_is_visible(self.locators.CURRENT_ADDRESS))
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.go_to_element(self.element_is_visible(self.locators.PERMANENT_ADDRESS))
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.go_to_element(self.element_is_visible(self.locators.SUBMIT_BUTTON))
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = epl.CheckBoxPageLocators()

    def expand_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def select_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ALL_TITLES_LIST)
        indexes = list(range(len(item_list)))
        for i in range(7):
            item = item_list[random.choice(indexes)]
            if item.text in ["Home", "Desktop", "Documents", "WorkSpace", "Office", "Downloads"]:
                continue
            self.go_to_element(item)
            item.click()

    def get_checked_checkboxes(self):
        checked_item = self.elements_are_visible(self.locators.CHECKED_ITEMS_LOCATOR)
        result = []
        for box in checked_item:
            title = box.find_element("xpath", ".//ancestor::span[@class='rct-text']").text.replace(" ", "").replace(
                ".doc", "").lower()
            result.append(title)
        return str(result)

    def get_output_result(self):
        result = [i.text.lower() for i in self.elements_are_present(self.locators.SELECTED_ITEMS_LOCATOR)]
        return str(result)


class RadioButtonPage(BasePage):
    locators = epl.RadioButtonPageLocators()

    def select_item(self, choice):
        choices = {
            "yes": [self.locators.YES_RADIO_ACTION, self.locators.YES_RADIO_STATUS],
            "impressive": [self.locators.IMP_RADIO_ACTION, self.locators.IMP_RADIO_STATUS],
        }
        radio_button = self.element_is_visible(choices[choice][0])
        radio_button.click()
        radio_button_status = self.element_is_present(choices[choice][1])
        return radio_button.text, radio_button_status.is_selected()

    def check_status(self):
        status = self.element_is_present(self.locators.CHECK_RADIO).text
        return status


class WebTablesPage(BasePage):
    locators = epl.WebTablesLocators()

    def add_record(self):
        """Add record in table about person"""
        count = 1  # random.randint(2, 4)
        # added_persons = []
        while count > 0:
            person_info = next(generated_person())
            # maybe use dict???
            # person = {
            #     "first_name": person_info.first_name,
            #     "last_name": person_info.last_name,
            #     "email": person_info.email,
            #     "age": person_info.age,
            #     "salary": person_info.salary,
            #     "department": person_info.department,
            # }
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_RECORD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            # added_persons.append([first_name, last_name, str(age), email, str(salary), department])
            return [first_name, last_name, str(age), email, str(salary), department]
        # return added_persons

    def get_table_records(self):
        all_records = self.elements_are_present(self.locators.ALL_RECORDS)
        persons_info = []
        for i in all_records:
            persons_info.append(i.text.split("\n"))
        return persons_info

    def search_record(self, key):
        self.element_is_visible(self.locators.SEARCH_BOX_INPUT).send_keys(key)

    def update_record_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    def delete_record(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def select_rows_quantity(self):
        rows_quantity = [5, 10, 20, 25, 50, 100]
        data = []
        for i in rows_quantity:
            count_row_button = Select(self.element_is_visible(self.locators.SELECT_FIELD))
            self.go_to_element(self.element_is_visible(self.locators.SELECT_FIELD))
            count_row_button.select_by_value(str(i))
            data.append(len(self.get_table_records()))
        return data, rows_quantity


class ButtonsPage(BasePage):
    locators = epl.ButtonPageLocators()

    def one_click(self):
        self.element_is_clickable(self.locators.CLICK_BUTTON).click()
        if self.element_is_present(self.locators.CHECK_CLICK_BUTTON):
            return True
        return False

    def double_click(self):
        self.go_to_element(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
        self.action_double_click(self.element_is_clickable(self.locators.DOUBLE_CLICK_BUTTON))
        if self.element_is_present(self.locators.CHECK_DOUBLE_CLICK_BUTTON):
            return True
        return False

    def right_click(self):
        self.go_to_element(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        self.action_right_click(self.element_is_clickable(self.locators.RIGHT_CLICK_BUTTON))
        if self.element_is_present(self.locators.CHECK_RIGHT_CLICK_BUTTON):
            return True
        return False


class LinksPage(BasePage):
    locators = epl.LinksPageLocators()

    def simple_link(self):
        link = self.element_is_visible(self.locators.SIMPLE_LINK)
        url = link.get_attribute("href")
        response = requests.get(url)
        if response.status_code == 200:
            link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            current_url = self.driver.current_url
            return url, current_url
        return url, response.status_code

    def bad_link(self, url):
        response = requests.get(url)
        if response.status_code == 400:
            return response.status_code
        self.element_is_visible(self.locators.BROKEN_LINK)


class UploadDownloadPage(BasePage):
    locators = epl.UploadDownloadPage

    def download(self):
        self.element_is_visible(self.locators.DOWNLOAD_BUTTON).click()
        time.sleep(1)

    def upload(self, path):
        file_name = path.split("/")[-1]
        self.element_is_clickable(self.locators.UPLOAD_BUTTON).send_keys(path)
        time.sleep(1)
        uploaded_path = self.element_is_present(self.locators.UPLOAD_FIELD_PATH).text
        uploaded_file_name = uploaded_path.split("\\")[-1]
        return uploaded_file_name, file_name


class DynamicPropertiesPage(BasePage):
    locators = epl.DynamicPropertiesPageLocators()

    def enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutException:
            return False
        return True

    def color_button(self):
        button = self.element_is_present(self.locators.COLOR_BUTTON)
        color_before = button.value_of_css_property("color")
        time.sleep(5.5)
        color_after = button.value_of_css_property("color")
        return color_before, color_after

    def visible_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_BUTTON)
        except TimeoutException:
            return False
        return True
