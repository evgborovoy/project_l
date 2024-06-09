from locators.alerts_frame_windows_locators import BrowserWindowsLocators
from pages.base_page import BasePage


class BrowserWindows(BasePage):
    locators = BrowserWindowsLocators()
    def new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        tabs_count = self.driver.window_handles
        return tabs_count

    def new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.switch_to()
        text = self.element_is_visible(self.locators.NEW_WINDOW_TEXT).text
        return text