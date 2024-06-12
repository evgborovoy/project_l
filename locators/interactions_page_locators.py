from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST_TAB = (By.XPATH, "//a[@id='demo-tab-list']")
    LIST_MENU = (By.XPATH, "//div[contains(@class,'vertical-list-container')]/div")
    GRID_TAB = (By.XPATH, "//a[@id='demo-tab-grid']")
    GRID_MENU = (By.XPATH, "//div[contains(@class,'create-grid')]/div")

