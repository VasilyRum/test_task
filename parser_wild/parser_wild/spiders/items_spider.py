import scrapy
import sqlite3
from datetime import datetime
from ..items import ParserWildItem
import unicodedata


class Items(scrapy.Spider):
    name = 'Items'

    def __init__(self):
        self.start_urls = self.create_urls_list()
        self.section = self.crete_section()

    @staticmethod
    def change_price_to_float(data_from_parse):
        data_from_parse = unicodedata.normalize("NFKD", data_from_parse)
        data_from_parse = data_from_parse.replace(' ', '')
        data_from_parse = data_from_parse[:-1]
        return float(data_from_parse)

    def create_urls_list(self):
        urls_list = []
        connect = sqlite3.connect('myurls_db')
        currs = connect.cursor()
        currs.execute("""SELECT url FROM myurls_db""")
        urls_tuple = list(currs.fetchall())
        for url in urls_tuple:
            urls_list.append(url[0])
        currs.close()
        return urls_list

    def crete_section(self):
        connect = sqlite3.connect('myurls_db')
        currs = connect.cursor()
        currs.execute("""SELECT sections FROM myurls_db""")
        section = list(currs.fetchall())[0][0]
        section = section.split('|')[:-1]
        currs.close()
        return section

    def parse(self, response):
        timestamp = datetime.now().timestamp()
        unique_id = response.css("span.j-article::text").get().strip()
        title = response.css("title::text").get().strip()
        brand = response.xpath('//*[@id="container"]/div[1]/div[2]/div[1]/div[1]/span[1]').css("::text").get()
        main_url = response.xpath('/html/head/link[5]').xpath('@href').get()
        price_current = response.css("span.final-cost::text").get().strip()
        price_current = self.change_price_to_float(price_current)
        price_original = response.css("del.c-text-base::text").get().strip()
        price_original = self.change_price_to_float(price_original)
        sale_tag = response.css("div.discount-tooltipster-content").css("span::text")[2].get()
        if not sale_tag:
            sale_tag = "Ваша скидка " + str(100 - price_current/price_original*100) + "%"
        main_image_link = response.css("a.j-photo-link")[0].xpath('@href').get()
        main_image_link = main_image_link[2:]
        set_image_link = response.css("a.j-photo-link")[1:].xpath('@href').getall()
        for id, url in enumerate(set_image_link):
            url = url[2:]
            set_image_link[id] = url
        """Block for parse is item have two or more variants"""
        variants = len(response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[3]/div[2]/div[5]/div/div/ul/li'))
        if variants == 0:
            variants = 1
        """Проверка, есть ли стиль у кнопки в корзину, если есть, значит товара нет в налиии
        Количество товаров на странице не нашел"""
        buy_button = response.xpath('//*[@id="container"]/div[1]/div[3]/div[2]/div[7]/div/button[1]')
        buy_button = buy_button.xpath('@style').get()
        if buy_button:
            in_stock = False
        else:
            in_stock = True
        """Block for parse Metadata"""
        metadata_all = {}
        for metadata in response.css('.params .pp'):
            metadata_all[metadata.css('span:nth-of-type(1) b::text').get().strip()] \
                = metadata.css('span:nth-of-type(2)::text').get().strip()

        """"Make items"""
        items = ParserWildItem()
        items['timestamp'] = timestamp
        items['RPC'] = unique_id
        items['URL'] = main_url
        items['title'] = title
        items['marketing_tags'] = 'not found '
        items['brand'] = brand
        items['section'] = self.section
        items['price_data'] = {'current': price_current,
                               'original': price_original,
                               'sale_tag': sale_tag}
        items['stock'] = {'in stock': in_stock,
                          'count': 'not found '}
        items['assets'] = {'main_image': main_image_link,
                           'set_images': set_image_link,
                           'view 360': 'not found ',
                           'video': 'not found '}
        items['metadata'] = {'description': metadata_all}
        items['variants'] = variants
        yield items
