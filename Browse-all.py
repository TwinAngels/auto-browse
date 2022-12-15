import os
import shutil
from selenium import webdriver
import time
import ssl
import chromedriver_binary  # Adds chromedriver binary to path
from selenium.common.exceptions import WebDriverException

source_folder = r"C:\AutoBrowse\Tenants\\"
destination_folder = r"C:\ProgramData\Skyhigh\SCP\Policy\Temp\\"

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path and remove old OPG
    source = source_folder + file_name
    destination = destination_folder + file_name
    os.remove(destination_folder + "SCPPolicy.opg")
    # copy only files
    if os.path.isfile(source):
        # Renaming and copy OPG file
        shutil.copy(source, destination)
        old_name = destination_folder + file_name
        new_name = destination_folder + "SCPpolicy.opg"
        os.rename(old_name, new_name)
        # Start Browsing action
        my_file = open("Urls-Full.txt", "r") 
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        driver = webdriver.Chrome(chrome_options=options)
        for i in range(1, 5):
            for url in my_file:
                try:
                    driver.get(url)
                    time.sleep(1)
                except WebDriverException:
                    print("page down")
            #driver.close()
            driver.quit();