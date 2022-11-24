import requests
import bs4
import optparse
import pprint

avito_url_local = "http://127.0.0.1/avito_main.html"
sneakers_url = "http://127.0.0.1/avito_second.html"
avito_url_global = "https://www.avito.ru"


class Parser:
    def __init__(self, parser: optparse.OptionParser):
        (self.options, _) = parser.parse_args()

        self.count = self.options.count
        self.debug = self.options.debug
        self.file_path = self.options.file_path
        self.fp = None
        self.url = avito_url_global if not self.debug else avito_url_local

    def extract_adv(self):
        print("Начало обработки основной страницы продукта", file=self.fp)
        html = requests.get(self.url).text
        soap = bs4.BeautifulSoup(html, "html.parser")
        if self.debug == 2:
            print(soap)
        try:
            if "<h1>Доступ ограничен: проблема с IP</h1>" == str(soap.find_all('h1')[0]):
                print("Доступ ограничен: проблема с IP")
                return
        except IndexError:
            pass

        advertisements = soap.find_all('a', attrs={"class": ["link-link-MbQDP",
                                                             "link-design-default-_nSbv",
                                                             "title-root-zZCwT",
                                                             "body-title-drnL0",
                                                             "title-root_maxHeight-X6PsH"],
                                                   "data-marker": "title"})
        for i in range(self.count):
            self.additional_adv(advertisements[i].get("href"))

    def additional_adv(self, url):

        print("\n\n\nНачало обработки дополнительной страницы продукта\n\n\n", file=self.fp)

        url = sneakers_url if self.debug else self.url + url

        html = requests.get(url).text
        soap = bs4.BeautifulSoup(html, "html.parser")
        if self.debug == 2:
            print(soap)
        advertisements = soap.find_all('a', attrs={"class": ["link-link-MbQDP",
                                                             "link-design-default-_nSbv",
                                                             "title-root-zZCwT",
                                                             "iva-item-title-py3i_",
                                                             "title-root_maxHeight-X6PsH"]})
        for i in advertisements:
            print("Ссылки на дополнительной странице продукт: ", i.get("href"), file=self.fp)

    def run(self):
        try:
            with open(self.file_path, "w+") as self.fp:
                self.extract_adv()
        except TypeError:
            self.extract_adv()


def main():
    parser = optparse.OptionParser()
    parser.add_option("-c", "--count", dest="count", help="Number of extracted advertisement.", type="int")
    parser.add_option("-f", "--file", dest="file_path", help="Write results to file (default none)", default=None)
    parser.add_option("-d", "--debug", dest="debug", help="Write out debug info", type="int")
    avito_parser = Parser(parser)
    avito_parser.run()


if __name__ == '__main__':
    main()
