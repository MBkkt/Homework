import turtle
from random import randrange


def tree(branchLen, t, alpha, static):
    if branchLen > 5:
        t.width(0)
        t.forward(branchLen)
        t.right(alpha)
        x = static or randrange(5, 16, 5)
        tree(branchLen - x, t, alpha, static)
        t.left(alpha * 2)
        tree(branchLen - x, t, alpha, static)
        t.right(alpha)
        y = branchLen//10
        t.width(y)
        if branchLen - x <= 5:
            t.color('green')
        else:
            t.color('brown')
        t.backward(branchLen)


def draw(len_=80, alpha=30, static=0):
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color('green')
    t.speed(5000)
    tree(len_, t, alpha, static)
    myWin.exitonclick()


if __name__ == '__main__':
    draw(static=0)
