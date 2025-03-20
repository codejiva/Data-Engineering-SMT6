import scrapy
from scrapy.crawler import CrawlerProcess

class CountriesSpider(scrapy.Spider):
    name = "countries"
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response):
        countries = response.css("div.country")

        for country in countries:
            yield {
                # pake string() buat ambil text dari <h3>
                "name": country.xpath("string(.//h3[@class='country-name'])").get(default="").strip(),
                "capital": country.css("span.country-capital::text").get(default="").strip(),
                "population": country.css("span.country-population::text").get(default="").strip(),
                "area": country.css("span.country-area::text").get(default="").strip(),
            }

# buat jalaninnya
process = CrawlerProcess(settings={
    "FEEDS": {
        "countries.json": {
            "format": "json",
            "indent": 4,
        }
    }
})

process.crawl(CountriesSpider)
process.start()