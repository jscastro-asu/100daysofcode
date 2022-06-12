from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = 'jdfhbvhfdbvhfo89@gmail.com'
PASSWORD = 'FakePAsswrd'
PHONE = '2061231234'


s = Service('/Users/jencastro/chromedriver')
driver = webdriver.Chrome(service=s)
url = 'https://www.linkedin.com/jobs/search/?f_AL=true&geoId=104116203&keywords=security%20engineer&location=Seattle%2C%20Washington%2C%20United%20States'
driver.get(url)


sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)


password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)

signin = driver.find_element(By.XPATH, '//button[text() = "Sign in"]')
signin.click()
time.sleep(3)

driver.maximize_window()
easy_apply = driver.find_element(By.XPATH, '//span[text()="Save"]')
easy_apply.click()



