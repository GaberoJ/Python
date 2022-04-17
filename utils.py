import requests
import datetime

def currency_rates(user_value, date = False):
    """Returns the value of the currency."""

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    start_string = response.text
    help_list = start_string.replace(",", ".").split('<')
    result = []

    for element in help_list:
        if '>' in element:
            help_list[help_list.index(element)] = element.split('>')

    for element in help_list:
        if type(element) == list:
            if element[0] == 'CharCode':
                result.append(element[-1])
            elif element[0] == 'Value':
                result.append(element[-1])

    result_dict = {}
    for i in range(0, len(result), 2):
        result_dict.setdefault(result[i], float(result[i+1]))

    user_value = user_value.upper()

    if date:
        return f'{result_dict.get(user_value)} {datetime.date.today()}'

    return result_dict.get(user_value)





response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

if __name__ == '__main__':
    print(currency_rates('usd', True))
    print(currency_rates('EUR'))
