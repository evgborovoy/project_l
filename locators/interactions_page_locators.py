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

class DroppablePageLocators:
    SIMPLE_TAB = (By.XPATH, "//a[@id='droppableExample-tab-simple']")
    SIMPLE_TAB_DRAG = (By.XPATH, "//div[@id='draggable']")
    SIMPLE_TAB_DROP = (By.XPATH, "//div[@id='simpleDropContainer']/div[@id='droppable']")

    ACCEPT_TAB = (By.XPATH, "//a[@id='droppableExample-tab-accept']")
    ACCEPT_TAB_DRAG_ACCEPTABLE = (By.XPATH, "//div[@id='acceptable']")
    ACCEPT_TAB_DRAG_NOT_ACCEPTABLE = (By.XPATH, "//div[@id='notAcceptable']")
    ACCEPT_TAB_DROP = (By.XPATH, "//div[@id='acceptDropContainer']/div[@id='droppable']")

    PREVENT_TAB = (By.XPATH, "//a[@id='droppableExample-tab-preventPropogation']")
    PREVENT_TAB_DRAG = (By.XPATH, "//div[@id='dragBox']")
    PREVENT_NOT_GREEDY_OUTER = (By.XPATH, "//div[@id='notGreedyDropBox']/p")
    PREVENT_NOT_GREEDY_INNER = (By.XPATH, "//div[@id='notGreedyInnerDropBox']/p")
    PREVENT_GREEDY_OUTER = (By.XPATH, "//div[@id='greedyDropBox']/p")
    PREVENT_GREEDY_INNER = (By.XPATH, "//div[@id='greedyDropBoxInner']/p")

    REVERT_TAB = (By.XPATH, "//a[@id='droppableExample-tab-revertable']")
    WILL_REVERT = (By.XPATH, "//div[@id='revertable']")
    NOT_REVERT = (By.XPATH, "//div[@id='notRevertable']")
    DROP_REVERT = (By.XPATH, "//div[@id='revertableDropContainer']/div[@id='droppable']")

