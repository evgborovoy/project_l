from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    NEW_TAB = (By.XPATH, "//button[@id='tabButton']")
    NEW_WINDOW = (By.XPATH, "//button[@id='windowButton']")
    NEW_WINDOW_TEXT = (By.XPATH, "//h1[@id='sampleHeading']")


class AlertsLocators:
    SIMPLE_ALERT_BUTTON = (By.XPATH, "//button[@id='alertButton']")
    APPEAR_ALERT_BUTTON = (By.XPATH, "//button[@id='timerAlertButton']")
    CONFIRM_ALERT_BUTTON = (By.XPATH, "//button[@id='confirmButton']")
    CONFIRM_ALERT_STATUS = (By.XPATH, "//span[@id='confirmResult']")
    PROMPT_ALERT_BUTTON = (By.XPATH, "//button[@id='promtButton']")
    PROMPT_ALERT_STATUS = (By.XPATH, "//span[@id='promptResult']")


class FramePageLocators:
    FRAME1 = "frame1"
    FRAME2 = "frame2"


class NestedFramePageLocators:
    PARENT_FRAME, CHILD_FRAME = 0, 0
    FRAME_TEXT = (By.XPATH, "//body")


class ModalDialogsPageLocators:
    SMALL_MODAL = (By.XPATH, "//button[@id='showSmallModal']")
    SMALL_MODAL_TEXT = (By.XPATH, "//div[@class='modal-body']")
    SMALL_MODAL_OVERLAY = (By.XPATH, "//div[@role='dialog']")
    LARGE_MODAL = (By.XPATH, "//button[@id='showLargeModal']")
    LARGE_MODAL_TEXT = (By.XPATH, "//div[@class='modal-body']")
    LARGE_MODAL_OVERLAY = (By.XPATH, "//div[@role='dialog']")
