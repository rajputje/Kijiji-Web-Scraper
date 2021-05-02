from flask import Flask, render_template
import kijiji_web_scraper

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", rooms = kijiji_web_scraper.rooms)

if __name__ == "__main__":
    app.run(debug=True)