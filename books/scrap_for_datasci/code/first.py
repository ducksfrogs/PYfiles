import requests

url = 'http://www.webscrapingfordatascience.com/basichttp/'

url = 'http://www.webscrapingfordatascience.com/paramhttp/?query=test'

url = 'http://www.webscrapingfordatascience.com/paramhttp/?query=a query with spaces'


url = 'http://www.webscrapingfordatascience.com/paramhttp/?query=complex?&'

import requests

from urllib.parse import quote, quote_plus

raw_string = 'a query with /, spaces and?&'

params = {
    'query': 'a query with /, spaces and?&'
}

r = requests.get(url, params=params)


def calc(a, b, op):
    url = 'http://www.webscrapingfordatascience.com/calchttp/'
    params = {'a': a, 'b':b, 'op': op}
    r = requests.get(url, params=params)
    return r.text

url = 'https://en.wikipedia.org/w/index.php' + \
    '?title= List_of_Game_of_Thrones_episodes&oldid=802553687'
