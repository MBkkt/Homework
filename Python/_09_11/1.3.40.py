import random


def brosok(x, y, n=1000000):
    win = 0
    for _ in range(n):
        k = 0
        for i in range(x):
            if random.randrange(1, 7) == 1:
                k += 1
        if k == y:
            win += 1
    return win / n


if __name__ == '__main__':
    print(brosok(6, 1))
    print(brosok(12, 2))
