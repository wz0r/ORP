# class Car:
#    pass


# c=Car()

# print(c, type(c))

class Room:
    number = 'Room 43'
    floor = 4


r = Room()
r1 = Room()

print(r.number, r1.number)
print(r.floor, r1.floor)

r.number = 12
r.floor = '5 floor'
print(r.number, r.floor)
print(r1.number, r1.floor)


class Door:
    def __init__(self):
        self.opened = True

    def open(self):
        print(self)
        print('Дверь открыта')


d = Door()
d2 = Door()
d.open()
d2.open()


class Car:
    def __init__(self):
        self.seat = 'sport seat'

    def sit(self):
        print(f'Сиденья {self.seat}')


c1 = Car()
c1.sit()

class Terminal():
    def hello(self, user_name):
        print(f"Self{self}")
        print('Hello', user_name)


t = Terminal()
t.hello('Dima')
t.hello('katya')