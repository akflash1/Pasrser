pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
url = "https://viva-art.com.ua/ua/g4231240-frezera-dlya-manikyura"

if response.status_code == 200:
    html = response.text
else:
    exit()

soup = BeautifulSoup(html, 'html.parser')

prices = soup.find_all('')

new_price = "prices.txt"

with open(new_price, 'w') as file:
    for price in prices:
        file.write(price.text + '\n')

print("Цены успешно записаны в", new_price)

