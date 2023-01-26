import scrapy
from scrapy.http import TextResponse


class QuotesSpider(scrapy.Spider):
    """Parse all quotes."""
    name = "quotes"
    start_urls = ['https://quotes.toscrape.com/page/1/']

    # Equal to `start_urls`
    # def start_requests(self):
    #     urls = [
    #         'https://quotes.toscrape.com/page/1/',
    #         'https://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: TextResponse):
        """Parse quotes information: text, author and tags."""
        # Default callback
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        
        # Recursively follow the link to the next page
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # Equal to `response.follow`
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
            yield response.follow(next_page, callback=self.parse)
