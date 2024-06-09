import locators.alerts_frame_windows_locators as locators
from pages.base_page import BasePage


class BrowserWindows(BasePage):
    locators = locators.BrowserWindowsLocators()
    def new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        tabs_count = self.driver.window_handles
        return tabs_count

    def new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.switch_to_window()
        text = self.element_is_visible(self.locators.NEW_WINDOW_TEXT).text
        return text

class AlertsPage(BasePage):
    locators = locators.AlertsLocators

    def simple_alert(self):
        self.element_is_visible(self.locators.SIMPLE_ALERT_BUTTON).click()
        alert = self.switch_to_alert()
        return alert.text

    def appear_alert(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_BUTTON).click()
        alert = self.switch_to_alert()
        return alert.text

    def confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert = self.switch_to_alert()
        alert.accept()
        status = self.element_is_present(self.locators.CONFIRM_ALERT_STATUS).text.split()[-1]
        return status

    def prompt_alert(self):
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert = self.switch_to_alert()
        data = "test_data"
        alert.send_keys(data)
        alert.accept()
        status = self.element_is_present(self.locators.PROMPT_ALERT_STATUS).text.split()[-1]
        return status, data
