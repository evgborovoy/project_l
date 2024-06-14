import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage


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
            assert max_size != min_size, "Size was not change"

    class TestDroppable:
        def test_simple(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            result = droppable_page.simple()
            assert result == "Dropped!", "Element has not been dropped"

        def test_accept(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            result, message = droppable_page.accept()
            assert result == "Dropped!", message

        def test_prevent(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy_inner, not_greedy_outer, greedy_inner, greedy_outer = droppable_page.prevent_propogation()
            assert not_greedy_inner and not_greedy_outer == "Dropped!", "Element has not been dropped in not greedy"
            assert greedy_inner == "Dropped!", "Element has not been dropped"
            assert greedy_outer == "Outer droppable", "Element has been dropped not in inner box"

        def test_revert(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            revert_before, revert_after = droppable_page.revert()
            not_revert_before, not_revert_after = droppable_page.not_revert()
            assert revert_before != revert_after
            assert not_revert_before == not_revert_after

    class TestDragabblePage:
        def test_simple(self, driver):
            draggable_page = DragabblePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            assert before != after, "Element has not been move"

        def test_axis_x(self, driver):
            draggable_page = DragabblePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before_top, after_top, before_left, after_left = draggable_page.axis_x_drag_box()
            assert before_top == after_top, "Element was move on Y-axis"
            assert before_left != after_left, "Element was not move on X-axis"

        def test_axis_Y(self, driver):
            draggable_page = DragabblePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before_top, after_top, before_left, after_left = draggable_page.axis_y_drag_box()
            assert before_top != after_top, "Element was move on X-axis"
            assert before_left == after_left, "Element was not move on Y-axis"