from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    NEW_TAB = (By.XPATH, "//button[@id='tabButton']")
    NEW_WINDOW = (By.XPATH, "//button[@id='windowButton']")
    NEW_WINDOW_TEXT = (By.XPATH, "//h1[@id='sampleHeading']")