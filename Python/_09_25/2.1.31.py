''' Биномиальное распределение. Составьте функцию binomial( ) , получающую
целые числа n и k, а также вещественное число р и вычисляющую
вероятность получения точно k орлов при n бросках монеты (с вероятностью
р орлов), используя формулу
f(k, п, р) = pk
(l-p)'•-
k п!!(k!(п- k)!)
Подсказка. Во избежание вычислений с огромными целыми числами вычислите
х = ln fik, п, р ), а затем возвратите ех. В глобальном коде получите
из командной строки числа n и р и удостоверьтесь, что сумма всех
значений k от О до n составляет приблизительно 1.'''
from math import factorial, log, exp


def comb(n, k):
    k = max(k, n - k)
    fac = 1
    for i in range(k + 1, n + 1):
        fac *= i
    return fac / factorial(n - k)


def binomial(n, k, p=0.5):
    s = k * log(p) + (n - k) * log(1 - p)
    return exp(s) * comb(n, k)


if __name__ == '__main__':
    n = int(input())
    s = 0
    for k in range(n + 1):
        x = binomial(n, k)
        print(f'{x:.3f}')
        s += x
    print(f'{s:.3f}')
