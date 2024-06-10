from selenium.webdriver.common.by import By


class Accordian:
    FIRST_SECTION = (By.XPATH, "//div[@id='section1Heading']")
    FIRST_SECTION_CONTENT = (By.XPATH, "//div[@id='section1Content']//p")
    FIRST_SECTION_SHOW = (By.XPATH, "(//div[@class='card']/div[2])[1]")
    SECOND_SECTION = (By.XPATH, "//div[@id='section2Heading']")
    SECOND_SECTION_CONTENT = (By.XPATH, "//div[@id='section2Content']//p")
    SECOND_SECTION_SHOW = (By.XPATH, "(//div[@class='card']/div[2])[2]")
    THIRD_SECTION = (By.XPATH, "//div[@id='section3Heading']")
    THIRD_SECTION_CONTENT = (By.XPATH, "//div[@id='section3Content']//p")
    THIRD_SECTION_SHOW = (By.XPATH, "(//div[@class='card']/div[2])[3]")
