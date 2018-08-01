import scrapy
from slashdot.items import SlashdotItem

class Slashdot(scrapy.Spider):
    name='scrape_slashdot'

    start_url = 'https://slashdot.org/'
    start_urls = [start_url]
    n_pages = 10
    for i in range(n_pages):
        start_urls.append(f"{start_url}?page={i}")

    def parse(self, response):
        print("Starting to parse:\n")
        hrefs = response.xpath("//span[contains(@class, 'story-title')]/a/@href").extract()
        for href in hrefs:
            url = "https:" + href
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = SlashdotItem()
        # returns a list
        descriptions = response.xpath("//article/div[contains(@class,'body')]//text()").extract()
        description = ""
        for elem in descriptions:
            description += elem.strip()
        story_bylines = response.xpath("//span[contains(@class, 'story-byline')]//text()").extract()
        story_byline = ""
        for elem in story_bylines:
            story_byline += elem.strip()
        title = response.xpath("//h2[contains(@class, 'story')]/span[contains(@class, 'story-title')]/a//text()").extract()[0].strip()

        item['description'] = description
        item['title'] = title
        item['story_byline'] = story_byline

        yield item
