"""Напишите программу для решения следующей задачи.
Три миссионера и три каннибала подошли к берегу реки, возле которого привязана лодка,
вмещающая только двух человек. Каждому нужно перебраться на другой берег,
чтобы продолжить путешествие. Однако,
если на каком-нибудь из берегов каннибалов окажется больше, чем миссионеров,
то миссионеры будут съедены. Найдите такую последовательность перевозок,
чтобы все безопасно оказались на другом берегу реки."""


def solve(m_count=3, c_count=3, boat=1, seats=4):
    if m_count == c_count == boat == 0:
        print('Win')
    elif boat > 0:
        if m_count < c_count:
            print(f'2 cannibals go                    '
                  f'{m_count} missionars and {c_count-seats} cannibals left')
            solve(m_count, c_count - seats, boat - 1)
        else:
            print(f'1 missionar and 1 cannibal go    '
                  f'{m_count-seats//2} missionars and {c_count-seats//2} cannibals left')
            solve(m_count - seats//2, c_count - seats//2, boat - 1)
    else:
        global c, n
        print(f'One cannibal back                '
              f'{c - m_count} misssioners and {n - c_count-seats//2} cannibal right')
        solve(m_count, c_count + seats//2, 1)


if __name__ == '__main__':
    # missionar = int(input())
    # cannibal = int(input())
    # boats = int(input())
    c, n = 12, 10
    solve(c, n)
