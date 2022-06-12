from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service('/Users/jennielyncastro/chromedriver')
browser = webdriver.Chrome(service=s)


# browser.get('https://en.wikipedia.org/wiki/Main_Page')
# article_count = browser.find_element(By.CSS_SELECTOR, '#articlecount a')
# article_count.click()

# current_events = browser.find_element(By.LINK_TEXT, "Current events")
# current_events.click()
#
# search_for = browser.find_element(By.NAME, "search")
# search_for.send_keys("Python (programming language)")
# search_for.send_keys(Keys.ENTER)



browser.get('http://secure-retreat-92358.herokuapp.com/')
fname = browser.find_element(By.NAME, "fName")
fname.send_keys("Jennielyn")

lname = browser.find_element(By.NAME, "lName")
lname.send_keys("Castro")

email = browser.find_element(By.NAME, "email")
email.send_keys('jencastro@email.com')

submit = browser.find_element(By.XPATH, '//button[text()="Sign Up"]')
submit.click()
