import requests
import re

from bs4 import BeautifulSoup

class Room:
    price = ''
    title = ''

    link = ''
    distance = ''

    imageUrl = ''

class SearchVariables:
    minPrice = 0
    maxPrice = 0
    distance = 0
    location = ''

    def __init__(self, minPrice=0, maxPrice=0, distance=0, location=''):
        self.minPrice = minPrice
        self.maxPrice = maxPrice
        self.distance = distance
        self.location = location

def searchRooms(pageNum, searchVars: SearchVariables):

    #prepare url for kijiji and send request
    url= toUrl(str(pageNum), str(searchVars.distance), str(searchVars.location))
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
            print("Failed to find and strip div of class price in the following item" + item)
            room.price = 'N/A'

        if re.search('[a-zA-Z]', room.price) == None:   #if it actually has a price and not "Please Contact"

            priceFloat = float(room.price.strip('$').replace(',', ''))

            if not(searchVars.minPrice <= priceFloat <= searchVars.maxPrice):
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