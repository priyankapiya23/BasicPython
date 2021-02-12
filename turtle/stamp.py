"stamp"
import turtle as t
for i in range(18):
    t.stamp()
    t.left(20)
    t.forward(20)

for i in range(4):
    for j in range(3):
        t.stamp()
        t.fd(50)
    t.right(90)
t.done()
