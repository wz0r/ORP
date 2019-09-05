#!/usr/bin/env/python3

z_list = []


def open_files(filename):
    file = open(filename, 'r')
    for line in file:
        z = line.split()
        z_list.append(z)
        wr_file('ip_ch.txt')


def wr_file(filename):
    file = open(filename, 'w')
    for x in z_list:
        file.write('{} {}\n'.format(x[1], x[0]))


if __name__ == '__main__':
    open_files('ip.txt')
