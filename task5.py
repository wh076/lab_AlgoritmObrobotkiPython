import turtle
import random


def set_pen(branchLen, t):
    # чем длиннее ветка, тем она толще
    t.width(branchLen // 10 + 1)
    # короткие ветки - листья
    if branchLen < 30:
        t.color("green")
    else:
        t.color("brown")


def tree(branchLen, t):
    # базовый случай: ветка слишком короткая, ничего не рисуем
    # рекурсивный случай
    if branchLen > 5:
        right_angle = random.randint(15, 45)
        left_angle = random.randint(15, 45)
        right_cut = random.randint(10, 20)
        left_cut = random.randint(10, 20)

        set_pen(branchLen, t)
        t.forward(branchLen)

        t.right(right_angle)
        tree(branchLen - right_cut, t)

        t.left(right_angle + left_angle)
        tree(branchLen - left_cut, t)

        # возвращаемся в исходное направление и точку
        t.right(left_angle)
        set_pen(branchLen, t)
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    myWin.tracer(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    tree(110, t)
    myWin.update()
    myWin.exitonclick()


main()
