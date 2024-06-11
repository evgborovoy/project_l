import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, ProgressBarPage, SliderPage


class TestWidgets:
    class TestAccordian:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            accordian_list = ["first", "second", "third"]
            accordian_titles = ["What is Lorem Ipsum?", "Where does it come from?", "Why do we use it?"]
            for idx in range(len(accordian_list)):
                title, content = accordian_page.accordian_content(accordian_list[idx])
                assert title == accordian_titles[idx], "Title not found"
                assert content > 0, "Empty content"

        def test_accordian_show(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            result = accordian_page.accordian_show()
            assert result, "More than 1 is visible"

    class TestAutoComplete:
        def test_multiple_auto_complete(self, driver):
            auto_complete = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete.open()
            result, input_color = auto_complete.multiple_auto_complete()
            assert result == input_color, "Colors are different"

        def test_multiple_remove(self, driver):
            auto_complete = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete.open()
            before, after = auto_complete.remove_multiply_by_one()
            assert before != after, "Color is not remove by one"

        def test_single(self, driver):
            auto_complete = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete.open()
            output_color, input_color = auto_complete.single_value()
            assert output_color == input_color, "Incorrect color in field"

    class TestDateAndTime:
        def test_date_send_value(self, driver):
            date_pick_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_pick_page.open()
            before, after = date_pick_page.date_sand_value()
            print(before)
            print(after)
            assert before != after

        def test_date_pick(self, driver):
            date_pick_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_pick_page.open()
            before, after = date_pick_page.date_pick()
            assert before != after

        # TODO: create test for data and time pick

    class TestSliderPage:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()
            before, after = slider_page.change_slider_value()
            assert before != after, "Slider is not change value"

    class TestProgressBarPage:
        def test_slider(self, driver):
            progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()
            before, after = progress_bar_page.check_progress_bar()
            assert before != after, "Progress bar has not change value"