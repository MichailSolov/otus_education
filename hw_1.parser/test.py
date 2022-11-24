# Задача спарсить с сайта https://spimex.com/markets/oil_products/trades/results/  таблицы
# найти цену товара с артикулом A592UFM060F и поместить их в новую таблицу

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tqdm import tqdm


def read_table(href_list):
    price_list = []

    for el in tqdm(href_list):
        df = pd.read_excel(el, skiprows=6)  # Считываем таблицу по адрессу ссылки
        d1 = df[df['Код\nИнструмента'] == 'A592UFM060F']['Unnamed: 11']  # Находим нужный элемент в этой таблице
        price_list.append(int(d1.iloc[0])) # записываем в список

    # Создаем новый DataFrame с новыми данными
    data = {'price': price_list}
    df_filled = pd.DataFrame(data)
    print(df_filled)

    # Сохраняем наш DataFrame в NewTable.xls
    writer = pd.ExcelWriter('NewTable.xls')
    df_filled.to_excel(writer)
    writer.save()
    print(f'Данные cохранили в Excel файл NewTable.xls')

def main():
    url = 'https://spimex.com/markets/oil_products/trades/results/'
    base_url = 'https://spimex.com'
    html = requests.get(url).text   # Получаем HTML код
    print(html)
    soup = bs(html, 'html.parser') # Исользуя библиотеку bs4 получаем объект "суп", подготовленный для дальнейшей работы

    # Применяем метод find_all , чтобы найти все тэги <a> с классом 'accordeon-inner__item-title', 'link', 'xls'
    table_href = soup.find_all('a', attrs={'class': ['accordeon-inner__item-title', 'link', 'xls']})
    print('Парсим данные')
    list_href = []

    # Пробегаемся по table_href и с помощью .get() вытаскиваем значение href и записываем в список все ссылки.
    for tbl in tqdm(table_href[1: 5]):
        href = tbl.get('href')
        file_url = base_url + href
        print(f' Ссылка на таблицу {file_url}')
        list_href.append(file_url)
    read_table(list_href)

# A592UFM060F


if __name__ == '__main__':
    main()