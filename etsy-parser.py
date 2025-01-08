from selenium import webdriver
from selenium_stealth import stealth
from bs4 import BeautifulSoup
import time
import json

class EtsyParser:
    def __init__(self):
        self.driver = self.init_webdriver()
    
    def init_webdriver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        driver = webdriver.Chrome(options=options)
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True)
        return driver
    
    def get_product_cards(self, url):
        self.driver.get(url)
        time.sleep(2)
        
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        cards = soup.select('div[data-listing-card-container]')
        
        products = []
        for card in cards:
            try:
                title = card.select_one('[data-listing-card-title-text]').text.strip()
                price = card.select_one('p[data-listing-card-price]').text.strip()
                seller = card.select_one('p[data-listing-card-shop-name]').text.strip()
                
                product = {
                    'title': title,
                    'price': price,
                    'seller': seller
                }
                products.append(product)
            except Exception as e:
                print(f"Error parsing card: {str(e)}")
                continue
        
        return products
    
    def close(self):
        if self.driver:
            self.driver.quit()

def main():
    parser = EtsyParser()
    try:
        search_url = "https://www.etsy.com/search?q=drops+air"
        products = parser.get_product_cards(search_url)
        
        print(f"Found {len(products)} products:")
        for product in products:
            print("\nProduct:")
            print(f"Title: {product['title']}")
            print(f"Price: {product['price']}")
            print(f"Seller: {product['seller']}")
            print("-" * 50)
            
    finally:
        parser.close()

if __name__ == "__main__":
    main()