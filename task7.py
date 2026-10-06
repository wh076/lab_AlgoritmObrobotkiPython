import turtle
import random


def mountain(t, x1, y1, x2, y2, depth, height):
    # базовый случай: рисуем отрезок
    if depth == 0:
        t.goto(x2, y2)
        return
    # рекурсивный случай: сдвигаем середину вверх или вниз и делим отрезок пополам
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2 + random.randint(-height, height)
    mountain(t, x1, y1, mid_x, mid_y, depth - 1, height // 2)
    mountain(t, mid_x, mid_y, x2, y2, depth - 1, height // 2)


def draw_layer(t, y, height, color):
    # рисуем один слой гор и закрашиваем его до низа экрана
    t.color(color)
    t.up()
    t.goto(-400, -300)
    t.down()
    t.begin_fill()
    t.goto(-400, y)
    mountain(t, -400, y, 400, y, 8, height)
    t.goto(400, -300)
    t.goto(-400, -300)
    t.end_fill()


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.setup(800, 600)
    myWin.bgcolor("lightblue")
    t.speed(0)
    myWin.tracer(0)
    t.hideturtle()

    # сначала дальние горы, потом ближние
    draw_layer(t, 100, 160, "gray")
    draw_layer(t, 0, 120, "dimgray")
    draw_layer(t, -120, 80, "darkgreen")

    myWin.update()
    myWin.exitonclick()


main()
