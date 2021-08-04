import urllib.request
from xml.dom.minidom import parseString


def get_data(url):  # getting data from url (XML file in that case)
    web_file = urllib.request.urlopen(url)  # send result of request
    return web_file.read()  # read web_file content


def get_currencies_dictionary(xml_content):

    dom = parseString(xml_content)
    dom.normalize()

    elements = dom.getElementsByTagName("Valute")
    currency_dict = {}

    for node in elements:  # that code 
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Value':
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))
                if child.tagName == 'CharCode':
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data
        currency_dict[char_code] = value
    return currency_dict


def print_dict(dict):
    needed_currency = 'JPY'  # change 
    needed_currency_value = dict[needed_currency]
    if needed_currency in dict:
        print(f'Курс {needed_currency} к рублю - {needed_currency_value}')


if __name__ == '__main__':
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    currency_dict = get_currencies_dictionary(get_data(url))
    print_dict(currency_dict)
