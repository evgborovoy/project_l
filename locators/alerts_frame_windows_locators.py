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
