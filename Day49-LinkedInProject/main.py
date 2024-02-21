# LinkedIn Auto bot that applies for jobs. I'll remove my email password on upload to GitHub, use your own.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

JOB_BOARD = ("https://www.linkedin.com/jobs/search/?currentJobId=3812214541&distance=25&f_AL=true&f_E=1%2C2%2C3&f_"
             "I=4%2C96%2C6%2C118%2C3231%2C24&f_JT=F%2CP%2CT%2CI&f_SB2=2&f_TPR=r2592000&f_WT=1%2C3%2C2&geoId=1029652"
             "50&keywords=software%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")
EMAIL = "email"
PASSWORD = "pass"
USER_AGENT = "Mozilla/5.0 ..."

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={USER_AGENT}")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(JOB_BOARD)

# Get to sign in page
time.sleep(1)
sign_in = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in.click()

# Sign In
time.sleep(1)
email_box = driver.find_element(By.ID, value="username")
password_box = driver.find_element(By.ID, value="password")
email_box.send_keys(EMAIL)
password_box.send_keys(PASSWORD)
password_box.send_keys(Keys.ENTER)

# Find the apply button
time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

# If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(PHONE)

# Submit the application
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()
