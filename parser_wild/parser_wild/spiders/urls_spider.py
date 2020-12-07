import scrapy
from ..items import ParserWildUrl
from scrapy.crawler import CrawlerProcess

class Urls(scrapy.Spider):
    name = 'Urls'
    custom_settings = {
        'ITEM_PIPELINES': {
            'parser_wild.pipelines.ParserWildPipeline': 400
        }
    }
    start_urls = [
        'https://www.wildberries.ru/catalog/obuv/zhenskaya/sabo-i-myuli/myuli'
    ]

    def parse(self, response):
        items = ParserWildUrl()
        section = ''
        sections = response.css("ul.bread-crumbs").css("span::text").getall()
        for adress in sections:
            adress += '|'
            section += adress
        print(type(section))
        urls = response.css("a.ref_goods_n_p").xpath('@href').getall()
        unique_id = response.css("div.dtList").xpath('@data-popup-nm-id').getall()
        for id, url in zip(unique_id, urls):
            items['url'] = 'https://www.wildberries.ru' + url
            items['unique_number'] = str(id)
            items['sections'] = section
            yield items

        next_page = response.css('a.pagination-next').xpath('@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

