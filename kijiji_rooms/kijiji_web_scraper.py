import requests
import re

from bs4 import BeautifulSoup

class Room:
    price = ''
    title = ''

    link = ''
    distance = ''

    imageUrl = ''

def searchRooms(pageNum, minPrice, maxPrice, distance, location):

    #prepare url for kijiji and send request
    url= toUrl(str(pageNum), str(distance), str(location))
    response = requests.get(url)

    #get response and store it in a data structure
    html = BeautifulSoup(response.text, 'html.parser')
    
    searchItems = html.findAll('div', class_='search-item')

    rooms = []

    #get all the relevant data and store it in a 'rooms' list
    for item in searchItems:

        room = Room()

        try:
            room.price = item.find('div', class_='price').text.strip()
        except:
            print(url)

        if re.search('[a-zA-Z]', room.price) == None:   #if it actually has a price and not "Please Contact"

            priceFloat = float(room.price.strip('$').replace(',', ''))

            if not(minPrice <= priceFloat <= maxPrice):
                continue

        room.title = item.find('a', class_='title').string.strip()
        room.link = item.find('a', class_='title').get('href')
        room.distance = item.find('div', class_='distance').string.strip()
        room.imageUrl = item.find('img').get('data-src', None)

        if room.imageUrl == None:
            room.imageUrl = item.find('img')['src']
            
        rooms.append(room)

    return rooms

def toUrl(pageNum, distance, location):
    return 'https://www.kijiji.ca/b-for-rent/mississauga-peel-region/room/page-' + pageNum \
        + '/k0c30349001l1700276?' \
        +'&address=' + location + '&ad=offering&radius=' + distance + '&dc=true'