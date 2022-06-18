import csv
from datetime import datetime

import requests


def collect_data():
    t_date = datetime.now().strftime("%d_%m_%Y")
    response = requests.get('https://www.lifetime.plus/api/analysis2')

    categories = response.json()['categories']

    result = []

    for c in categories:
        c_name = c.get('name').strip()
        c_items = c.get('items')

        for item in c_items:
            item_name = item.get('name').strip()
            item_price = item.get('price')
            item_description = item.get('description').strip()
            item_wait_time = item.get('days')
            item_biomaterials = item.get('biomaterial').strip()
            result.append(
                [c_name, item_name, item_price, item_description, item_wait_time, item_biomaterials])

    with open(f'{t_date}.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                'Категория',
                'Название',
                'Цена',
                'Описание',
                'Готовность в днях',
                'Биоматериалы',
            )
        )

        writer.writerows(result)


def main():
    collect_data()


if __name__ == '__main__':
    main()
