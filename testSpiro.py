import math
import turtle



def drawCircleTurtle(x,y,r):
    #drwaing circle by turtle
    turtle.up() #pen up
    turtle.setpos(x+r,y) #setting position
    turtle.down() #start drawing


    for i in range(0,365,5):
        a=math.radians(i) #radians
        turtle.setpos(x+r*math.cos(a), y+r*math.sin(a))


drawCircleTurtle(100, 100, 50)
turtle.mainloop()