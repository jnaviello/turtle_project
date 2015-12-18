import turtle


def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(120)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range (3):
        some_turtle.forward(80)
        some_turtle.right(120)


def draw_circle(some_turtle):
    for i in range (1, 37):
        some_turtle.circle(100)
        some_turtle.right(10)

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    jason= turtle.Turtle()
    jason.shape("turtle")
    jason.speed(20)
    jason.color("red")
    jason.home()
    for i in range(47):
        draw_square(jason)
        jason.right(10)

    nissa = turtle.Turtle()
    nissa.shape("turtle")
    nissa.speed(20)
    nissa.color("blue")
    nissa.home()
    draw_circle(nissa)

    bella = turtle.Turtle()
    bella.shape("arrow")
    bella.color("orange")
    bella.speed(20)
    for i in range(1, 47):
        draw_triangle(bella)
        bella.right(10)
    bella.home()
    bella.right(90)
    bella.forward(375)
    window.exitonclick()

draw_flower()




