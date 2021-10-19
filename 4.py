#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    return input("Ведите строку: ")


def test_input(string):
    if string.isdigit():
        return True
    else:
        return False


def str_to_int(number):
    return int(number)


def print_int(str_s):
    print(str_s)


if __name__ == '__main__':
    value = get_input()
    if test_input(value):
        print_int(str_to_int(value))
