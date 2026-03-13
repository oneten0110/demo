from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as Chromeoptions
from selenium.webdriver.edge.options import Options as Edgeoptions

import time
import os
import threading

GRID_URL="http://localhost:4444"

def run_test(option):
    driver=webdriver.Remote(command_executor=GRID_URL,options=option)
    ##drive=webdriver.Chrome()

    driver.get("file://" + os.path.abspath("c.html"))
    #driver.get("there u gone copy the path ")
    time.sleep(2)

    driver.find_element(By.ID,"pdfFile").send_keys(os.path.abspath("sample.pdf"))
    time.sleep(2)

    driver.find_element(By.ID,"convertBtn").click()
    time.sleep(8)

    driver.find_element(By.ID,"downloadBtn").click()
    time.sleep(2)

    driver.quit()

for opt in [Chromeoptions(),Edgeoptions()]:
    threading.Thread(target=run_test,args=(opt,)).start()

print("sucees grids")