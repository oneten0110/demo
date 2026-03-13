from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("file:///C:/Users/admin/Desktop/foundation/exp.html")
time.sleep(2)

username=driver.find_element(By.ID,"username")
username.send_keys("kumar")
time.sleep(2)

password=driver.find_element(By.NAME,"password")
password.send_keys("1234")
time.sleep(2)

password=driver.find_element(By.NAME,"password").clear()
password=driver.find_element(By.NAME,"password").send_keys("445")
time.sleep(3)

text=driver.find_element(By.ID,"msg").text
print("text: ",text)

print("username: displayed?",driver.find_element(By.ID,"username").is_displayed())
print("button works?",driver.find_element(By.ID,"loginBtn").is_enabled())

driver.find_element(By.ID,"loginBtn").click()
time.sleep(2)

print("successfully done")
driver.quit()