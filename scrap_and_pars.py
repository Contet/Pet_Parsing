from bs4 import BeautifulSoup
import re
from requests import get
import time
import random

url = 'https://kursk.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p' + '=1&region=4835&room2=1'
houses = []
count = 1
print("Начинаю скрапинг, это может занять некоторое время!")
while count <= 2:
    url = 'https://kursk.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=' + str(count) + '&region=4835&room2=1'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    house_data = html_soup.find_all('div', re.compile(r'link'))
    if house_data != []:
        houses.extend(house_data)
        value = random.random()
        scaled_value = value * 6
        print(f'Скрапинг {count} страницы...')
        time.sleep(scaled_value)
    else:
        print("Объявления кончились, начинаю парсинг...")
        time.sleep(7)
        break
    count +=1
print("Объявления кончились, начинаю парсинг...")
time.sleep(7)
house = []
for link in houses:
    title = link.find('span', {'data-mark': 'OfferTitle'})
    subtitle = link.find('span', {'data-mark': 'OfferSubtitle'})
    price = link.find('span', {'data-mark': 'MainPrice'})

    house.append({
        'title': title.text if title else None,
        'subtitle': subtitle.text if subtitle else None,
        'price': price.text.replace('\xa0₽', '') if price else None,
    })

for numbers in range(len(house)):
    house_info = house[numbers]
    if house_info.get("price") and house_info.get("title") != None:
        print(f"{numbers + 1} квартира - {house_info.get(title)}, стоимостью - {house_info.get(price)} Рублей")
print(f"Парсинг завершен :D")