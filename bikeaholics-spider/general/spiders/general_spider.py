from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.linkextractors import LinkExtractor


class GeneralSpider(Spider):
    name = 'general'

    def __init__(self, *args, **kwargs):
        super(GeneralSpider, self).__init__(*args, **kwargs)
        self.le = LinkExtractor()

    def parse(self, response):
        if not isinstance(response, HtmlResponse):
            return

        # import pdb; pdb.set_trace()
        yield {"body": response.body}

        for link in self.le.extract_links(response):
            if not link.url.startswith("http://www.bikeaholics.org"):
                continue

            r = Request(url=link.url)
            r.meta.update(link_text=link.text)
            yield r
