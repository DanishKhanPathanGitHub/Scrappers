from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from ProductScrapers.spiders.amazon_product import AmazonProductSpider
from ProductScrapers.spiders.flipkart_product import FlipkartProductSpider
from ProductScrapers.spiders.BookSwagan import BookSwaganProductSpider


def identify(url):
    """Identify the platform based on the URL."""
    if 'amazon.in' in url and ('/dp/' in url or '/d/' in url):
        return "Amazon"
    elif '/p/itm' in url and 'flipkart.com' in url:
        return "Flipkart"
    elif 'bookswagon.com/book/' in url:
        return "BookSwagon"
    else:
        print(f"Unsupported URL: {url}")
        return False

platformToSpider = {
    'Amazon':AmazonProductSpider,
    'Flipkart':FlipkartProductSpider,
    'BookSwagon':BookSwaganProductSpider
}
def run_spider(url):
    """Run the appropriate spider based on the identified platform."""
    platform = identify(url)

    if not platform:
        print("Invalid URL or unsupported platform.")
        return

    # Start the CrawlerProcess
    process = CrawlerProcess(get_project_settings())

    process.crawl(platformToSpider[platform], product_url=url)

    process.start()


if __name__ == "__main__":
    # Input the URL from the user
    url = input("Enter the product URL: \n")
    settings = get_project_settings()
    settings.set('LOG_LEVEL', 'ERROR')

    run_spider(url)
