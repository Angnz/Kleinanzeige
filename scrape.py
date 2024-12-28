import requests
from bs4 import BeautifulSoup

def scrape_kleinanzeige():
    # Your Kleinanzeigen listings URL
    URL = "https://www.kleinanzeigen.de/s-bestandsliste.html?userId=56130477"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    
    try:
        # Fetch the page content with headers
        response = requests.get(URL, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract listings (adjust these selectors based on the actual HTML structure)
        listings = []
        for item in soup.select('.ad-listitem'):
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
