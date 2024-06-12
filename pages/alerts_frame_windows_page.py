from selenium.common import TimeoutException

import locators.alerts_frame_windows_locators as locators
from pages.base_page import BasePage


class BrowserWindows(BasePage):
    locators = locators.BrowserWindowsLocators()

    def new_tab(self):
        self.remove_ads()
        self.element_is_visible(self.locators.NEW_TAB).click()
        tabs_count = self.driver.window_handles
        return tabs_count

    def new_window(self):
        self.remove_ads()
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.switch_to_window()
        text = self.element_is_visible(self.locators.NEW_WINDOW_TEXT).text
        return text


class AlertsPage(BasePage):
    locators = locators.AlertsLocators

    def simple_alert(self):
        self.remove_ads()
        self.element_is_visible(self.locators.SIMPLE_ALERT_BUTTON).click()
        alert = self.switch_to_alert()
        return alert.text

    def appear_alert(self):
        self.remove_ads()
        self.element_is_visible(self.locators.APPEAR_ALERT_BUTTON).click()
        alert = self.switch_to_alert()
        return alert.text

    def confirm_alert(self):
        self.remove_ads()
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert = self.switch_to_alert()
        alert.accept()
        status = self.element_is_present(self.locators.CONFIRM_ALERT_STATUS).text.split()[-1]
        return status

    def prompt_alert(self):
        self.remove_ads()
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert = self.switch_to_alert()
        data = "test_data"
        alert.send_keys(data)
        alert.accept()
        status = self.element_is_present(self.locators.PROMPT_ALERT_STATUS).text.split()[-1]
        return status, data


class FramePage(BasePage):
    locators = locators.FramePageLocators

    def check_frame(self):
        self.remove_ads()
        frames = [self.locators.FRAME1, self.locators.FRAME2]
        result = []
        for frame in frames:
            self.driver.switch_to.frame(frame)
            result.append(frame + ":" + self.element_is_visible(("xpath", "//body")).text)
            self.driver.switch_to.default_content()
        return result


class NestedFramePage(BasePage):
    locators = locators.NestedFramePageLocators

    def check_nested_frames(self):
        self.remove_ads()
        result = []
        frames = [self.locators.PARENT_FRAME, self.locators.CHILD_FRAME]
        for frame in frames:  # Switch on frame using frame index
            self.driver.switch_to.frame(frame)
            result.append(self.element_is_visible(self.locators.FRAME_TEXT).text)
        return result


class ModalDialogsPage(BasePage):
    locators = locators.ModalDialogsPageLocators

    def small_modal_text(self):
        self.remove_ads()
        self.element_is_visible(self.locators.SMALL_MODAL).click()
        return self.element_is_visible(self.locators.SMALL_MODAL_TEXT).text

    def small_modal_close_overlay(self):
        self.remove_ads()
        self.element_is_visible(self.locators.SMALL_MODAL).click()
        self.element_is_visible(self.locators.SMALL_MODAL_OVERLAY).click()
        try:
            self.element_is_not_visible(self.locators.SMALL_MODAL_OVERLAY)
            return True
        except TimeoutException:
            return False

    def large_modal_text(self):
        self.remove_ads()
        self.element_is_visible(self.locators.LARGE_MODAL).click()
        return self.element_is_visible(self.locators.LARGE_MODAL_TEXT).text

    def large_modal_close_overlay(self):
        self.element_is_visible(self.locators.LARGE_MODAL).click()
        self.element_is_visible(self.locators.LARGE_MODAL_OVERLAY).click()
        try:
            self.element_is_not_visible(self.locators.LARGE_MODAL_OVERLAY)
            return True
        except TimeoutException:
            return False
