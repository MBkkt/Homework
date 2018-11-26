import _10_02.Dog.stdarray as stdarray
import _10_02.Dog.stddraw as stddraw
import random


def draw_end():
    xs, ys = x, y
    if x == n - 1:
        xs = n
    elif x == 0:
        xs = -1
    if y == n - 1:
        ys = n
    elif y == 0:
        ys = -1
    stddraw.line(x, y, xs, ys)
    stddraw.show(100)


n = 15
a = stdarray.create2D(n, n, False)
stddraw.setXscale(0, n)
stddraw.setYscale(0, n)
stddraw.setPenRadius(0.2)
stddraw.setPenColor(stddraw.YELLOW)
x = y = n // 2
while 0 < x < n - 1 and 0 < y < n - 1:
    a[x][y] = True
    x0, y0 = x, y
    if a[x - 1][y] and a[x + 1][y] and a[x][y - 1] and a[x][y + 1]:
        for i in range(2, x0 + 1):
            if not a[i][1]:
                stddraw.setPenColor(stddraw.RED)
                stddraw.filledCircle(i, 1, 0.3)
            if not a[i - 1][1]:
                stddraw.setPenColor(stddraw.WHITE)
                stddraw.filledCircle(i - 1, 1, 0.3)
            stddraw.show(100)

        for i in range(2, y0 + 1):
            if not a[x0][i]:
                stddraw.setPenColor(stddraw.RED)
                stddraw.filledCircle(x0, i, 0.3)
            if not a[x0][i - 1]:
                stddraw.setPenColor(stddraw.WHITE)
                stddraw.filledCircle(x0, i - 1, 0.3)
            stddraw.show(100)

        stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(x, y, 0.3)
        x, y = random.randrange(1, n - 1), random.randrange(1, n - 1)
        while a[x][y]:
            x, y = random.randrange(1, n - 1), random.randrange(1, n - 1)
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(x, y, 0.3)
        stddraw.setPenRadius(0.2)
        stddraw.setPenColor(stddraw.YELLOW)
    else:
        r = random.randrange(1, 5)
        if r == 1 and (not a[x + 1][y]):
            x += 1
        elif r == 2 and (not a[x - 1][y]):
            x -= 1
        elif r == 3 and (not a[x][y + 1]):
            y += 1
        elif r == 4 and (not a[x][y - 1]):
            y -= 1
        stddraw.line(x0, y0, x, y)
    stddraw.show(100)

draw_end()

