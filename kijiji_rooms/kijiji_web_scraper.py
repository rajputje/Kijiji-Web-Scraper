import requests

from bs4 import BeautifulSoup

class Room:
    price = ''
    title = ''

    link = ''
    distance = ''

    imageUrl = ''

class SearchVariables:
    minPriceEnabled = True
    maxPriceEnabled = True
    minPrice = 0
    maxPrice = 0
    distance = 0
    location = ''

    def __init__(self, minPrice=0, maxPrice=0, minPriceEnabled = True, maxPriceEnabled = True, distance=0, location=''):
        self.minPrice = minPrice
        self.maxPrice = maxPrice
        self.minPriceEnabled = minPriceEnabled
        self.maxPriceEnabled = maxPriceEnabled
        self.distance = distance
        self.location = location

def searchRooms(pageNum, searchVars: SearchVariables):

    #prepare url for kijiji and send request
    url= toUrl(str(pageNum), searchVars)
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

        room.title = item.find('a', class_='title').string.strip()
        room.link = item.find('a', class_='title').get('href')
        room.distance = item.find('div', class_='distance').string.strip()
        room.imageUrl = item.find('img').get('data-src', None)

        if room.imageUrl == None:
            room.imageUrl = item.find('img')['src']
            
        rooms.append(room)

    return rooms

def toUrl(pageNum, searchVars):
    if(searchVars.minPriceEnabled or searchVars.maxPriceEnabled):
        minPrice = str(searchVars.minPrice) if searchVars.minPriceEnabled else ""
        maxPrice = str(searchVars.maxPrice) if searchVars.maxPriceEnabled else ""
        priceArg = '&price=' + minPrice + '__' + maxPrice
    else:
        priceArg = ''
    
    return 'https://www.kijiji.ca/b-for-rent/mississauga-peel-region/room/page-' + str(pageNum) \
        + '/k0c30349001l1700276?' + '&address=' + str(searchVars.location) + '&ad=offering&radius=' + str(searchVars.distance) \
             + '&dc=true' + priceArg