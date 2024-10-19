import scrapy
import json

class FlipkartProductSpider(scrapy.Spider):
    name = 'product_flipkart'
    allowed_domains = ['flipkart.com']

    def __init__(self, product_url=None, *args, **kwargs):
        super(FlipkartProductSpider, self).__init__(*args, **kwargs)
        self.output_file = 'flipkart_products.json'
        self.product_url = product_url  # Store the URL from run_spider.py
        if product_url:
            self.start_urls = [product_url]
        else:
            self.start_urls = []

    def parse(self, response):
        """Extract product details."""
        # Extract the product title, price, and categories using Scrapy selectors
        title = response.css('.VU-ZEz::text').get()
        unavailable = response.css('.QqFHMw.vslbG+._3Yl67G._7Pd1Fp::attr(disabled)').get()
        availability = True
        if unavailable:
            availability = False
        price = response.css('div.Nx9bqj.CxhGGd::text').get()
        categories = response.css('.r2CdBx .R0cyWM::text').getall()[1:-2]

        scraped_data = {
            'request-status': 'OK',
            'product-title': title,
            'availability':availability,
            'price': price,
            'categories': categories
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