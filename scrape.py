import random
import requests
from bs4 import BeautifulSoup

# List of common user agents to rotate through
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edge/91.0.864.59",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
]

def scrape_kleinanzeige():
    URL = "https://www.kleinanzeigen.de/s-bestandsliste.html?userId=56130477"
    
    session = requests.Session()
    
    headers = {
        "User-Agent": random.choice(user_agents)  # Randomly pick a User-Agent
    }
    
    try:
        response = session.get(URL, headers=headers)
        response.raise_for_status()  # Will raise an exception for HTTP errors
        
        # If scraping is successful, parse the content
        soup = BeautifulSoup(response.text, 'html.parser')
        
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

