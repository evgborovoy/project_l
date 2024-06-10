from pages.widgets_page import AccordianPage


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
