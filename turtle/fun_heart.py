#heart
import turtle as t

t.bgcolor("black")
t.pensize(2)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.speed("fastest")
t.color("red" , "pink")

t.begin_fill()
t.left(140)
t.forward(110)
curve()

t.left(120)
curve()
t.forward(111.65)
t.end_fill()
t.hideturtle()
t.done()
