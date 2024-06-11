import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    prefs = {
        "download.default_directory": f"{os.getcwd()}/assets",
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    options.page_load_strategy = "eager"
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver
