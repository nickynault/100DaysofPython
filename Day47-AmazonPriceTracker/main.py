# Amazon Price Tracker w Beautiful Soup

import requests
from bs4 import BeautifulSoup
import smtplib

AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
BUY_PRICE = 200

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

title = soup.find(id="productTitle").get_text().strip()

if price < BUY_PRICE:
    message = f"{title} is now {price}!"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{AMAZON_URL}".encode("utf-8")
        )
