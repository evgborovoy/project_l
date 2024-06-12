import random

from locators import interactions_page_locators as locators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = locators.SortablePageLocators()

    def get_item_list(self, locator):
        list = self.elements_are_visible(locator)
        return [i.text for i in list]

    def change_elements(self, element):
        elements = {"list": {
            "tab": self.locators.LIST_TAB,
            "menu": self.locators.LIST_MENU
        },
            "grid": {
                "tab": self.locators.GRID_TAB,
                "menu": self.locators.GRID_MENU

            }}
        self.remove_ads()
        self.element_is_visible(elements[element]["tab"]).click()
        order_before = self.get_item_list(elements[element]["menu"])
        item_list = random.sample(self.elements_are_visible(elements[element]["menu"]), 2)
        item_from = item_list[0]
        item_to = item_list[1]
        self.drag_and_drop(item_from, item_to)
        order_after = self.get_item_list(elements[element]["menu"])
        return order_before, order_after

