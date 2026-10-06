import turtle


def draw_triangle(t, points, color):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()


def middle(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]


def sierpinski(t, points, depth, colors):
    # рисуем треугольник, цвет зависит от уровня
    draw_triangle(t, points, colors[depth])
    # базовый случай: глубина 0, дальше не делим
    if depth == 0:
        return
    # рекурсивный случай: делим на 3 угловых треугольника
    sierpinski(t, [points[0], middle(points[0], points[1]), middle(points[0], points[2])], depth - 1, colors)
    sierpinski(t, [points[1], middle(points[0], points[1]), middle(points[1], points[2])], depth - 1, colors)
    sierpinski(t, [points[2], middle(points[2], points[1]), middle(points[0], points[2])], depth - 1, colors)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.hideturtle()
    colors = ["blue", "red", "green", "yellow", "violet", "orange"]
    points = [[-250, -200], [0, 230], [250, -200]]
    sierpinski(t, points, 5, colors)
    myWin.exitonclick()


main()
