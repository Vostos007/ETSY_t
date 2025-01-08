from selenium import webdriver
from selenium_stealth import stealth
from bs4 import BeautifulSoup
import time
import requests

def get_product_info(url):
    session = requests.Session()
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml'
    }
    
    response = session.get(url, headers=headers)
    json_data = response.json()
    
    title = json_data["title"]
    price = json_data["price"]
    description = json_data["description"]
    
    return (title, price, description)

if __name__ == "__main__":
    test_url = "https://www.etsy.com/listing/123456789/test-product"
    title, price, description = get_product_info(test_url)
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Description: {description}")