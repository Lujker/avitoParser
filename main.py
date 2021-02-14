# This is a sample Python script.
import AvitoParser
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    url = 'https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg'
    AvitoParser.AvitoObj.set_log_path('logfile.txt')
    AvitoParser.AvitoObj.set_exel_path('exelout.xlsx')

    AvitoParser.get_info(AvitoParser.get_html(url))
    AvitoParser.AvitoObj.write_exel_data()

    # получения количества страниц и парсинг их в цикле
    # total_pages = (
    #     AvitoParser.get_total_pages(
    #         AvitoParser.get_html(url)))
    # for i in range(2, total_pages):
    #     url_gen = url + "?p="+str(i)
    #     AvitoParser.get_info(AvitoParser.get_html(url_gen))
    # AvitoParser.AvitoObj.write_exel_data()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
