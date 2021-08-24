from flask import Flask, render_template, request, session

import json
import os

import kijiji_web_scraper
from kijiji_web_scraper import SearchVariables

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config['SECRET_KEY'] = os.urandom(24)

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
    
    #if this is a new session, set default values
    if session.get('session_exists') == None:
        session['session_exists'] = True
        searchVars = SearchVariables(DEF_MIN_PRICE, DEF_MAX_PRICE, DEF_DISTANCE, DEF_LOCATION)
    #else get values from input fields and session variables
    else:
        searchVars = _getInputSearchVars(request.args)        
    
    #update session variables
    _setSessionSearchVars(searchVars.minPrice, searchVars.maxPrice, searchVars.distance, searchVars.location) 

    rooms = kijiji_web_scraper.searchRooms(pageNum, searchVars)

    return render_template("home.html", pageNum = pageNum, rooms = rooms, minPrice = searchVars.minPrice,\
                        maxPrice = searchVars.maxPrice, distance = searchVars.distance, location = searchVars.location)

def _getInputSearchVars(requestArgs: dict) -> SearchVariables:
    '''
    Get variables from input fields in the html file. Gives previously set values if input field is empty.
    '''

    minPrice = requestArgs.get("min_price")
    maxPrice = requestArgs.get("max_price")
    distance = requestArgs.get("distance")
    location = requestArgs.get("location")

    sv = SearchVariables()
    sv.minPrice = session['minPrice'] if minPrice == "" or minPrice is None else float(minPrice)
    sv.maxPrice = session['maxPrice'] if maxPrice == "" or maxPrice is None else float(maxPrice)
    sv.distance = session['distance'] if distance == "" or distance is None else float(distance)
    sv.location = session['location'] if location == "" or location is None else location

    return sv

def _setSessionSearchVars(minPrice: float, maxPrice: float, distance: float, location: str):
    '''
    Set search variables stored in session
    '''
    session['minPrice'] = minPrice
    session['maxPrice'] = maxPrice
    session['distance'] = distance
    session['location'] = location

if __name__ == "__main__":

    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))