import requests
import re

from bs4 import BeautifulSoup

class Room:
    price = ''
    title = ''

    link = ''
    distance = ''

    imageUrl = ''

def searchRooms(pageNum, minPrice, maxPrice, distance):

    url= getUrl(str(pageNum), str(distance))
    response = requests.get(url)

    html = BeautifulSoup(response.text, 'html.parser')
    infoList = html.findAll('div', class_='search-item')

    rooms = []

    for info in infoList:

        room = Room()

        try:
            room.price = info.find('div', class_='price').text.strip()
        except:
            print(url)

        if re.search('[a-zA-Z]', room.price) == None:   #if it actually has a price and not "Please Contact"

            priceFloat = float(room.price.strip('$').replace(',', ''))

            if not(minPrice <= priceFloat <= maxPrice):
                continue

        room.title = info.find('a', class_='title').string.strip()
        room.link = info.find('a', class_='title').get('href')
        room.distance = info.find('div', class_='distance').string.strip()
        room.imageUrl = info.find('img').get('data-src', None)

        if room.imageUrl == None:
            room.imageUrl = info.find('img')['src']
            
        rooms.append(room)

    return rooms

def getUrl(pageNum, distance):
    return 'https://www.kijiji.ca/b-for-rent/mississauga-peel-region/room/page-' + pageNum \
        + '/k0c30349001l1700276?' \
        +'&address=Deerfield+Drive%2C+Nepean%2C+ON&ad=offering&radius=' + distance + '&dc=true'