"""Напишите программу для решения следующей задачи.
Три миссионера и три каннибала подошли к берегу реки, возле которого привязана лодка,
вмещающая только двух человек. Каждому нужно перебраться на другой берег,
чтобы продолжить путешествие. Однако,
если на каком-нибудь из берегов каннибалов окажется больше, чем миссионеров,
то миссионеры будут съедены. Найдите такую последовательность перевозок,
чтобы все безопасно оказались на другом берегу реки."""
from itertools import product


def solve(m_count, c_count, boat=1):
    if m_count == c_count == boat == 0:
        print('Win')
    elif boat > 0:
        if m_count < c_count:
            print(f'2 cannibals go                    '
                  f'{m_count} missionaries and {c_count-2} cannibals left')
            solve(m_count, c_count - 2, boat - 1)
        else:
            print(f'1 missionary and 1 cannibal go    '
                  f'{m_count-1} missionaries and {c_count-1} cannibals left')
            solve(m_count - 1, c_count - 1, boat - 1)
    else:
        print('One cannibal back')
        solve(m_count, c_count + 1, 1)


if __name__ == '__main__':
    # missionar = int(input())
    # cannibal = int(input())
    # boats = int(input())
    solve(3, 3, 1)
