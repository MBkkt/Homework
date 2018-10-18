"""Биномиальные коэффициенты. Составьте программу, создающую и выводящую
двумерный массив с переменной длиной строк а таким образом,
чтобы элемент а [ n ] [ k] содержал вероятность получить k орлов при
n бросках монеты. Для определения максимального значения n используйте
аргумент командной строки. Эти числа известны как биномиальное
распределение: если умножить каждый элемент ряда k на 2", то получатся
биномиальные коэффициенты (коэффициенты х!' в (х+ 1 )"), упорядоченные
в треугольник Паскаля. Для их вычисления начните с а[ n] [О] = О. О
для всех n и а [ 1 ] [ 1 ] = 1 . О, затем вычислите значения в последующих
рядах, слева направо, как а[n][k] = (a[n- 1 ][k] + a [n-1 J[k-1 ] )/2. 0. """

from fractions import Fraction


class Pascal:
    def __init__(self, n):
        """Создаем треугольник Паскаля n-строк"""
        self.pas = [[0 for j in range(n)] for i in range(n)]
        self.pas[0][0] = 1
        for i in range(1, n):
            for j in range(i + 1):
                if i - 1 >= 0:
                    self.pas[i][j] += self.pas[i - 1][j]
                    if j - 1 >= 0:
                        self.pas[i][j] += self.pas[i - 1][j - 1]
        self.n = n

    def __str__(self):
        """Строковое прдставление"""
        string = ''
        for i in range(self.n):
            string += ' '.join(map(lambda x: str(x) if x else '', self.pas[i])) + '\n'
        return string

    def binary(self, b=True):
        """Приводим треугольник Паскаля к биномиальным коэффицентам или обратно"""
        for i in range(1, self.n):
            for j in range(i + 1):
                self.pas[i][j] = Fraction(self.pas[i][j] / 2 ** i) if b else self.pas[i][j] * 2 ** i


if __name__ == '__main__':
    p10 = Pascal(10)
    print(p10)
    p10.binary()
    print(p10)
    p10.binary(b=False)
    print(p10)
