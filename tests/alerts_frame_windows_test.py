import time

from pages.alerts_frame_windows_page import BrowserWindows, AlertsPage, FramePage, NestedFramePage, ModalDialogsPage


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

    class TestFrames:

        def test_frames(self, driver):
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result = frame_page.check_frame()
            expected = ['frame1:This is a sample page', 'frame2:This is a sample page']
            assert result == expected, "Failed to switch to frame"

    class TestNestedFrames:

        def test_nested_frames(self, driver):
            frame_page = NestedFramePage(driver, "https://demoqa.com/nestedframes")
            frame_page.open()
            result = frame_page.check_nested_frames()
            expected = ["Parent frame", "Child Iframe"]
            print(result)
            assert result == expected

    class TestModalDialogs:
        def test_small_modal_text(self, driver):
            modal_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_page.open()
            result = modal_page.small_modal_text()
            expected = "This is a small modal"
            assert expected in result, "Failed to open small modal"

        def test_small_modal_overlay_close(self, driver):
            modal_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_page.open()
            result = modal_page.small_modal_close_overlay()
            assert result, "Small modal not close"

        def test_large_modal(self, driver):
            modal_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_page.open()
            result = modal_page.large_modal_text()
            expected = "Lorem Ipsum"
            assert expected in result, "Failed to open large modal"

        def test_large_modal_overlay_close(self, driver):
            modal_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_page.open()
            result = modal_page.large_modal_close_overlay()
            assert result, "Large modal not close"
