import requests
import pandas as pd
from bs4 import BeautifulSoup


class AvitoObj:
    """
    Объект который описывает сущность одного объявления на странице Avito
    """
    __log_file: str = ''
    __exel_file: str = ''
    url_list: list = list()
    title_list: list = list()
    price_list: list = list()
    address_list: list = list()

    def __init__(self):
        self.url = str()
        self.title = str()
        self.price = str()
        self.address = str()

    @classmethod
    def set_log_path(cls, log_file=''):
        cls.__log_file = log_file

    @classmethod
    def set_exel_path(cls, exel_file=''):
        cls.__exel_file = exel_file

    def make_str(self) -> str:
        return self.url + " ; " + self.title + " ; " + self.price + " ; " + self.address + '\n'

    def input_to_log(self):
        with open(self.__class__.__log_file, 'a+', encoding='utf16') as f:
            f.write(self.make_str())

    @classmethod
    def write_exel_data(cls):
        if True:
            writer = pd.ExcelWriter(cls.__exel_file, engine='openpyxl')
            data_frame = pd.DataFrame({'URL': cls.url_list,
                                       'Title': cls.title_list,
                                       'Price': cls.price_list,
                                       'Address': cls.address_list})
            data_frame.to_excel(writer)
            writer.save()
            writer.close()


# получения текста запросы по url
def get_html(url) -> str:
    r = requests.get(url)
    return r.text


# Получение количества страниц в запросе
def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-root-2oCjZ').find_all(
        'span', class_="pagination-item-1WyVp")[-2].get('data-marker')
    result = int(pages.split('(')[1].split(')')[0])
    return result


# Перебор объявлений на странице
def get_info(html) -> None:
    """
    Парсинг переданного html текста страницы Авито и запись в списки
    """
    soup = BeautifulSoup(html, 'lxml')
    obj_ls = list()
    for item in soup.find_all('div', class_='iva-item-body-NPl6W'):  # имена объявлений со страницы и ссылка на нее
        new_obj = AvitoObj()
        try:
            new_obj.url = 'https://www.avito.ru/' + item.find_all(
                'div', class_='iva-item-titleStep-2bjuh')[0].find_all('a')[0].get('href')  # ссылка на объект
            new_obj.title = item.find_all(
                'div', class_='iva-item-titleStep-2bjuh')[0].find_all('a')[0].get('title')  # титул объявления
            new_obj.price = (item.find_all(
                'div', class_='iva-item-priceStep-2qRpg')[0].text.split('\\')[0])  # цена за месяц
            new_obj.address = item.find_all('div', class_='iva-item-developmentNameStep-1hr7p')[0].text
            obj_ls.append(new_obj)
        except Exception:
            obj_ls.append(new_obj)  # если нет одного из элементов информации все равно записываем объект

    # Запись информации в общие списки
    try:
        for obj in obj_ls:
            if AvitoObj.url_list is not None:
                AvitoObj.url_list.append(obj.url)
            if AvitoObj.title_list is not None:
                AvitoObj.title_list.append(obj.title)
            if AvitoObj.price_list is not None:
                AvitoObj.price_list.append(obj.price)
            if AvitoObj.address_list is not None:
                AvitoObj.address_list.append(obj.address)
            obj.input_to_log()
    except Exception:
        print("list is None")
