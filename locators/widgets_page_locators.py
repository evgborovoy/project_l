from selenium.webdriver.common.by import By


class AccordianLocators:
    FIRST_SECTION = (By.XPATH, "//div[@id='section1Heading']")
    FIRST_SECTION_CONTENT = (By.XPATH, "//div[@id='section1Content']//p")
    FIRST_SECTION_SHOW = (By.XPATH, "(//div[@class='card']/div[2])[1]")
    SECOND_SECTION = (By.XPATH, "//div[@id='section2Heading']")
    SECOND_SECTION_CONTENT = (By.XPATH, "//div[@id='section2Content']//p")
    SECOND_SECTION_SHOW = (By.XPATH, "(//div[@class='card']/div[2])[2]")
    THIRD_SECTION = (By.XPATH, "//div[@id='section3Heading']")
    THIRD_SECTION_CONTENT = (By.XPATH, "//div[@id='section3Content']//p")
    THIRD_SECTION_SHOW = (By.XPATH, "(//div[@class='card']/div[2])[3]")


class AutoCompleteLocators:
    MULTIPLE_CONTAINER = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTIPLE_CONTAINER_VALUE = (By.XPATH, "//div[contains(@class,'auto-complete__multi-value__label')]")
    MULTIPLE_CONTAINER_VALUE_REMOVE = (By.XPATH, "//div[contains(@class,'auto-complete__multi-value__remove')]")
    MULTIPLE_CONTAINER_VALUE_REMOVE_ALL = (By.XPATH, "//div[contains(@class,'auto-complete__indicators')]")
    SINGLE_CONTAINER = (By.XPATH, "//input[@id='autoCompleteSingleInput']")
    SINGLE_CONTAINER_VALUE = (By.XPATH, "//div[contains(@class,'auto-complete__single-value')]")


class DatePickerLocators:
    DATE_FIELD = (By.XPATH, "//input[@id='datePickerMonthYearInput']")
    DATE_MONTH_FIELD = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    DATE_DAY_FIELD = (By.XPATH, "//div[contains(@class, 'react-datepicker__day react-datepicker__day')]")
    DATE_YEAR_FIELD = (By.XPATH, "//select[@class='react-datepicker__year-select']")

    DATE_AND_TIME_FIELD = (By.XPATH, "//input[@id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH_FIELD = (By.XPATH, "//div[@class='react-datepicker__month-read-view']")
    DATE_AND_TIME_MONTH_LIST = (By.XPATH, "//div[@class='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_FIELD = (By.XPATH, "//div[@class='react-datepicker__year-read-view']")
    DATE_AND_TIME_YEAR_LIST = (By.XPATH, "//div[@class='react-datepicker__year-option']")
    DATE_AND_TIME_DAY_FIELD = (By.XPATH, "//div[contains(@class, 'react-datepicker__day react-datepicker__day')]")
    DATE_AND_TIME_TIME_LIST = (By.XPATH, "//li[@class='react-datepicker__time-list-item ']")


class SliderPageLocators:
    SLIDER_INPUT = (By.XPATH, "//input[@type='range']")
    SLIDER_VALUE = (By.XPATH, "//input[@id='sliderValue']")


class ProgressBarLocators:
    START_STOP_BUTTON = (By.XPATH, "//button[@id='startStopButton']")
    PROGRESS_BAR = (By.XPATH, "//div[@role='progressbar']")


class TabsPageLocators:
    TAB_WHAT = (By.XPATH, "//a[@id='demo-tab-what']")
    TAB_WHAT_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-what']")
    TAB_ORIGIN = (By.XPATH, "//a[@id='demo-tab-origin']")
    TAB_ORIGIN_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-origin']")
    TAB_USE = (By.XPATH, "//a[@id='demo-tab-use']")
    TAB_USE_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-use']")


class ToolTipsPageLocators:
    BUTTON = (By.XPATH, "//button[@id='toolTipButton']")
    BUTTON_HOVERED = (By.XPATH, "//button[@aria-describedby='buttonToolTip']")
    INPUT_FIELD = (By.XPATH, "//input[@id='toolTipTextField']")
    INPUT_FIELD_HOVERED = (By.XPATH, "//input[@aria-describedby='textFieldToolTip']")
    CONTRARY = (By.XPATH, "//a[text()='Contrary']")
    CONTRARY_HOVERED = (By.XPATH, "//a[@aria-describedby='contraryTexToolTip']")
    TIP = (By.XPATH, "//div[@class='tooltip-inner']")

class MenuPageLocators:
    MENU_ITEM_LIST = (By.XPATH, "//ul[@id='nav']//li/a")