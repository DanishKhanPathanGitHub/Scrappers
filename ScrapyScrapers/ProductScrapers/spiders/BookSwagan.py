import scrapy
import json

class BookSwaganProductSpider(scrapy.Spider):
    name = 'bookswagan_scraper'
    allowed_domains = ['bookswagan.com']

    def __init__(self, product_url=None, *args, **kwargs):
        super(BookSwaganProductSpider, self).__init__(*args, **kwargs)
        self.output_file = 'bookswagan_product_detail.json'
        
        # Store the URL passed from run_spider.py
        if product_url:
            self.start_urls = [product_url]
        else:
            self.start_urls = []

    def parse(self, response):
        # Scrape the title
        title = response.xpath('//span[@id="ctl00_phBody_ProductDetail_lblTitle"]/text()').get()

        # Extract availability
        availability = response.xpath('//span[@id="ctl00_phBody_ProductDetail_lblAvailable"]/text()').get()
        if availability == 'Out of Stock':
            availability = False
        else:
            availability = True
        # Extract price
        price = response.xpath('//div[@class="mobileprice"]/span[@class="a-price"]/text()').get()

        categories = response.css('div#categories div.col-sm-12 ul.list-unstyled.blacklistreview li a::text').getall()
        categories = [category.strip() for category in categories if category.strip()]  # Clean categories

        print(categories or None)
        # Prepare the scraped data
        scraped_data = {
            'request-status': 'OK',
            'product-title': title,
            'availability':availability,
            'price': price,
            'categories': categories,
        }

        # Write the scraped data to a CSV file
        self.write_to_json(scraped_data)

        # Return the scraped data
        return scraped_data

    def write_to_json(self, scraped_data):
        # Write or append data to a JSON file
        with open(self.output_file, 'a', encoding='utf-8') as jsonfile:
            json.dump(scraped_data, jsonfile, ensure_ascii=False, indent=4)
            jsonfile.write(',\n')  # To separate multiple entries
