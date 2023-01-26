from .quotes_spider import QuotesSpider
import scrapy


class TagQuotesSpider(QuotesSpider):
    """Parse quotes with a specific tag."""
    name = "tag-quotes"

    def start_requests(self):
        url = 'https://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)
