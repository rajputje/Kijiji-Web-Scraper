from flask import Flask, render_template

import kijiji_web_scraper


app = Flask(__name__)


@app.route("/")
@app.route("/<pageNum>")

def home(pageNum = 1):

    rooms = kijiji_web_scraper.searchRooms(pageNum)

    return render_template("home.html", pageNum = pageNum, rooms = rooms)


if __name__ == "__main__":

    app.run(debug=True)