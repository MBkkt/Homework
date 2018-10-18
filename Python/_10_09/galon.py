"""Напишите программу для решения следующей задачи:
у вас есть два кувшина - на четыре и три галлона. Но ни на одном из них нет маркировки.
Также имеется насос, с помощью которого можно набирать воду.
Как получить ровно два галлона в четырёхгаллоновом кувшине?
Размер каждого кувшина и итоговое количество воды, которое нужно оставить в наибольшем из них пусть
запрашиваются из консоли."""

import sys

sys.setrecursionlimit(30000)


def answ(one, two, k=0, ans=''):
    global need, depth
    # global count, lim
    # count += 1
    if one[0] == need:
        print(ans)
        # print(count, lim)
        exit(0)
    elif k == depth:
        pass
        # lim += 1
    else:
        temp = min(one[0] + two[0], one[1])
        if temp != one[0]:
            temp2 = two[0] - (temp - one[0])
            answ([temp, one[1]], [temp2, two[1]], k=k + 1, ans=ans + f'{temp} {temp2}\n')
        temp = min(one[0] + two[0], two[1])
        if temp != two[0]:
            temp2 = one[0] - (temp - two[0])
            answ([temp2, one[1]], [temp, two[1]], k=k + 1, ans=ans + f'{temp2} {temp}\n')

        if one[0] != 0:
            answ([0, one[1]], two, k=k + 1, ans=ans + f'0 {two[0]}\n')
        if two[0] != 0:
            answ(one, [0, two[1]], k=k + 1, ans=ans + f'{one[0]} 0\n')

        if one[0] != one[1]:
            answ([one[1], one[1]], two, k=k + 1, ans=ans + f'{one[1]} {two[0]}\n')
        if two[0] != two[1]:
            answ(one, [two[1], two[1]], k=k + 1, ans=ans + f'{one[0]} {two[1]}\n')


if __name__ == '__main__':
    oneT = [0, int(input())]
    twoT = [0, int(input())]
    need = int(input())
    for depth in range(1, 100):
        one = oneT
        two = twoT
        # count = lim = 0
        answ(one, two, ans=f'0 0 - start\n')
        # print(count, lim)
    print("NO")
