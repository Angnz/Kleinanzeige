import requests
from bs4 import BeautifulSoup

def scrape_kleinanzeige():
    # Your Kleinanzeigen listings URL
    URL = "https://www.kleinanzeigen.de/s-bestandsliste.html?userId=56130477"
    
    try:
        # Fetch the page content
        response = requests.get(URL)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract listings
        listings = []
        for item in soup.select('.ad-listitem'):
            # Update these selectors based on your HTML structure
            title = item.select_one('.text-module-begin').text.strip()
            price = item.select_one('.aditem-main--middle--price').text.strip()
            url = item.select_one('a')['href']
            listings.append({
                "title": title,
                "price": price,
                "url": f"https://www.kleinanzeigen.de{url}"
            })
        
        return listings

    except Exception as e:
        print(f"Error occurred while scraping: {e}")
        return []
