''' Гармонические числа. Создайте программу harmonic . ру, определяющую
для вычисления гармонических чисел три функции: harmonic( ),
h armonicSmall ( ) и harmoniclarge ( ). Функция h armonicSma ll ( ) должна
вычислить лишь сумму (как в программе 2.1.1), функция ha rmonicla rge()
должна использовать аппроксимацию Нп = lo&(n) +у+ 1/(2п) - 1/(12п2) ­
- 1!(120п4) (число у= 0.5772 1 5664901 532 ... - это константа Эйлера),
а функция ha rmonic () должна вызвать функцию ha rmonicSmall ()
для n< 100 и функцию harmoniclarge () в противном случае. '''

from math import log


def harmonicSmall(x):
    return sum((1 / i for i in range(1, x + 1)))


def harmonicLarge(x):
    y = 0.577215664901532
    return log(x) + y + (1 / (2 * n)) - (1 / (12 * (n ** 2))) + (1 / (120 * (n ** 4)))


def harmonic(n):
    if n < 100:
        return harmonicSmall(n)
    return harmonicLarge(n)


if __name__ == '__main__':
    n = int(input())
    ans = harmonic(n)
    print(ans)
