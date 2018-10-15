"""1. Расстояние Хемминга. Расстояние Хемминга (Hamming distance) между двумя
строками битов длиной n равно количеству битов, по которым отличаются
эти две строки. Составьте программу, получающую из командной строки
целое число k и битовую строку s, а выводящую все битовые строки, у которых
расстояние Хемминга больше k из s. Например, если k = 2, а s - 0000, то
ваша программа должна вывести
0011 0101 0110 1001 1010 1100
Подсказка: выберите k из n битов в строке s для перестановки. """



def hamming(s1, s2):
    """Вычисляем расстояние Хэмминга"""
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def ans(s, k):
    n = len(s)
    for s2 in range(2 ** n):
        s2 = ('0' * (n - 1) + str(bin(s2))[2:])[-n:]
        if hamming(s, s2) == k:
            yield s2


if __name__ == '__main__':
    k = int(input())
    s = input()
    print(*ans(s, k))
