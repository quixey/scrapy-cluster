
import datetime

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.linkextractors import LinkExtractor

from frontera.contrib.backends.sqlalchemy import revisiting


class GeneralSpider(Spider):
    name = 'general'

    def __init__(self, *args, **kwargs):
        super(GeneralSpider, self).__init__(*args, **kwargs)
        self.le = LinkExtractor()

    def parse(self, response):
        if not isinstance(response, HtmlResponse):
            return

        # Fields to work with -
        # response.url
        #         .body
        #         .encoding
        #         .headers
        #         .request                    <class 'scrapy.http.request.Request'>
        #         .meta["frontier_request"] { <class 'frontera.core.models.Request'>
        #            .meta {
        #              "crawl_at"
        #              "depth"
        #              "domain" {
        #                "fingerprint"
        #                "name"
        #                "netloc"
        #              }
        #              "fingerprint"
        #              "origin_is_frontier"
        #            }
        #          }

        # Missing from the party -
        # database fields score, created_at, fetched_at;

        self.logger.info("PARSE URL: {}".format(response.url))
        if response.url == "http://www.bikeaholics.org/ALoop.html":
            # import pdb; pdb.set_trace()
            self.logger.info("SETTING SPIDER SCHEDULE: {}".format(response.url))
            response.request.meta[b'spiderdate'] = revisiting.utcnow_timestamp() + datetime.timedelta(minutes=3).seconds

        yield {"body": response.body}

        for link in self.le.extract_links(response):
            if not link.url.startswith("http://www.bikeaholics.org"):
                continue

            r = Request(url=link.url)
            r.meta.update(link_text=link.text)
            yield r
