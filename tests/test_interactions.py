import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


class TestInteractions:
    class TestSortable:
        def test_change_list(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            order_before, order_after = sortable_page.change_elements("list")
            assert order_before != order_after, "Order was not change on list"

        def test_change_grid(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            order_before, order_after = sortable_page.change_elements("grid")
            assert order_before != order_after, "Order was not change on grid"

    class TestSelectable:

        def test_select_list(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            selected_item = selectable_page.select_elements("list")
            assert len(selected_item) > 0, "No selected item on list"

        def test_select_grid(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            selected_item = selectable_page.select_elements("grid")
            assert len(selected_item) > 0, "No selected item on list"

    class TestResizable:

        def test_resize_box(self, driver):
            resize_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resize_page.open()
            max_size, min_size = resize_page.change_size_box()
            assert max_size == ("500px", "300px") and min_size == ('150px', '150px'), "Out of box size"



        def test_resize_window(self, driver):
            resize_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resize_page.open()
            max_size, min_size = resize_page.change_size_window()
            print(max_size)
            print(min_size)
            assert max_size != min_size , "Size was not change"

