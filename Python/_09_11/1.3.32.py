from itertools import permutations as per


def sum3(n):
    unique = set()
    temp = int(n ** (1 / 3)) + 1
    for a, b, c, d in per(range(1, temp), 4):
        s = a ** 3 + b ** 3
        if s == c ** 3 + d ** 3 and s < n and s not in unique:
            unique.add(s)
            yield s


if __name__ == '__main__':
    num = int(input())
    for i in sum3(num):
        print(i)
