from flask import Flask, render_template, request

import json
import os

import kijiji_web_scraper
from kijiji_web_scraper import SearchVariables

app = Flask(__name__)

#get api key from json file
with open("./keys/api_keys.json") as api_keys:
    api_key_dict = json.loads(api_keys.read())

#injecting api key to the template
@app.context_processor
def maps_api_key():
    return dict(API_KEY=api_key_dict["API_KEY"])

DEF_MIN_PRICE = 450
DEF_MAX_PRICE = 700
DEF_DISTANCE = 10
DEF_LOCATION = 'Deerfield Drive, Nepean, ON'

@app.route("/")
@app.route("/<pageNum>")

def home(pageNum = 1):

    if request.args:
        searchVars = _getInputSearchVars(request.args)        
    else:
        searchVars = SearchVariables(DEF_MIN_PRICE, DEF_MAX_PRICE, True, True, DEF_DISTANCE, DEF_LOCATION)

    rooms = kijiji_web_scraper.searchRooms(pageNum, searchVars)

    return render_template("home.html", pageNum = pageNum, rooms = rooms, searchVars = searchVars.__dict__)

def _getInputSearchVars(requestArgs: dict) -> SearchVariables:
    '''
    Get variables from input fields in the html file. Gives default values for unset variables.
    '''

    if requestArgs:
        minPrice = requestArgs.get("min_price")
        maxPrice = requestArgs.get("max_price")
        distance = requestArgs.get("distance")
        location = requestArgs.get("location")
        minPriceEnabled = requestArgs.get("min_price_chk")
        maxPriceEnabled = requestArgs.get("max_price_chk")

        sv = SearchVariables()
        sv.minPrice = 0 if minPrice == "" or minPrice is None else float(minPrice)
        sv.maxPrice = 0 if maxPrice == "" or maxPrice is None else float(maxPrice)
        sv.distance = 1 if distance == "" or distance is None else float(distance)
        sv.location = "Canada" if location == "" or location is None else location
        sv.minPriceEnabled = False if minPriceEnabled == "undefined" or minPriceEnabled is None else True
        sv.maxPriceEnabled = False if maxPriceEnabled == "undefined" or maxPriceEnabled is None else True
    
    return sv

if __name__ == "__main__":

    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))