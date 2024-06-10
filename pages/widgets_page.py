from selenium.common import TimeoutException

from pages.base_page import BasePage
import locators.widgets_page_locators as locators


class AccordianPage(BasePage):
    locators = locators.Accordian()

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
