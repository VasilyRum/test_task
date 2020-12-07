import random
import json
from datetime import datetime

test = {
 "timestamp": datetime.now().timestamp(),  # Текущее время в формате timestamp
 "RPC": "123",  # {str} Уникальный код товара
 "url": "http",  # {str} Ссылка на страницу товара
 "title": "Лапти",  # {str} Заголовок/название товара
 "marketing_tags": [1, 2, 3],  # {list of str}
 "brand": "Dolce and Gabbana",  # {str} Брэнд товара
 "section": [],  # {list of str} Иерархия разделов
 "price_data": {
                "current": 1.2,  # {float} Цена со скидкой
                "original": 1.3,  # {float} Оригинальная цена
                "sale_tag": "Скидка 10%"  # {str}  Скидка на товар
              },
 "stock": {
                "in_stock": True,  # {bool} Отражает наличие товара в магазине
                "count": 3  # {int} Количество оставшегося товара в наличии, иначе 0
          },
 "assets": {
                "main_image": "http",  # {str} Ссылка на основное 	изображение товара
                "set_images": ["http", "http2"],  # {list of str} Список больших 	изображений товара
                "view360": ["http", "http2"],  # {list of str}
                "video": ["http", "http2"]  # {list of str}
           },
 "metadata": {
                "__description": "",  # {str} Описание товар
                "АРТИКУЛ": "A88834",
                "СТРАНА ПРОИЗВОДИТЕЛЬ": "Китай"
            },
 "variants": 1  # {int} Кол-во вариантов у товара в карточке
}
test2 = {
 "timestamp": "123",  # Текущее время в формате timestamp
 "RPC": "123",  # {str} Уникальный код товара
 "url": "http",  # {str} Ссылка на страницу товара
 "title": "Лапти",  # {str} Заголовок/название товара
 "marketing_tags": [1, 2, 3],  # {list of str}
 "brand": "Dolce and Gabbana",  # {str} Брэнд товара
 "section": [],  # {list of str} Иерархия разделов
 "price_data": {
                "current": 1.2,  # {float} Цена со скидкой
                "original": 1.3,  # {float} Оригинальная цена
                "sale_tag": "Скидка 10%"  # {str}  Скидка на товар
              },
 "stock": {
                "in_stock": True,  # {bool} Отражает наличие товара в магазине
                "count": 3  # {int} Количество оставшегося товара в наличии, иначе 0
          },
 "assets": {
                "main_image": "http",  # {str} Ссылка на основное 	изображение товара
                "set_images": ["http", "http2"],  # {list of str} Список больших 	изображений товара
                "view360": ["http", "http2"],  # {list of str}
                "video": ["http", "http2"]  # {list of str}
           },
 "metadata": {
                "__description": "",  # {str} Описание товар
                "АРТИКУЛ": "A88834",
                "СТРАНА ПРОИЗВОДИТЕЛЬ": "Китай"
            },
 "variants": 11111  # {int} Кол-во вариантов у товара в карточке
}
A = [test, test2]


def make_json(python_list_of_dict):
    """Function that make JSON from list of dictionaries
    """
    out_json = json.dumps(python_list_of_dict, indent=2)
    return out_json


# new_json = make_json(A)
# print(type(new_json))
# print(new_json)

a = '4 150 ₽'
a = a.replace(' ', '')
print(a)