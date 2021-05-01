import requests

from bs4 import BeautifulSoup


pageNum = 1

minPrice = 450

maxPrice = 700


url='https://www.kijiji.ca/b-for-rent/mississauga-peel-region/room/page-' + str(pageNum) + 'k0c30349001l1700276?rb=true&ll=43.733835%2C-79.823181&address=11965+Hurontario+Street%2C+Brampton%2C+ON&ad=offering&radius=11.0&dc=true'

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')


infoList = html.findAll('div', class_='info')

class Room:
    price = ''
    title = ''

    link = ''
    distance = ''

rooms = []

for info in infoList:

    room = Room()

    room.price = info.find('div', class_='price').string.strip()

    if room.price != 'Please Contact':

        priceFloat = float(room.price.strip('$').replace(',', ''))

        if not(minPrice <= priceFloat <= maxPrice):
            continue

    room.title = info.find('a', class_='title').string.strip()

    room.link = info.find('a', class_='title').get('href')

    room.distance = info.find('div', class_='distance').string.strip()

    print(room.__dict__)
    rooms.append(room)