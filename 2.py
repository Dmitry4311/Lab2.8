#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():
    def circle():
        return math.pi * r ** 2

    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))
    answer = input("Хотите  получить площадь боковой поверхности цилиндра"
                   "(напишите - 1), или полную площадь цилиндра"
                   "( напишите - 2)?: ")
    side = 2 * math.pi * r * h

    if answer == "1":
        print(f"Площадь боковой поверхности: {side}")
    else:
        s_circle = circle()
        full = side + 2 * s_circle
        print(f"Полная площадь: {full}")


if __name__ == '__main__':
    cylinder()
