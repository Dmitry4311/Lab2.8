#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


workers = []


def get_route():
    """
    Запросить данные о зодиаке.
    """
    surname = input("Фамилия? ")
    name = input("Имя? ")
    zodiac_sign = input("Знак зодиака ")
    date_of_birth = input("Дата рождения ")

    return {
        'surname ': surname,
        'name': name,
        'zodiac_sign': zodiac_sign,
        'date_of_birth': date_of_birth,
    }


def display_routes(wo):
    """
    Отобразить список зодиаков.
    """
    if wo:
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 30,
            '-' * 30
        )
        print(line)
        print(
                '| {:^4} | {:^30} | {:^20} | {:^30} | {:^30} |'.format(
                    "№",
                    "Имя",
                    "Фамилия",
                    "Знак зодиака",
                    "Дата рождения"
                )
        )
        print(line)

        for idx, worker in enumerate(workers, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>30} | {:>30}'.format(
                    idx,
                    worker.get('surname', ''),
                    worker.get('name', ''),
                    worker.get('zodiac_sign', ''),
                    worker.get('date_of_birth', '')
                )
            )
        print(line)

    else:
        print("зодиак не найдены")


def select_routes(wo, zo):
    """
    Выбрать зодиак после заданного времени.
    """

    for worker in wo:
        if worker.get('zodiac_sign') == zo:
            print(
                '{:>4}, {}, {}'.format(worker.get('surname', ''),
                                       worker.get('name', ''),
                                       worker.get('date_of_birth', ''))
            )


def main():
    """
    Главная функция программы.
    """

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о зодиаке.
            route = get_route()

            # Добавить словарь в список.
            workers.append(route)
            # Отсортировать список в случае необходимости.
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('destination', ''))

        elif command == 'list':
            # Отобразить все зодиаки.
            display_routes(workers)

        elif command == 'select':
            zodiac_select = input("Выберите знак зодиака: ")
            select_routes(workers, zodiac_select)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить зодиак;")
            print("list - вывести список зодиаков;")
            print("select - найти зодиак ")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
