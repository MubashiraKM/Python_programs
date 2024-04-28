import turtle
s=turtle.Turtle()
s.shape("turtle")
turtle.bgcolor("black")
s.color("white")
s.speed(0)
for i in range(100):
    for j in range(200):
        s.forward(i)
        s.right(i)
        s.left(j)
        s.backward(j)
turtle.mainloop()