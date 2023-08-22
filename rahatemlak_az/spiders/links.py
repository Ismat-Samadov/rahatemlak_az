import scrapy


class LinksSpider(scrapy.Spider):
    name = "links"
    allowed_domains = ["rahatemlak.az"]
    start_urls = ["https://rahatemlak.az/kiraye?page=1",
                  "https://rahatemlak.az/alqi-satqi?page=1"]

    def parse(self, response):
        for link in response.css('.item-box a.caption::attr(href)').getall():
            yield {
                'link': link
            }

        next_page = response.css(".pagination a[rel='next']::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
