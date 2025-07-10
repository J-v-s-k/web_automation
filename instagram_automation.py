from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
service=Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(options=options,service=service)
driver.maximize_window()
driver.get("https://www.instagram.com")
wait=WebDriverWait(driver,15)
username=wait.until(EC.presence_of_element_located((By.NAME,"username")))
password=wait.until(EC.presence_of_element_located((By.NAME,"password")))
username.send_keys("j.v.s.krishna")
password.send_keys("xxxxxxxxxxxxxx")
login=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button')))
login.click()
save_info=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/section/div/button')))
save_info.click()
