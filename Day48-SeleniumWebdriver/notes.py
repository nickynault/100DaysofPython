from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={USER_AGENT}")
chrome_options.add_experimental_option("detach", True)  # keeps chrome open

driver = webdriver.Chrome(options=chrome_options)

# Grab different nearby pieces

# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1")
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")


# Grab all different ways

# driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')  # THIS IS OP USE THIS FOR REAL
# print(bug_link.text)


# Click and search

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)


# Enter contents and press button
driver.get("https://secure-retreat-92358.herokuapp.com")
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
first_name.send_keys("Rick")
last_name.send_keys("A")
email.send_keys("rick@email.com")
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()
