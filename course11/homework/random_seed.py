#!/usr/bin/env/python3

import random, sys, os, time
from flask import Flask

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    #SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)

z = []
x = random.randint(1, 10)
print(x)


def init_seed():
    if len(sys.argv) < 2:
        print('python random_seed.py [seed] [1 or more]', sys.argv)
        sys.exit()
    else:
        FLASK_RANDOM_SEED = int(sys.argv[2])
        start_flask(FLASK_RANDOM_SEED)
        print('Flask Random Seed = {}'.format(FLASK_RANDOM_SEED))


def start_flask(seed):
    seed_random = random.randint(int(seed), 10)
    print('Flask Random = {}'.format(seed_random))
    z.append(seed_random)
    app.run()


@app.route('/', methods=['GET'])
def number_is():
    return 'Число {} загадано'.format(z[0])


@app.route('/guess/<int:num1>', methods=['POST'])
def number_guess(num1):
    if z[0] > num1:
        return 'Загаданное  число {} > числа {}'.format(z[0], num1)
    if z[0] < num1:
        return 'Загаданное  число {} < числа {}'.format(z[0], num1)
    else:
        return 'Вы угадали число {} == {}'.format(num1, z[0])


if __name__ == '__main__':
    init_seed()
    #start_flask(x)
