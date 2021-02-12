#3 function to show the function calling
import turtle as t;


def squarefunc(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

def trifunc(size):
    for i in range(3):
        t.forward(size)
        t.left(120)


def circlefunc(size):
    t.circle(size)



trifunc(20)
squarefunc(100)
circlefunc(50)
t.done()
