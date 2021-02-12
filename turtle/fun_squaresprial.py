#square spiral
import turtle as t
t.speed("fastest")
t.bgcolor("black")

for i in range (5):
     for colours in ["red", "magenta" , "blue" , "cyan" , "green" , "yellow" , "white"]:#ask child to do it 2 decogon
         t.color(colours)
         t.pensize(3)
         t.left(12)
         t.forward(200)
         t.left(90)
         t.forward(200)
         t.left(90)
         t.forward(200)
         t.left(90)
         t.forward(200)
         t.left(90)
t.done()
