import time

from pages.alerts_frame_windows_page import BrowserWindows


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
