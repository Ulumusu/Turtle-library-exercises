import math
import turtle

def drawSpiral(x, y, z):
    turtle.up()
    turtle.setpos(x+z, y)
    turtle.down()

    for i in range(0, 1800):
        a=math.radians(i)
        turtle.setpos(x+(z**a)*math.cos(a), y+(z**a)*math.sin(a))

drawSpiral(0,0,1.15)
turtle.mainloop()