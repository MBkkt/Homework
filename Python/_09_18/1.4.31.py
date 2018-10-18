""" Сапер. Составьте программу, которая получает три аргумента командной
строки, т, п и р, а затем создает массив логических элементов размером
т х п, каждый элемент которой занят с вероятностью р. В этой игре занятые
ячейки соответствуют минам, а пустые безопасны. Выведите массив,
используя звездочку для мин и точку для безопасных мест. Затем замените
каждый безопасный квадрат количеством соседних мин (выше, ниже,
слева, справа и по диагонали) и выведите результат, как в этом примере: """

import random


def draw(arr, kl=''):
    for r in range(1, len(arr) - 1):
        for c in range(1, len(arr[0]) - 1):
            x = '*' if bombs[r][c] else kl or arr[r][c]
            print(x, end=' ')
        print()
    print()


def solve(arr):
    for r in range(1, len(arr) - 1):
        for c in range(1, len(arr[0]) - 1):
            for n1 in range(r - 1, r + 2):
                for n2 in range(c - 1, c + 2):
                    if bombs[n1][n2]:
                        arr[r][c] += 1
    return arr


if __name__ == '__main__':
    s = input().split()  # столбцы, строки, вероятность мины
    m = int(s[0])
    n = int(s[1])
    p = float(s[2])
    bombs = [[1 if (random.random() < p and 0 < j <= m and 0 < i <= n) else 0
              for j in range(m + 2)]
             for i in range(n + 2)]
    draw(bombs, kl='.')
    saper = [[0 for j in range(m + 2)]
             for i in range(n + 2)]
    saper = solve(saper)
    draw(saper)
