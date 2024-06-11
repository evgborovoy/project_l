import random
import time

from generator.generator import generated_date

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
import locators.widgets_page_locators as locators


class AccordianPage(BasePage):
    locators = locators.AccordianLocators()

    def accordian_content(self, accordian_num):
        accordian = {
            "first": {
                "title": self.locators.FIRST_SECTION,
                "content": self.locators.FIRST_SECTION_CONTENT
            },
            "second": {
                "title": self.locators.SECOND_SECTION,
                "content": self.locators.SECOND_SECTION_CONTENT
            },
            "third": {
                "title": self.locators.THIRD_SECTION,
                "content": self.locators.THIRD_SECTION_CONTENT
            }
        }
        title = self.element_is_visible(accordian[accordian_num]["title"]).text
        try:
            content = self.element_is_visible(accordian[accordian_num]["content"], 1).text
        except TimeoutException:
            self.element_is_visible(accordian[accordian_num]["title"]).click()
            content = self.element_is_visible(accordian[accordian_num]["content"]).text
        return title, len(content)

    def accordian_show(self):
        accordion_show = [self.locators.FIRST_SECTION_SHOW, self.locators.SECOND_SECTION_SHOW,
                          self.locators.THIRD_SECTION_SHOW]
        accordion = [self.locators.FIRST_SECTION, self.locators.SECOND_SECTION, self.locators.THIRD_SECTION]

        for i in range(len(accordion_show)):
            for j in range(len(accordion_show)):
                if i == j:
                    continue
                try:
                    block = self.element_is_visible(accordion_show[i], 1)
                except TimeoutException:
                    self.element_is_visible(accordion[i]).click()
                    block = self.element_is_visible(accordion_show[i])
                if (block.get_attribute("class") == "collapse show") and (
                        self.element_is_present(accordion_show[j]).get_attribute("class") != "collapse"):
                    return False
        return True


class AutoCompletePage(BasePage):
    locators = locators.AutoCompleteLocators()

    def multiple_auto_complete(self):
        colors_list = ["Red", "Green", "Blue", "Black", "Yellow", "Purple", "White", "Indigo", "Magenta", "Aqua"]
        colors_input = random.sample(colors_list, random.randint(2, 5))
        for color in colors_input:
            field = self.element_is_clickable(self.locators.MULTIPLE_CONTAINER)
            field.send_keys(color[:3])
            time.sleep(.2)
            field.send_keys(Keys.ENTER)
        colors_from_field = list(
            map(lambda x: x.text, self.get_colors_from_multiple_field()))
        return colors_from_field, colors_input

    def remove_multiply_by_one(self):
        colors_count_before, _ = self.multiple_auto_complete()
        remove = self.elements_are_visible(self.locators.MULTIPLE_CONTAINER_VALUE_REMOVE)
        remove[0].click()
        colors_count_after = self.get_colors_from_multiple_field()
        return len(colors_count_before), len(colors_count_after)

    def get_colors_from_multiple_field(self):
        return self.elements_are_present(self.locators.MULTIPLE_CONTAINER_VALUE)

    def single_value(self):
        colors_list = ["Red", "Green", "Blue", "Black", "Yellow", "Purple", "White", "Indigo", "Magenta", "Aqua"]
        color_input = random.choice(colors_list)
        field = self.element_is_clickable(self.locators.SINGLE_CONTAINER)
        field.send_keys(color_input[:3])
        field.send_keys(Keys.ENTER)
        color_from_field = self.element_is_visible(self.locators.SINGLE_CONTAINER_VALUE).text
        return color_from_field, color_input


class DatePickerPage(BasePage):
    locators = locators.DatePickerLocators()

    def date_sand_value(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_FIELD)
        value_before = input_date.get_attribute("value")
        for i in range(10):  # Почему-то input_date.clear() не очищает поле
            input_date.send_keys(Keys.BACKSPACE)
        input_date.send_keys("01/01/2020")
        input_date.send_keys(Keys.ENTER)
        value_after = input_date.get_attribute("value")
        return value_before, value_after

    def date_pick(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_FIELD)
        value_before = input_date.get_attribute("value")
        input_date.click()
        self.set_date_by_text(self.locators.DATE_MONTH_FIELD, date.month)
        self.set_date_by_text(self.locators.DATE_YEAR_FIELD, date.year)
        self.set_item_from_list(self.locators.DATE_DAY_FIELD, date.date)
        value_after = input_date.get_attribute("value")
        return value_before, value_after

    def set_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    # TODO: Complete function
    # def select_date_and_time(self):
    #     date = next(generated_date())
    #     input_date = self.element_is_visible(self.locators.DATE_AND_TIME_FIELD)
    #     value_before = input_date.get_attribute("value")
    #     input_date.click()
    #     self.element_is_visible(self.locators.DATE_AND_TIME_MONTH_FIELD).click()
    #     self.set_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
    #     self.element_is_visible(self.locators.DATE_AND_TIME_YEAR_FIELD).click()
    #     self.set_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, random.choice(str(list(range(2020, 2028)))))
    #     self.set_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
    #     self.set_item_from_list(self.locators.DATE_AND_TIME_DAY_FIELD, date.date)
    #     value_after = input_date.get_attribute("value")
    #     print(date)
    #     print(value_before)
    #     print(value_after)


class SliderPage(BasePage):
    locators = locators.SliderPageLocators()

    def change_slider_value(self):
        value = self.element_is_visible(self.locators.SLIDER_VALUE)
        value_before = value.get_attribute("value")
        slider = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drug_and_drop_by_offset(slider, random.randint(1, 100), 0)
        value_after = value.get_attribute("value")
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = locators.ProgressBarLocators()

    def check_progress_bar(self):
        value = self.element_is_present(self.locators.PROGRESS_BAR).text
        button = self.element_is_visible(self.locators.START_STOP_BUTTON)
        button.click()
        time.sleep(random.randint(1, 4))
        button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR).text
        return value, value_after


class TabsPage(BasePage):
    locators = locators.TabsPageLocators()

    def check_tabs(self, tab):
        tabs = {
            "what": {
                "button": self.locators.TAB_WHAT,
                "content": self.locators.TAB_WHAT_CONTENT
            },
            "origin": {
                "button": self.locators.TAB_ORIGIN,
                "content": self.locators.TAB_ORIGIN_CONTENT
            },
            "use": {
                "button": self.locators.TAB_USE,
                "content": self.locators.TAB_USE_CONTENT
            }
        }
        button = self.element_is_visible(tabs[tab]["button"])
        button.click()
        title = button.text
        content = self.element_is_visible(tabs[tab]["content"]).text
        return title, len(content)


class ToolTipsPage(BasePage):
    locators = locators.ToolTipsPageLocators()

    def hover_on_element(self, element, hover):
        self.move_to_element(element)
        self.element_is_visible(hover)
        return self.element_is_visible(self.locators.TIP).text

    def hover_on_button(self):
        return self.hover_on_element(self.locators.BUTTON, self.locators.BUTTON_HOVERED)

    def hover_on_input_field(self):
        return self.hover_on_element(self.locators.INPUT_FIELD, self.locators.INPUT_FIELD_HOVERED)

    def hover_on_text(self):
        return self.hover_on_element(self.locators.CONTRARY, self.locators.CONTRARY_HOVERED)
