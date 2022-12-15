import os
from selenium import webdriver
import time
import ssl
import chromedriver_binary  # Adds chromedriver binary to path
from selenium.common.exceptions import WebDriverException

my_file = open("urls-validated.txt", "r") 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)
for i in range(1, 80):
	for url in my_file:
     try:
      driver.get(url)
      time.sleep(1)
    except WebDriverException:
            print("page down")
	driver.quit();