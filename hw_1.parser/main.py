import requests
import bs4
import optparse
import pprint

avito_url = "http://127.0.0.1/avito_main.html"
sneakers_url = "http://127.0.0.1/avito_second.html"


# url = "https://www.avito.ru"


class Parser:
    def __init__(self, parser: optparse.OptionParser, url):
        (self.options, _) = parser.parse_args()

        self.url = url
        self.count = self.options.count
        self.debug = self.options.debug
        self.file_path = self.options.file_path

    def extract_adv(self):
        html = requests.get(self.url).text
        soap = bs4.BeautifulSoup(html, "html.parser")
        if self.debug:
            print(soap)
        advertisements = soap.find_all('a', attrs={"class": ["link-link-MbQDP",
                                                             "link-design-default-_nSbv",
                                                             "title-root-zZCwT",
                                                             "body-title-drnL0",
                                                             "title-root_maxHeight-X6PsH"],
                                                   "data-marker": "title"})
        for i in range(self.count):
            self.additional_adv(advertisements[i].get("href"))

    def additional_adv(self, url):
        url = sneakers_url
        html = requests.get(url).text
        soap = bs4.BeautifulSoup(html, "html.parser")
        if self.debug:
            print(soap)
        advertisements = soap.find_all('a', attrs={"class": ["link-link-MbQDP",
                                                             "link-design-default-_nSbv",
                                                             "title-root-zZCwT",
                                                             "iva-item-title-py3i_",
                                                             "title-root_maxHeight-X6PsH"]})
        for i in advertisements:
            print(i.get("href"))

    def run(self):
        self.extract_adv()


def main():
    parser = optparse.OptionParser()
    parser.add_option("-c", "--count", dest="count", help="Number of extracted advertisement.", type="int")
    parser.add_option("-f", "--file", dest="file_path", help="Write results to file (default none)", default=None)
    parser.add_option("-d", "--debug", dest="debug", action="store_true", help="Write out debug info")
    avito_parser = Parser(parser, avito_url)
    avito_parser.run()


if __name__ == '__main__':
    main()
