# file: datascraper/spiders/example_spider.py
import scrapy
from datascraper import db_utils 

class ExampleSpider(scrapy.Spider):
    name = "datascraper"

    async def start(self):
        conn = db_utils.readurls_from_db()
        self.log(conn)
        urls = conn
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log(f"Page title: {response.text}")
