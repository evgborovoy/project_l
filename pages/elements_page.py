import random
import time

from generator.generator import generated_person
import locators.element_page_lockators as epl
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = epl.TextBoxPageLockators

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
        for i in range(5):
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
            print(title)
            result.append(title)
        return str(result)

    def get_output_result(self):
        result = [i.text.lower() for i in self.elements_are_present(self.locators.SELECTED_ITEMS_LOCATOR)]
        return str(result)
