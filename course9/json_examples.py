#!/usr/bin/env/python3

import json

from files import way_better


if __name__ == '__main__':
    data = way_better('data.json')
    print('raw data is', data, type(data))
    print()

# Из строки в обьект
    obj = json.loads(data)
    print(obj, type(obj))

    print(obj['object'], obj['boolean'])
    print()

# Из обьекта в строку

    print('dumping object to text:')
    obj['new-value'] = 'secret'
    print(json.dumps(obj))
