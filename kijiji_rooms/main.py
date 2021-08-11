from flask import Flask, render_template, request

import kijiji_web_scraper


app = Flask(__name__)

DEF_MIN_PRICE = 450
DEF_MAX_PRICE = 700
DEF_DISTANCE = 10
DEF_LOCATION = 'Deerfield+Drive%2C+Nepean%2C+ON'

currMinPrice = DEF_MIN_PRICE
currMaxPrice = DEF_MAX_PRICE
currDistance = DEF_DISTANCE
currLocation = DEF_LOCATION

@app.route("/")
@app.route("/<pageNum>")

def home(pageNum = 1):

    global currMinPrice
    global currMaxPrice
    global currDistance
    global currLocation

    minPrice = request.args.get("min_price")
    maxPrice = request.args.get("max_price")
    distance = request.args.get("distance")
    location = request.args.get("location")

    minPrice = currMinPrice if minPrice == "" or minPrice is None else float(minPrice)
    maxPrice = currMaxPrice if maxPrice == "" or maxPrice is None else float(maxPrice)
    distance = currDistance if distance == "" or distance is None else float(distance)

    currMinPrice = minPrice
    currMaxPrice = maxPrice
    currDistance = distance
    currLocation = location

    rooms = kijiji_web_scraper.searchRooms(pageNum, minPrice, maxPrice, distance, location)

    return render_template("home.html", pageNum = pageNum, rooms = rooms, minPrice = minPrice, maxPrice = maxPrice,\
         distance = distance, location = location)

if __name__ == "__main__":

    app.run(debug=True)