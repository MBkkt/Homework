"""Напишите программу для решения следующей задачи.
Три миссионера и три каннибала подошли к берегу реки, возле которого привязана лодка,
вмещающая только двух человек. Каждому нужно перебраться на другой берег,
чтобы продолжить путешествие. Однако,
если на каком-нибудь из берегов каннибалов окажется больше, чем миссионеров,
то миссионеры будут съедены. Найдите такую последовательность перевозок,
чтобы все безопасно оказались на другом берегу реки."""
from itertools import product


def path(count=3):
    # boat: missioner canibal
    boats = [(1, 1), (0, 2), (2, 0)]
    for variant in product(boats, boats, boats):
        if sum(i[0] for i in variant) != sum(i[1] for i in variant) != count:
            continue
        old = [count, count]  # out
        new = [0, 0]  # in
        for boat in variant:
            old[0] -= boat[0]
            old[1] -= boat[1]
            new[0] += boat[0]
            new[1] += boat[1]
            if 0 < new[0] < new[1] or 0 < old[0] < old[1]:
                break
        else:
            yield variant


if __name__ == '__main__':
    print(*path(), sep='\n')
