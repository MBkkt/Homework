"""Задача дня рождения. Предположим, в пустую комнату входят люди, пока
у двух из них не совпадут дни рождения. Сколько в среднем людей должно
войти в комнату до совпадения? Проведите эксперименты для оценки
значения этого количества. Подразумевается, что дни рождения - равномерно
распределенные случайные целые числа от О до 364."""
import random


def train():
    last = set()  # вошедшие
    x = random.randrange(365)  # входящий
    k = 1  # людей зашло до совпадения
    while x not in last:
        last.add(x)
        x = random.randrange(365)
        k += 1
    return k


if __name__ == '__main__':
    n = int(input())  # количество эксперементов
    p = 0  # среднее
    for i in range(n):
        p += train()
    print(f'В среднем в комнату должно зайти {p/n:.0f} человека')