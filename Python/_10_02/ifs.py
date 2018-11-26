from random import random
from matplotlib import pyplot as plt
import numpy as np


def discrete(a):
    t = sum(a)*random()
    subtotal = 0.0
    for j in range(len(a)):
        subtotal += a[j]
        if subtotal > t:
            return j


def tabler():
    n, *m = map(int, input().split(' '))
    return [[float(x) for x in input().split(' ')] for _ in range(n)] if m else [float(x) for x in input().split(' ')]


rep = 100000 or int(input())
ps, xs, ys = (tabler() for _ in range(3))

w, h = 1024, 1024
im = np.empty((w, h), np.uint8)
x = y = 0.0
for i in range(rep):
    r = discrete(ps)
    x0 = xs[r][0] * x + xs[r][1] * y + xs[r][2]
    y0 = ys[r][0] * x + ys[r][1] * y + ys[r][2]
    x, y = x0, y0
    im.itemset((int(y * w), int(x * h)), 255)
plt.imshow(im, origin='')
plt.show()