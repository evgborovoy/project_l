from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def remove_ads(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').remove();")
        self.driver.execute_script("document.getElementById('Ad.Plus-970x250-1').remove();")

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=6):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=6):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=6):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=6):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=6):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=6):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_drug_and_drop_by_offset(self, element, x_coordinate, y_coordinate):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coordinate, y_coordinate)
        action.perform()

    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_alert(self, timeout=6):
        alert = wait(self.driver, timeout).until(EC.alert_is_present(), message="issue with alert")
        self.driver.switch_to.alert
        return alert

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def drag_and_drop(self, element_from, element_to):
        action = ActionChains(self.driver)
        action.drag_and_drop(element_from, element_to)
        action.perform()