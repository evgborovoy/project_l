from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST_TAB = (By.XPATH, "//a[@id='demo-tab-list']")
    LIST_MENU = (By.XPATH, "//div[contains(@class,'vertical-list-container')]/div")
    GRID_TAB = (By.XPATH, "//a[@id='demo-tab-grid']")
    GRID_MENU = (By.XPATH, "//div[contains(@class,'create-grid')]/div")


class SelectablePageLocators:
    LIST_TAB = (By.XPATH, "//a[@id='demo-tab-list']")
    LIST_MENU = (By.XPATH, "//ul[contains(@id, 'verticalListContainer')]/li")
    LIST_MENU_ACTIVE = (By.XPATH, "//ul[contains(@id, 'verticalListContainer')]/li[contains(@class, 'active')]")
    GRID_TAB = (By.XPATH, "//a[@id='demo-tab-grid']")
    GRID_MENU = (By.XPATH, "//div[contains(@class, 'grid-container')]//li")
    GRID_MENU_ACTIVE = (By.XPATH, "//div[contains(@class, 'grid-container')]//li[contains(@class, 'active')]")

class ResizablePageLocators:
    BOX = (By.XPATH, "//div[@id='resizableBoxWithRestriction']")
    BOX_HANDLE = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction'] span[class^='react-resizable-handle']")
    WINDOW = (By.XPATH, "//div[@id='resizable']")
    WINDOW_HANDLE = (By.CSS_SELECTOR, "div[id='resizable'] span[class^='react-resizable-handle']")

