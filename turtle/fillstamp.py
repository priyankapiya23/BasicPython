#fill stamp
import turtle as t;
t.fillcolor("red")
for i in range(10):
    for j in range(6):
        t.stamp()
        t.begin_fill()
        t.fd(30)
        t.lt(30)
        t.fd(30)
        t.lt(60)
        t.fd(30)
        t.end_fill()
    t.lt(30)
t.done()
