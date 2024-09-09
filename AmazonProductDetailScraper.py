from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests



def verify_url_And_get_driver(url):
    service = Service(r"D:\Python\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", False)  # Keep browser open after script ends
    driver = webdriver.Chrome(service=service, options=options)
    
    domain = 'amazon.in'
    pattern = '/dp/'
    try:
        driver.get(url)
        return driver if domain in url and pattern in url else False
    except:
        return False
    
def main():
    PRODUCT_URL = input("Enter the url: \n")
    driver = verify_url_And_get_driver(PRODUCT_URL)

    if not driver:
        return {
            'request-status':'BAD',
        }

    
    driver.get(PRODUCT_URL)
    title = driver.find_element(By.ID, 'productTitle').text   
    price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
    categories_div = driver.find_element(By.ID, 'wayfinding-breadcrumbs_feature_div')
    categories = [element.text for element in categories_div.find_elements(By.CLASS_NAME, 'a-link-normal') ]
    
    return {
        'request-status':'OK',
        'product-title':title,
        'price':price,
        'categories':categories,
    }

if __name__=="__main__":
    main()
