# Selenium Bot day. will use the bot, do a automated game bot, etc

from selenium import webdriver
from selenium.webdriver.common.by import By

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={USER_AGENT}")
chrome_options.add_experimental_option("detach", True)  # keeps chrome open

driver = webdriver.Chrome(options=chrome_options)

driver.quit()
