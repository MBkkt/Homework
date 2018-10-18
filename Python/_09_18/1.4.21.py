""" Самое длинное плато. Дан массив целых чисел. Составьте программу,
находящую длину и положение самой длинной непрерывной последовательности
равных значений, где значения элементов непосредственно
перед и сразу после этой последовательности меньше."""

import random


def longest_plato(a):
    mx = [0, -1, -1]  # длина, начало и конец плато
    N = len(a)
    for i in range(1, N - 1):
        if a[i - 1] < a[i]:
            for j in range(i + 1, N):  # лучше while
                if a[i] < a[j]:
                    break
                if a[i] > a[j]:
                    mx = [j - i, i, j]
                    break
    return mx


if __name__ == '__main__':
    arr = [random.randrange(3) for _ in range(20)]  # массив
    ans = longest_plato(arr)
    print(f'Длина = {ans[0]}',
          f'Начало = {ans[1]}',
          f'Конец = {ans[2]}',
          sep='\n', )
    print(arr)
