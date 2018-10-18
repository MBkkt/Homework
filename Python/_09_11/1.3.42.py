from itertools import count


def time_stable(r, x=0.01):
    stable = 1 - 1 / r
    for t in count():
        if abs(x - stable) < 0.01:
            return t
        elif t >= 10000000:
            return 'Не стабилизируется'
        x *= r * (1 - x)


if __name__ == '__main__':
    n = int(input())
    for r in (n, 3.5, 3.8, 5):
        t = time_stable(r)
        print(t)
