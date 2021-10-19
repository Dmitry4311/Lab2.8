#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    a = int(input("Введите целое число: "))
    if a > 0:
        positive()
    elif a == 0:
        print("Число равно нулю")
    else:
        negative()


def negative():
    print("Отрицательное")


def positive():
    print("Положительное")


if __name__ == '__main__':
    test()
