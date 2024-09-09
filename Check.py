from AmazonProductDetailScraper import main as AmazonScraper
from FlipcartProductScraper import main as FlipkartScraper


amazon_product_detail = AmazonScraper()
flipkart_product_detail = FlipkartScraper()

print(amazon_product_detail)
print(flipkart_product_detail)