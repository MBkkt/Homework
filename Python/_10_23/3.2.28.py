""" Элементы. Составьте тип данных Element для записей периодической
таблицы элементов. Включите в тип данных значение элемента, атомный
номер, символ и атомный вес, а также методы доступа для каждого из этих
значений. Затем составьте тип данных PeriodicTaЬle, читающий значения
из файла, создающий массив объектов Element (сам файл и описание
его формата можно найти на сайте книги) и отвечающий на запросы со
стандартного устройства ввода, чтобы пользователь мог ввести такую
молекулярную формулу, как Н20, и получить в ответ, например, молекулярную
массу. Разработайте API и реализации для каждого типа данных. """

import pandas as pd


class Element:
    def __init__(self, d):
        self.element = d['element']
        self.name = d['name']
        self.number = d['number']
        # self.symbol = d['symbol']
        self.weight = d['weight']
        # self.boil = d['boil']
        # self.melt = d['melt']
        # self.densite_vapour = d['densite_vapour']
        # self.fusion = d['fusion']


def tabler(d):
    for x in d:
        d[x] = Element(d[x])
    return d


def mass(x):
    sum_ = ''
    # sumtest = ''
    tDigit = ''
    tWord = ''
    for i in range(len(x)):
        if x[i].isdigit():
            tDigit += x[i]
        elif tDigit:
            sum_ += f'*{tDigit}'
            # sumtest += f'*{tDigit}'
            tDigit = ''
        if not x[i].isdigit():
            if i + 1 == len(x) or x[i + 1].isdigit() or x[i + 1].isupper():
                tWord += x[i]
                sum_ += f'+{table[tWord].weight}'
                # sumtest += f'+{tWord}'
                tWord = ''
            else:
                tWord += f'{x[i]}'
    # print(sumtest)
    return eval(sum_)


def answer(formula):
    yield f'{formula}'
    yield f'Weight: {mass(formula)}'


def source(file):
    df = pd.read_csv(file, delimiter=',')
    df = df.rename(columns={'Element': 'number', 'Number': 'element', 'Symbol': 'symbol', 'Weight': 'weight',
                            'Boil': 'boil', 'Melt': 'melt', 'Density Vapour': 'densite_vapour', 'Fusion': 'fusion'})
    df['name'] = df.index
    df.index = df['element']
    df.fillna(0)
    df = df.T.to_dict()
    return df


if __name__ == '__main__':
    table = source('elements.csv')
    table = tabler(table)

    formula = input()
    print(*answer(formula), sep='\n')
