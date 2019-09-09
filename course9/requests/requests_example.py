#!/usr/bin/env/python3

import requests


def get_habr():
    r = requests.get('https://habr.com')
    print(r.status_code)
    print(r.headers)
    print(r.content)


def find_pet_by_tag(tag):
    params = {'tags': tag}
    headers = {
        #'Accept': 'application/xml'
        'Accept': 'application/json'
    }
    url = 'http://petstore.swagger.io/v2/pet/findByTags'
    r = requests.get(url, params=params, headers=headers)
    print(r.status_code, r.headers)
    print(r.content)


if __name__ == '__main__':
    #get_habr()
    find_pet_by_tag('string')
