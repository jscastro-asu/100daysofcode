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
PATH = '/Users/jensmac/chromedriver'
TWITTER_EMAIL = 'jngkngekr@gmail.com'
TWITTER_PASSWORD = "Fakepwsdfd3!"
URL = 'https://www.speedtest.net/'
URL2 = 'https://twitter.com/login'
S = Service(PATH)

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

        username = self.driver.find_element(By.NAME, 'text')
        username.send_keys(TWITTER_EMAIL)
        time.sleep(2)

        next_btn = self.driver.find_element(By.XPATH, '//span[text()="Next"]')
        next_btn.click()
        time.sleep(3)

        username2 = self.driver.find_element(By.NAME, 'text')
        username2.send_keys("offsecjen")
        time.sleep(2)

        next_btn = self.driver.find_element(By.XPATH, '//span[text()="Next"]')
        next_btn.click()
        time.sleep(3)

        pw = self.driver.find_element(By.NAME, 'password')
        pw.send_keys(TWITTER_PASSWORD)
        pw.send_keys(Keys.ENTER)
        time.sleep(3)

        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"My current @Xfinity download speed: {self.down}, upload speed: {self.up}. Promised speed 300 down, 10 up. I am Jen's bot.")
        time.sleep(3)

        tweet_btn = self.driver.find_element(By.XPATH, '//span[text()="Tweet"]')
        tweet_btn.click()


bot = InternetSpeedTwitterBot(PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
