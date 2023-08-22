import scrapy

class PropertySpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["rahatemlak.az"]
    start_urls = [
        "https://rahatemlak.az/kiraye?page=1",
        "https://rahatemlak.az/alqi-satqi?page=1"
    ]

    def parse(self, response):
        for link in response.css('.item-box a.caption::attr(href)').getall():
            yield scrapy.Request(url=link, callback=self.parse_content)

        next_page = response.css(".pagination a[rel='next']::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_content(self, response):
        try:
            owner = response.css('td span.bolder.text-left.color-theme.font-14::text').get()
        except AttributeError:
            owner = None

        try:
            owner_category = response.css('td span.text-right.color-theme.font-14::text').get()
        except AttributeError:
            owner_category = None

        try:
            phone = response.css('span.color-theme.font-14 a::attr(href)').get()
        except AttributeError:
            phone = None

        yield {
            'link': response.url,
            'owner': owner,
            'owner_category': owner_category,
            'phone': phone
        }
