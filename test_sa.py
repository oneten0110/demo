from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()

def test_aa(driver):
    driver.get("https://www.w3schools.com/")
    time.sleep(5)

    search=driver.find_element(By.ID,"search2")
    search.send_keys("python")
    time.sleep(5)

    search.send_keys(Keys.RETURN)

    print(driver.title)
    assert True
