# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ParserWildPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
        pass

    def create_connection(self):
        self.conn = sqlite3.connect('myurls_db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS myurls_db""")
        self.curr.execute("""CREATE TABLE myurls_db(
                        url text,
                        sections text
                        )""")

    def store_db(self, item):
        self.curr.execute("""INSERT INTO myurls_db VALUES (?,?)""", (
            str(item['url']),
            str(item['sections'])
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
