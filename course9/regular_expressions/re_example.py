#!/usr/bin/env/python3

import re

if __name__ == '__main__':
    name_pattern = r'My name is .*\.'
    is_name = re.match(name_pattern, 'My name is Dmitry.')
    print('is name:', bool(is_name))

    is_name = re.match(name_pattern, 'I am just a string.')
    print('is name:', bool(is_name))

    name_pattern_group = r'My name is (.*)\.'
    name = re.findall(name_pattern_group, 'My name is Dmitry.')
    print(name)

