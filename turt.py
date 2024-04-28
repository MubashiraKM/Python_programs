import turtle
import colorsys
s=turtle.Turtle()
turtle.bgcolor("black")
h=0.0
s.speed(0)
for i in range(200,0,-1):
    s.color(colorsys.hsv_to_rgb(h,1,1))
    for j in range(4):
        s.forward(i)
        s.right(90)
    # s.circle(i)
    s.right(4)
    h+=0.01
turtle.mainloop()