from selenium import webdriver
import time
import ssl
import chromedriver_binary  # Adds chromedriver binary to path


my_file = open("urls.txt", "r") 
driver = webdriver.Chrome()
for i in range(1, 80):
	for url in my_file:
		driver.get(url)
		time.sleep(1)
	driver.close()


driver = webdriver.Chrome()
driver.get("http://www.google.com")
time.sleep(2) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('coronavirus')
search_box.submit()
time.sleep(2) # Let the user actually see something!
driver.close()