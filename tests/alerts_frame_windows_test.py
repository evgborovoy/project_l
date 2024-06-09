import time

from pages.alerts_frame_windows_page import BrowserWindows, AlertsPage


class TestAlertsFrameWindows:

    class TestBrowserWindows:
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindows(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            tabs = browser_windows_page.new_tab()
            assert len(tabs) == 2, "Failed to open new tab"

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindows(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text = browser_windows_page.new_window()
            time.sleep(3)
            assert text == "This is a sample page", "Failed to open new window"

    class TestAlerts:
        def test_simple_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            result = alert_page.simple_alert()
            expected = "You clicked a button"
            assert result == expected, "Alert is not open"

        def test_appear_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            result = alert_page.appear_alert()
            expected = "This alert appeared after 5 seconds"
            assert result == expected, "Alert is not open"

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            status = alert_page.confirm_alert()
            assert status == "Ok", "Wrong action in alert"

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            status, data = alert_page.prompt_alert()
            assert status == data, "Wrong data in alert"

