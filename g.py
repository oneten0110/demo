from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver=webdriver.Chrome()
driver.get("https://demoblaze.com/#")
time.sleep(2)

driver.find_element(By.LINK_TEXT,"Laptops").click()
time.sleep(2)

print("successfully done")
driver.quit()