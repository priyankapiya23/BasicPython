import turtle as t;
for i in range(2):
    for j in range(6):
        t.stamp()
        t.forward(20)
    t.left(90)
    for k in range(6):
        t.stamp()
        t.forward(40)
    t.left(90)
t.done()
