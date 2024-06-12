import random
import time

from locators import interactions_page_locators as locators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = locators.SortablePageLocators()
    elements = {
        "list": {
            "tab": locators.LIST_TAB,
            "menu": locators.LIST_MENU
        },
        "grid": {
            "tab": locators.GRID_TAB,
            "menu": locators.GRID_MENU
        }
    }

    def get_item_list(self, locator):
        list = self.elements_are_visible(locator)
        return [i.text for i in list]

    def change_elements(self, element):
        self.remove_ads()
        self.element_is_visible(self.elements[element]["tab"]).click()
        order_before = self.get_item_list(self.elements[element]["menu"])
        item_list = random.sample(self.elements_are_visible(self.elements[element]["menu"]), 2)
        item_from = item_list[0]
        item_to = item_list[1]
        self.drag_and_drop(item_from, item_to)
        order_after = self.get_item_list(self.elements[element]["menu"])
        return order_before, order_after


class SelectablePage(BasePage):
    locators = locators.SelectablePageLocators()
    elements = {
        "list": {
            "tab": locators.LIST_TAB,
            "menu": locators.LIST_MENU,
            "active": locators.LIST_MENU_ACTIVE
        },
        "grid": {
            "tab": locators.GRID_TAB,
            "menu": locators.GRID_MENU,
            "active": locators.GRID_MENU_ACTIVE
        }
    }

    def select_elements(self, element):
        self.remove_ads()
        self.element_is_visible(self.elements[element]["tab"]).click()
        self.click_to_select_item(self.elements[element]["menu"])
        active_items = self.element_is_visible(self.elements[element]["active"])
        return active_items.text

    def click_to_select_item(self, elements):
        item_list = self.elements_are_visible(elements)
        select = random.choice(item_list)
        select.click()


class ResizablePage(BasePage):
    locators = locators.ResizablePageLocators()

    def get_px_from_size(self, value_of_size):
        width = value_of_size.split(";")[0].split(":")[1].replace(" ","")
        height = value_of_size.split(";")[1].split(":")[1].replace(" ","")
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute("style")
        return size_value

    def change_size_box(self):
        self.remove_ads()
        time.sleep(0.1)  # Без задержки не срабатывает увеличение
        self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_size(self.get_max_min_size(self.locators.BOX))
        self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.BOX_HANDLE), -500, -300)
        min_size = self.get_px_from_size(self.get_max_min_size(self.locators.BOX))
        return max_size, min_size

    def change_size_window(self):
        self.remove_ads()
        self.action_drug_and_drop_by_offset(self.element_is_visible(self.locators.WINDOW_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_size(self.get_max_min_size(self.locators.WINDOW))
        self.action_drug_and_drop_by_offset(self.element_is_visible(self.locators.WINDOW_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_size(self.get_max_min_size(self.locators.WINDOW))
        return max_size, min_size
