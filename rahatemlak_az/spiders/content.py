import scrapy


class ContentSpider(scrapy.Spider):
    name = "content"
    allowed_domains = ["rahatemlak.az"]
    start_urls = ["https://rahatemlak.az/elan/292714-baki-nerimanov-3-otaqli-ofis-kiraye-verilir"]

    def parse(self, response):
        yield {
            'owner': response.css('td span.bolder.text-left.color-theme.font-14::text').get(),
            'owner_category': response.css('td span.text-right.color-theme.font-14::text').get(),
            'phone': response.css('span.color-theme.font-14 a::attr(href)').get()
        }
