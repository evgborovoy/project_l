import time

from pages.interactions_page import SortablePage


class TestInteractions:
    class TestSortable:
        def test_change_list(self,driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            order_before, order_after = sortable_page.change_elements("list")
            assert order_before != order_after, "Order was not change on list"

        def test_change_grid(self,driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            order_before, order_after = sortable_page.change_elements("grid")
            assert order_before != order_after, "Order was not change on grid"