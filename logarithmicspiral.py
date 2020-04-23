import sys, random, argparse
import numpy as np
import math
import turtle
import random
from PIL import Image
from datetime import datetime
from fractions import gcd

sys.setrecursionlimit(50000)


'''
x = cos(t)(ae^bt) 
y= sin(t)(ae^bt)


x = a*math.exp(b*t)*math.cos(t)
y = a*math.exp(b*t)*math.sin(t)   

from jkings454 (github)
'''



class Spiral:
    #construct
    def __init__(self, xc, yc, col,a, b):
        #make turtle object
        self.t=turtle.Turtle()
        #set turtle cursor
        self.t.shape("arrow")
        #set ending draw flag
        self.drawingComplete=False

        #set parameters
        self.setparams(xc,yc,col,a,b)

        #restart mode
        self.restart()

        self.step=1


    def setparams(self, xc,yc,col,a, b):
        #spiral parameter
        self.xc=xc
        self.yc=yc
        self.b=float(b)
        self.a=float(a)
        self.col=col
        #set color
        self.t.color(*col)
        #save angle, help make animation
        self.c=0



    def restart(self):
        #set flag
        self.drawingComplete=False
        #show turtle
        self.t.showturtle()
        #go to first point
        self.t.up()

        a,b=self.a, self.b     

        c=0.0
        x = a*math.exp(b*c)*math.cos(c)
        y = a*math.exp(b*c)*math.sin(c)  
        self.t.setpos(self.xc +x, self.yc + y)
        self.t.down()

    def draw(self):
        a, b =self.a, self.b
        #draw another points
        for i in range(0, 2500, self.step):
        
            c=math.radians(i)
            x = a*math.exp(b*c)*math.cos(c)
            y = a*math.exp(b*c)*math.sin(c)  
            self.t.setpos(self.xc +x, self.yc + y)
            self.t.down()

        #finish so i hide turtle
        self.t.hideturtle()


    def update(self):
         if self.drawingComplete:
             return

         #++ angle
         self.c += self.step
         a, b =self.a, self.b 

         #set angle
         c=math.radians(self.c)
         
         x = a*math.exp(b*c)*math.cos(c)
         y = a*math.exp(b*c)*math.sin(c)
         
         self.t.setpos(self.xc +x, self.yc + y)
         
         if self.c >=2500:
             self.drawingComplete=True #finish drawing
             #drawing finish, so i drawing turtle
             self.t.hideturtle()


    def clear(self):
         self.t.clear()
         
class SpiralAnimator:

    def __init__(self, N):
        #set time in miliseconds
        self.deltaT=10
        #set window width and height
        self.width=turtle.window_width()
        self.height=turtle.window_height()

        #make spiral object
        self.spirals=[]
        for i in range(N):
            #generate random parameters
            rparams=self.genRandomParams()
            #set spiral parameters
            spiral=Spiral(*rparams)
            self.spirals.append(spiral)

        #timer start
        turtle.ontimer(self.update, self.deltaT)



    def restart(self):
        for spiral in self.spirals:
            #clear
            spiral.clear()
            #generate random parameters
            rparams= self.genRandomParams()
            #set spirals parameters
            spiral.setparams(*rparams)
            #reset drawing
            spiral.restart()
            

    #generate random parameters    
    def genRandomParams(self):
        width, height= self.width, self.height
        a=random.uniform(0,1)
        b=random.uniform(0,1)
        xc=random.randint(-width//2, width//2)
        yc=random.randint(-height//2, height//2)
        col=(random.random(),
             random.random(),
             random.random())
        return (xc, yc, col,b,a)

    
    def update(self):
        #update all spirals
        nComplete=0
        for spiral in self.spirals:
            #update
            spiral.update()
            if spiral.drawingComplete:
                nComplete+=1

            #if all spirals finished, you restart
            if nComplete == len(self.spirals):
                self.restart()
            #timer
            turtle.ontimer(self.update, self.deltaT)

    #turn on and off turtle cursor
    def toggleTurtles(self):
             for spiral in self.spirals:
                 if spiral.t.invisible():
                     spiral.t.hideturtle()
                 else:
                     spiral.t.showturtle()

#save spirals in image
def saveDrawing():
         #hide turtle
         turtle.hideturtle()
         #generate random name
         dateStr=(datetime.nom()).strtime("%d%b%Y-%H%M%S")
         fileName= 'spiral-' + dateStr
         print("save drawing in file %s.eps/png" % fileName)

         canvas=turtle.getcanvas()
         #save drawing in image postscript
         canvas.postscript(file = fileName + '.eps')
         #use Pillow module to converte image postricpt on PNG
         img= Image.open(fileName + '.eps') 
         img.save(fileName + 'png', 'png')
         #show turtle cursor
         turtle.showturtle()

def main():
         #use sys.argv
         print('Spiral generate-exercise')
         #parser generate
         descStr='''This program draw spiral. Use turtle module. If you don't use argument
         the program will be drawing random spirals'''

         parser=argparse.ArgumentParser(description=descStr)

         #add arguments
         parser.add_argument('--sparams', nargs=3, dest='sparams', required=False,
                             help="hello")

         args=parser.parse_args()

         #set width window 80%
         turtle.setup(width=0.8)


         #set cursor    
         turtle.shape('arrow')

         #set title
         turtle.title("Spirals")
         #add button to save image

         turtle.onkey(saveDrawing, "s")

         #hide cursor turtle main function
         turtle.hideturtle()

         #check arguments

         if args.sparams:
             params = [float(x) for x in args.sparams]
             #drawing spirals with parameters
             col=(0.0, 0.0, 0.0)
             spiral=Spiral(0, 0, col, *params)
             spiral.draw()
         else:
             spiralAnim=SpiralAnimator(2)
             #add button to turn on and off turtle cursor
             turtle.onkey(spiralAnim.toggleTurtles, "t")
             #add restart animator
             turtle.onkey(spiralAnim.restart, "space")


         #start mainloop turtle
         turtle.mainloop()
         
if __name__ == '__main__':
    main()
