import os
import time

from pages.practice_form_page import PracticeFormPage


class TestFormsPage:
    class TestPracticeFormsPage:

        def test_form(self, driver):
            practice_form_page = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
            practice_form_page.open()
            path = f"{os.getcwd()}/assets/uploadFile.jpg"
            image_name = path.split("/")[-1]
            p, subject = practice_form_page.fill_form(path)
            result = practice_form_page.form_result()
            print(result)
            for i in [f"{p.first_name} {p.last_name}", p.email, subject, image_name, p.current_address]:
                assert i in result, "Wrong info about person"