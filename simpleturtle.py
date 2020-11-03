import turtle as t
#to draw circle
t.circle(100)


#draw rectangle without repeat
t.fd(100)
t.right(90)
t.fd(200)
t.right(90)
t.fd(100)
t.right(90)
t.fd(200)
t.right(90)


#draw square without repeat
t.fd(100)
t.right(90)
t.fd(100)
t.right(90)
t.fd(100)
t.right(90)
t.fd(100)
t.right(90)


#to draw shapes
n=eval(input("enter number of sides"))
for i in range(n):
    t.fd(50)
    t.right(360/n)
t.done()
