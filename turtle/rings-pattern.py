#rings
import turtle as t

t.bgcolor("black")
t.speed(0)

t.penup()
t.goto(-200,0)
t.pendown()

for i in range(3):
     for colours in ["red" , "magenta" , "blue" , "cyan" , "green" , "yellow" , "white"]:
         t.color(colours)
         t.pensize(3)
         t.circle(150)
         t.forward(20)
t.done()
