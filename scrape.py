import requests
from bs4 import BeautifulSoup

def scrape_listings():
    URL = "https://www.kleinanzeigen.de/s-bestandsliste.html?userId=56130477"  # Replace with your actual URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        items = soup.find_all("article", class_="aditem")  # Adjust this based on your HTML structure
        listings = []
        for item in items:
            title = item.find("a", class_="ellipsis").text.strip()
            link = item.find("a", class_="ellipsis")["href"]
            listings.append({"title": title, "link": f"https://www.ebay-kleinanzeigen.de{link}"})
        return listings
    else:
        return []
