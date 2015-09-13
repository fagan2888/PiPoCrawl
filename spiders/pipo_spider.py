import scrapy
from PiPoCrawl.items import PipocrawlItem


class PipocrawlSpider(scrapy.Spider):
    name = "pipo"
    allowed_domains = ["econ.sciences-po.fr"]
    start_urls = [
        "http://econ.sciences-po.fr/"
    ]

    def parse(self, response):
        events = response.selector.xpath("//div[@class='my_agenda']")
        for seminar in events:
            #NOTE: You need to include the period in the xpath expression to
            # make it relative.  Otherwise, you will start from the begining
            #NOTE: Including the text() specification in the xpath drops the
            # html surrounding the content
            item = PipocrawlItem()
            item['date'] = seminar.xpath(".//strong/text()").extract_first()
            item['title'] = seminar.xpath(".//span[@class='titre']")
            item['title'] = item['title'].xpath(".//a/text()").extract()
            item['description'] = seminar.xpath(".//span[@class='desc']/text()"
                                                ).extract()
            yield item
