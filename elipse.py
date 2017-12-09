import math
import turtle


def drawEcllipse(x, y, z, q):
    turtle.up()
    turtle.setpos(x+z, y)
    turtle.down()

    for i in range(0, 365):
        a=math.radians(i)
        turtle.setpos(x+z*math.cos(a), y+q*math.sin(a))

drawEcllipse(0,0, 300, 100)
turtle.mainloop()