from contextlib import contextmanager


@contextmanager
def do_work(value, mode='r'):
    print('some work before, __enter__')
    try:
        open_file = open(value, mode)
    except Exception as e:
        print('Exception was here!')
        #yield None
    else:
        #yield open_file
        open_file.close()
    print('some work after, __exit__')


with do_work('to_open.txt'):
    print('Some work here!')
    # if w is not None:
    #     print(w.read())


def foo():
    # SOME WORK // OPEN FILE
    return open_file
    # SOME WORK AFTER

def gen():
    print('before')
    yield 1
    print('after')
    # yield 2

g = gen()
next(g)
next(g)