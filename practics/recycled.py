# -*- coding: utf-8 -*-


class Recycled(object):
    def __init__(self, size):
        self.size = size

    def change_size(self, size):
        self.size = size

    def get_size(self):
        print('This recycled size {}'.format(self.size))

    def put_v(self, v):
        if v.size <= self.size:
            print(f"{v} is in a HandBox")
        else:
            print(f'{v.size} is to big for a HandBox with size = {self.size}')


class Thing:
    def __init__(self, size):
        self.size = size


class Bag(Recycled):
    pass


b1 = Recycled(20)
b1.get_size()

b2 = Recycled(45)
b2.get_size()

int1 = Thing(21)
b1.put_v(int1)

bag1 = Bag(45)
bag1.get_size()

bag_put = Thing(50)
bag1.put_v(bag_put)
