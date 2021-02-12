"circle pattern"
import turtle as t 
colors=["red","purple","green","blue"]
t.bgcolor("black")
s=t.Pen()
for i in range(360):
    s.pencolor(colors[i % 4])
    s.width(i/100 + 1)
    s.forward(i)
    s.left(59)

t.done()
