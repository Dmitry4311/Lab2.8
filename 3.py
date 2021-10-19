#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def multiplication():
    summa = 1
    while True:
        num = int(input("Ведите число: "))
        if num != 0:
            summa *= num
            print(summa)
        else:
            return False


if __name__ == '__main__':
    multiplication()
