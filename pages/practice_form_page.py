import random

from selenium.webdriver import Keys

from generator.generator import generated_person
from pages.base_page import BasePage
from locators.practice_form_locators import PracticeFormLocators


class PracticeFormPage(BasePage):
    locators = PracticeFormLocators()

    def fill_form(self, image_path):
        self.remove_ads()
        person_info = next(generated_person())
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person_info.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person_info.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person_info.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.go_to_element(self.element_is_present(self.locators.GENDER))
        self.element_is_visible(self.locators.MOBILE).send_keys(person_info.mobile)
        # self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(person_info.)
        subject = random.choice(["Maths", "Commerce", "Biology"])
        self.element_is_visible(self.locators.SUBJECTS).send_keys(subject)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.PICTURE_FIELD).send_keys(image_path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_FIELD).send_keys(person_info.current_address)
        self.go_to_element(self.element_is_present(self.locators.CURRENT_ADDRESS_FIELD))
        self.element_is_present(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person_info, subject

    def form_result(self):
        result = self.elements_are_visible(self.locators.RESULT_TABLE)
        data = []
        for i in result:
            data.append(i.text)
        return data
