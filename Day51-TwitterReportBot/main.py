# Twitter internet speed complaint bot

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

PROMISED_DOWN = 150
PROMISED_UP = 10

SPEEDTEST_URL = 'https://www.speedtest.net/'
TWITTER_URL = 'https://twitter.com/'

TWITTER_EMAIL = 'YOUR_EMAIL'
TWITTER_HANDLE = '@YOUR_TWITTER_HANDLE'
TWITTER_PASSWORD = 'MYPASSWORD'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.go_button = None
        self.path_go_button = None
        self.chrome_driver = None
        self.provider = ""
        self.up = 0
        self.down = 0

    def get_internet_speed(self, web_url=SPEEDTEST_URL):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.chrome_driver = webdriver.Chrome(options=chrome_options)
        self.chrome_driver.get(url=web_url)

        # trigger test by clicking "GO" button
        self.path_go_button = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        self.go_button = self.chrome_driver.find_element(By.XPATH, value=self.path_go_button)
        self.go_button.click()

        time.sleep(60)
        # Find popup window
        popup = '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button'

        # Close popup window
        self.chrome_driver.find_element(by=By.XPATH, value=popup).click()
        self.down = self.chrome_driver.find_element(by=By.CLASS_NAME, value="download-speed").text
        self.up = self.chrome_driver.find_element(by=By.CLASS_NAME, value="upload-speed").text
        self.provider = self.chrome_driver.find_element(by=By.CLASS_NAME, value="result-label").text
        time.sleep(10)

    def display(self):
        print(
            f"Internet test speed result for {self.provider}:\nUpload speed: {self.up}Mbps\nDownload speed: {self.down}Mbps")

    def tweet_at_provider(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.chrome_driver = webdriver.Chrome(options=chrome_options)
        self.chrome_driver.get("https://twitter.com/home")
        time.sleep(10)
        email_input = self.chrome_driver.find_element(By.XPATH,
                                                      "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_input.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)

        try:
            pass_input = self.chrome_driver.find_element(By.XPATH,
                                                         "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")

            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = self.chrome_driver.find_element(By.XPATH,
                                                       "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            username.send_keys(
                TWITTER_HANDLE)  # Your Username here in case Twitter asks for username before asking password
            username.send_keys(Keys.ENTER)
            time.sleep(5)
            pass_input = self.chrome_driver.find_element(By.XPATH,
                                                         "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)

        time.sleep(5)

        twit_input = self.chrome_driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        twit_input.send_keys(f"My Current Internet Speed is {self.down} Download and {self.up} Upload")
        time.sleep(5)

        post_button_loc = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]'
        post_button = self.chrome_driver.find_element(By.XPATH, post_button_loc)
        post_button.click()

        print("Tweet Done")
        time.sleep(20)
        self.chrome_driver.quit()
