from scrapy import signals


class EmptyFieldsLogger:
    """Extension for find empty fields in parsed data."""

    @classmethod
    def from_crawler(cls, crawler):
        """Connect signals to extension."""
        ext = cls()
        crawler.signals.connect(
            ext.spider_opened,
            signal=signals.spider_opened,
        )
        crawler.signals.connect(
            ext.item_scraped,
            signal=signals.item_scraped,
        )
        crawler.signals.connect(
            ext.spider_closed,
            signal=signals.spider_closed,
        )
        return ext

    def spider_opened(self, spider):
        """Save event class fields."""
        self.empty_fields = set(spider.event_class.fields.keys())

    def item_scraped(self, item, spider):
        """Handle scraped item data."""
        self._remove_filled_fields(item, spider)

    def _remove_filled_fields(self, item, spider):
        """Remove filled fields from set of empty fields."""
        for field, value in item._values.items():
            if value:
                self.empty_fields.discard(field)

    def spider_closed(self, spider):
        """Print logs with empty fields names."""
        spider.logger.warning(
            "Empty fields detected:\n"
            + "\n".join(self.empty_fields)
        )
