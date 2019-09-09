#!/usr/bin/env/python3

from bs4 import BeautifulSoup
import urllib
import urllib3
import urllib.parse


def get_habrahabr():
    http = urllib3.PoolManager()
    url = 'https://habr.com'
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, features='html.parser')
    print(soup)


def find_pet_by_tag(tag):
    http = urllib3.PoolManager()
    url = 'http://petstore.swagger.io/v2/pet/findByTags'
    query_args = {'tags': tag}
    data = urllib.parse.urlencode(query_args)
    full_url = '{}?{}'.format(url, data)
    print(full_url)
    response = http.request('GET', full_url, headers={'Accept': 'application/json'})
    soup = BeautifulSoup(response.data, features='html.parser')
    print('{}\n'.format(soup))


if __name__ == '__main__':
    find_pet_by_tag('string')

