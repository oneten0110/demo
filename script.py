from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()

#here no broweswer opned insted im runining in docekr
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver=webdriver.Chrome(options=options)

driver.get("https://www.wikipedia.org/")

print(driver.title)

driver.quit()