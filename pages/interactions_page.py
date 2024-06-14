import random
import re
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
        width = value_of_size.split(";")[0].split(":")[1].replace(" ", "")
        height = value_of_size.split(";")[1].split(":")[1].replace(" ", "")
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


class DroppablePage(BasePage):
    locators = locators.DroppablePageLocators()

    def simple(self):
        self.remove_ads()
        drag = self.element_is_visible(self.locators.SIMPLE_TAB_DRAG)
        drop = self.element_is_visible(self.locators.SIMPLE_TAB_DROP)
        self.drag_and_drop(drag, drop)
        return drop.text

    def accept(self):
        self.remove_ads()
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        accept = self.element_is_visible(self.locators.ACCEPT_TAB_DRAG_ACCEPTABLE)
        not_accept = self.element_is_visible(self.locators.ACCEPT_TAB_DRAG_NOT_ACCEPTABLE)
        drop = self.element_is_visible(self.locators.ACCEPT_TAB_DROP)
        self.drag_and_drop(not_accept, drop)
        if drop.text != "Drop here":
            return drop.text, "Not acceptable box was accept"
        self.drag_and_drop(accept, drop)
        return drop.text, "Acceptable element has not been dropped"

    def prevent_propogation(self):
        self.remove_ads()
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag = self.element_is_visible(self.locators.PREVENT_TAB_DRAG)
        not_greedy_inner = self.element_is_visible(self.locators.PREVENT_NOT_GREEDY_INNER)
        not_greedy_outer = self.element_is_visible(self.locators.PREVENT_NOT_GREEDY_OUTER)

        self.drag_and_drop(drag, not_greedy_inner)
        not_greedy_inner_text = not_greedy_inner.text
        not_greedy_outer_text = not_greedy_outer.text

        greedy_inner = self.element_is_visible(self.locators.PREVENT_GREEDY_INNER)
        greedy_outer = self.element_is_visible(self.locators.PREVENT_GREEDY_OUTER)

        self.drag_and_drop(drag, greedy_inner)
        greedy_inner_text = greedy_inner.text
        greedy_outer_text = greedy_outer.text
        return not_greedy_inner_text, not_greedy_outer_text, greedy_inner_text, greedy_outer_text

    def revert(self):
        self.remove_ads()
        self.element_is_visible(self.locators.REVERT_TAB).click()
        revert = self.element_is_visible(self.locators.WILL_REVERT)
        drop = self.element_is_visible(self.locators.DROP_REVERT)
        self.drag_and_drop(revert, drop)
        revert_before = revert.get_attribute("style")
        time.sleep(1)
        revert_after = revert.get_attribute("style")
        return revert_before, revert_after

    def not_revert(self):
        self.element_is_visible(self.locators.REVERT_TAB).click()
        not_revert = self.element_is_visible(self.locators.NOT_REVERT)
        drop = self.element_is_visible(self.locators.DROP_REVERT)
        self.drag_and_drop(not_revert, drop)
        not_revert_before = not_revert.get_attribute("style")
        time.sleep(1)
        not_revert_after = not_revert.get_attribute("style")
        return not_revert_before, not_revert_after


class DragabblePage(BasePage):
    locators = locators.DragabblePageLoactors()

    def get_before_and_after_position(self, element):
        self.action_drug_and_drop_by_offset(element, random.randint(5, 10), random.randint(5, 10))
        position_before = element.get_attribute("style")
        self.action_drug_and_drop_by_offset(element, random.randint(50, 200), random.randint(50, 200))
        position_after = element.get_attribute("style")
        return position_before, position_after

    def get_top_position(self, position):
        return re.findall(r'\d[0-9]+|\d', position.split(";")[2])

    def get_left_position(self, position):
        return re.findall(r'\d[0-9]+|\d', position.split(";")[1])

    def simple_drag_box(self):
        self.remove_ads()
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag = self.element_is_visible(self.locators.SIMPLE_DRAG)
        before, after = self.get_before_and_after_position(drag)
        return before, after

    def axis_x_drag_box(self):
        self.remove_ads()
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        drag_x = self.element_is_visible(self.locators.AXIS_RESTRICTED_DRAG_X)
        position = self.get_before_and_after_position(drag_x)
        top_before = self.get_top_position(position[0])
        top_after = self.get_top_position(position[1])
        left_before= self.get_left_position(position[0])
        left_after = self.get_left_position(position[1])
        return top_before, top_after, left_before, left_after

    def axis_y_drag_box(self):
        self.remove_ads()
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        drag_y = self.element_is_visible(self.locators.AXIS_RESTRICTED_DRAG_Y)
        position = self.get_before_and_after_position(drag_y)
        top_before = self.get_top_position(position[0])
        top_after = self.get_top_position(position[1])
        left_before = self.get_left_position(position[0])
        left_after = self.get_left_position(position[1])
        return top_before, top_after, left_before, left_after