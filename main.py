import requests
import bs4
import optparse
import pprint

url = "http://127.0.0.1/avito_main.html"


def additional_adv(url):
    html = requests.get(url).text
    soap = bs4.BeautifulSoup(html, "html.parser")
    advertisements = soap.find_all('a', attrs={"class": ["link-link-MbQDP",
                                                        "link-design-default-_nSbv",
                                                        "title-root-zZCwT",
                                                        "iva-item-title-py3i_",
                                                        "title-root_maxHeight-X6PsH"])



def main_parser(parser):
    (options, _) = parser.parse_args()
    extract_adv(int(options.count))


def extract_adv(count):
    html = requests.get(url).text
    soap = bs4.BeautifulSoup(html, "html.parser")
    advertisements = soap.find_all('a', attrs={"class": ["link-link-MbQDP",
                                                         "link-design-default-_nSbv",
                                                         "title-root-zZCwT",
                                                         "body-title-drnL0",
                                                         "title-root_maxHeight-X6PsH"],
                                               "data-marker": "title"})
    for i in range(count):
        print(advertisements[i].get("href"))


def main():
    parser = optparse.OptionParser()
    parser.add_option("-c", "--count", dest="count", help="Number of extracted advertisement.")
    parser.add_option("-f", "--file", dest="file_path", help="Write results to file (default none)", default=None)
    main_parser(parser)


if __name__ == '__main__':
    main()
