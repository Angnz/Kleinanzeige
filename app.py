from flask import Flask, render_template
from scrape import scrape_kleinanzeige

app = Flask(__name__)

@app.route("/")
def index():
    # Call the scraping function to get listings
    listings = scrape_kleinanzeige()
    return render_template("index.html", listings=listings)

if __name__ == "__main__":
    app.run(debug=True)
