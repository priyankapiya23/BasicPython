print("hey this is turtle program")
import turtle as t
from turtle import *

"star"
for i in range(5):
    t.fd(100)
    t.left(720/5)

"square"
for i in range(4):
    t.forward(100)
    t.right(90)

"trinage"
for i in range(3):
    t.forward(100)
    t.right(120)


"stamp"
for i in range(20):
    stamp()
    left(20)
    forward(20)

"circle pattern"
colors=["red","purple","green","blue"]
t.bgcolor("black")
s=t.Pen()
for i in range(360):
    s.pencolor(colors[i % 4])
    s.width(i/100 + 1)
    s.forward(i)
    s.left(59)

t.done()
