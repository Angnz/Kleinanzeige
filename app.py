from flask import Flask, render_template
from scrape import scrape_listings  # Import the scraping logic

app = Flask(__name__)

@app.route("/")
def home():
    listings = scrape_listings()  # Fetch data using the scraper
    return render_template("index.html", listings=listings)

if __name__ == "__main__":
    app.run(debug=True)
