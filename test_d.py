import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
def test_sample(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    username=driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    time.sleep(2)
   

    password=driver.find_element(By.NAME,"password")
    password.send_keys("secret_sauce")
    time.sleep(2)
    
    driver.find_element(By.ID,"login-button").click()
    time.sleep(2)

    driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    print("product has been added")
    time.sleep(1)

    driver.find_element(By.NAME,"add-to-cart-sauce-labs-bike-light").click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    time.sleep(2)

    driver.find_element(By.ID,"checkout").click()
    time.sleep(2)

    username=driver.find_element(By.NAME,"firstName")
    username.send_keys("kathir")
    time.sleep(2)
    
    username=driver.find_element(By.NAME,"lastName")
    username.send_keys("velan")
    time.sleep(2)

    username=driver.find_element(By.NAME,"postalCode")
    username.send_keys("604407")
    time.sleep(2)

    driver.find_element(By.ID,"continue").click()
    time.sleep(2) 

    driver.find_element(By.ID,"finish").click()
    right=driver.find_element(By.CLASS_NAME,"complete-header").text
    assert "Thank you for your order!" in right 
    
    driver.find_element(By.ID,"back-to-products").click()
    time.sleep(2)

    driver.find_element(By.ID,"react-burger-menu-btn")
    time.sleep(2)

    driver.find_element(By.ID,"logout_sidebar_link")
    time.sleep(2)         
    
