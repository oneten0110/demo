from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver=webdriver.Chrome()
driver.get("file:///C:/Users/admin/Desktop/foundation/a.html")
time.sleep(2)

driver.find_element(By.ID,"username").send_keys("kumar")
time.sleep(2)

driver.find_element(By.NAME,"password").send_keys("1234")
time.sleep(2)

driver.find_element(By.TAG_NAME,"input").send_keys("muthu")
time.sleep(2)

driver.find_element(By.LINK_TEXT,"Forgot Password?").click()
time.sleep(2)

alert=Alert(driver)
print("alert:",alert.text)
alert.accept()

driver.find_element(By.XPATH,"//button[contains(@class,'submitBtn')]").click()
time.sleep(2)

alert=Alert(driver)
print("alert:",alert.text)
alert.accept()

driver.find_element(By.CSS_SELECTOR,".submitBtn").click()

alert=Alert(driver)
print("alert:",alert.text)
alert.accept()

driver.find_element(By.ID,"loginBtn").click()
time.sleep(2)

print("All seleniyum works")
driver.quit()             