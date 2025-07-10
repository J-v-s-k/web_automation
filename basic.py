from selenium import webdriver
from selenium.webdriver.chrome.service import Service
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service=Service(executable_path="chromedriver.exe")

driver=webdriver.Chrome(options=options,service=service)
driver.maximize_window()
driver.get("https://www.google.com")


