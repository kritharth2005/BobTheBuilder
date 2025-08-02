import scrapy
from bid_scraper.items import BidScraperItem

class BidsSpider(scrapy.Spider):
    name = "bids"
    allowed_domains = ["emma.maryland.gov"]
    start_urls = ["https://emma.maryland.gov/page.aspx/en/rfp/request_browse_public"]

    def parse(self, response):
        for row in response.css('tr[data-object-type="rfp"]'):
            cells = row.css('td[data-iv-role="cell"]')
            item = BidScraperItem()

            title = cells[2].css('a::text').get(default='').strip()
            href = cells[2].css('a::attr(href)').get()
            url = response.urljoin(href) if href else ''

            item['title'] = title
            item['url'] = url
            item['expiration_date'] = cells[4].css('::text').get(default='').strip()
            item['publish_date'] = cells[5].css('::text').get(default='').strip()
            item['category'] = cells[6].css('::text').get(default='').strip()
            item['solicitation_type'] = cells[7].css('::text').get(default='').strip()
            item['issuing_agency'] = cells[8].css('::text').get(default='').strip()

            yield item
