# opens speedtest link and runs the test
# once completed, it opens twitter login
# it aill auto login then will tweet the speed results.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

DOWNLOAD = 300
UPLOAD = 10
PATH = '/Users/jencastrochromedriver'
TWITTER_EMAIL = 'Jvhbdfvbfif@gmail.com'
TWITTER_PASSWORD = "Fakepassword!"
URL = 'https://www.speedtest.net/'
URL2 = 'https://twitter.com/login'
S = Service('/Users/jencastro/chromedriver')

class InternetSpeedTwitterBot:


    def __init__(self,s):
        self.driver = webdriver.Chrome(service=S)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):

        self.driver.get(URL)
        go = self.driver.find_element(By.XPATH, '//span[text()="Go"]')
        go.click()

        time.sleep(40)

        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        #print(f"My Xfinity download speed:{self.down}")
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        #print(f"My Xfinity upload speed:{self.up}")


    def tweet_at_provider(self):
        self.driver.get(URL2)
        time.sleep(2)

        username = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_EMAIL)

        next_btn = self.driver.find_element(By.XPATH, '//span[text()="Next"]')
        next_btn.click()
        time.sleep(3)

        pw = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pw.send_keys(TWITTER_PASSWORD)
        pw.send_keys(Keys.ENTER)
        time.sleep(15)

        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"My current Xfinity download speed: {self.down}, upload speed: {self.up}")
        time.sleep(3)
        tweet_btn = self.driver.find_element(By.XPATH, '//button[text()="Tweet"]')
        tweet_btn.click()

        self.driver.quit()

bot = InternetSpeedTwitterBot(PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
