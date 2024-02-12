# Amazon Price Tracker w Beautiful Soup

import requests
import lxml
from bs4 import BeautifulSoup

AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(AMAZON_URL,
                        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                                 "Accept-Language": "en-US,en;q=0.9"
                                 })
contents = response.text

soup = BeautifulSoup(contents, 'lxml')

start_price = soup.find(class_="a-price-whole")
price_fraction = soup.find(class_="a-price-fraction")
price = start_price.text + price_fraction.text
price = float(price)
print(price)

