import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

def init_driver() -> WebDriver:
    """Initialize and return the Selenium WebDriver."""
    options = Options()
    options.add_argument('--headless')  # Run in headless mode (without UI)
    options.add_argument('--no-sandbox')  # Required for certain environments
    options.add_argument('--disable-dev-shm-usage')  # To avoid errors in Docker
    options.add_argument('--disable-gpu')  # Disable GPU for better performance in headless mode
    options.add_argument('--remote-debugging-port=9222')  # For debugging if needed

    # Initialize the ChromeDriver (it will use the latest version automatically)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_listings():
    """Scrape the listings from the specified eBay Kleinanzeigen page."""
    url = 'https://www.kleinanzeigen.de/s-bestandsliste.html?userId=56130477'

    driver = init_driver()
    driver.get(url)
    time.sleep(3)  # Wait for the page to load (you can adjust this)

    # Scroll down to load more content if needed (if there are multiple pages or scrollable content)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Wait for new items to load

    # You may need to adjust the selectors depending on how the listings are structured on the page.
    listings = driver.find_elements(By.CLASS_NAME, 'ad-listing')  # Adjust according to your page structure

    # Loop through the listings and print the title and link of each
    for listing in listings:
        title = listing.find_element(By.CLASS_NAME, 'ad-title').text
        link = listing.find_element(By.TAG_NAME, 'a').get_attribute('href')
        print(f"Title: {title}\nLink: {link}\n")

    # Close the driver after scraping
    driver.quit()

# Call the function to start scraping
if __name__ == '__main__':
    try:
        scrape_listings()
    except Exception as e:
        print(f"Error occurred while scraping: {e}")
