#!/usr/bin/env/python3

from bs4 import BeautifulSoup
import urllib
import urllib3


def get_habrahabr():
    http = urllib3.PoolManager()
    url = 'https://habr.com'
    response = http.request('GET', url)
    code = BeautifulSoup(response.code)
    #info = BeautifulSoup(response.info)
    #html = BeautifulSoup(response.read)
    #BeautifulSoup(response.close)
    print(code)


if __name__ == '__main__':
    get_habrahabr()

