#!/usr/bin/env/python3

import json

from files import way_better


if __name__ == '__main__':
    data = way_better('data.json')  # текст который лежит в data.json
    print('raw data is', data, type(data))
    print()

# Из строки в обьект (словарь)
    obj = json.loads(data)
    print(obj, type(obj))

    print(obj['object'], obj['boolean'])
    print()

# Из обьекта (словаря) в строку (тип json)

    print('dumping object to text:')
    obj['new-value'] = 'secret'  # новый ключ со значением
    print(json.dumps(obj, sort_keys=True, indent=4))  # из словаря в json, с форматированием
