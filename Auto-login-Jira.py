#Download the chromedriver for th version of Chrome you have on your System
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r"path to hromedriver.exe")
driver.get("YOUR URL for jira login page")
username='abc@cdf.com'
login_email = driver.find_element_by_id('username').send_keys(username)
login = driver.find_element_by_id('login-submit').click()
time.sleep(5) #In case where there is only login email and after pressing continue the webpage asks for password
password='password'
login_password = driver.find_element_by_id('password').send_keys(password)
login = driver.find_element_by_id('login-submit').click()

