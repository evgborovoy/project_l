from selenium.webdriver.common.by import By


class TextBoxPageLockators:

    # Empty field
    FULL_NAME = (By.XPATH, "//input[@id='userName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")

    # Created info
    CREATED_FULL_NAME = (By.XPATH, "//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")

class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.XPATH, "//button[@aria-label='Expand all']")
    ALL_TITLES_LIST = (By.XPATH, "//span[@class='rct-title']")
    CHECKED_ITEMS_LOCATOR = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    SELECTED_ITEMS_LOCATOR = (By.XPATH, "//span[@class='text-success']")