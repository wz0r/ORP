#!/usr/bin/env/python3

#  + Написать декоратор, который отменяет выполнение любой
# декорированной функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!

from functools import wraps, reduce
from time import time
# @wraps(f) используется для сохранения контекста декорируемой функции в декораторе
# например для вывода имени декорируемой функции


def logger(func):
    """
    Декоратор логирующий выполнение любой декорированной функции
    """
    print('Decorator created\n')

    @wraps(func)
    def logger_wrap(*args, **kwargs):
        print('\n1.\'{}\' started\n'.format(func.__name__))
        func_return = func(*args, **kwargs)
        print('2.\'{}\' stopped\n'.format(func.__name__))

        return func_return

    return logger_wrap


@logger
def short(string_param):
    print('Speed!', string_param)
    return 'short'


def main():
    print(short('Hi'))
    print(short('Bye'))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bye!')

