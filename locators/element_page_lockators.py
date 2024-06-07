from selenium.webdriver.common.by import By


class TextBoxPageLocators:
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


class RadioButtonPageLocators:
    YES_RADIO_ACTION = (By.XPATH, "//label[@for='yesRadio']")
    YES_RADIO_STATUS = (By.XPATH, "//input[@id='yesRadio']")
    IMP_RADIO_ACTION = (By.XPATH, "//label[@for='impressiveRadio']")
    IMP_RADIO_STATUS = (By.XPATH, "//input[@id='impressiveRadio']")
    CHECK_RADIO = (By.XPATH, "//span[@class='text-success']")


class WebTablesLocators:
    # add person form
    ADD_RECORD_BUTTON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT = (By.XPATH, "//input[@id='department']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")

    # table
    SEARCH_BOX_INPUT = (By.XPATH, "//input[@id='searchBox']")
    ALL_RECORDS = (By.XPATH, "//div[@class='rt-tr-group']")
    DELETE_BUTTON = (By.XPATH, "//span[@title='Delete']")
    UPDATE_BUTTON = (By.XPATH, "//span[@title='Edit']")
    SELECT_FIELD = (By.XPATH, "//select")


class ButtonPageLocators:
    CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    DOUBLE_CLICK_BUTTON = (By.XPATH, "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.XPATH, "//button[@id='rightClickBtn']")
    CHECK_CLICK_BUTTON = (By.XPATH, "//p[@id='dynamicClickMessage']")
    CHECK_RIGHT_CLICK_BUTTON = (By.XPATH, "//p[@id='rightClickMessage']")
    CHECK_DOUBLE_CLICK_BUTTON = (By.XPATH, "//p[@id='doubleClickMessage']")

class LinksPageLocators:
    SIMPLE_LINK = (By.XPATH, "//a[@id='simpleLink']")
    BROKEN_LINK = (By.XPATH, "//a[@id='bad-request']")