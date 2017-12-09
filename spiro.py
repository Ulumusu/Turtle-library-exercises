import sys, random, argparse
import numpy as np
import math
import turtle
import random
from PIL import Image
from datetime import datetime
from fractions import gcd




class Spiro:
    def __init__(self, xc, yc, col, R, r, l):

        #create turtle object
        self.t=turtle.Turtle() #1 new object turtle
        self.t.shape('turtle') #2 #cursor like turtle

        self.step=5 #3

        self.drawingComplete=False  #4

        self.setparams(xc, yc, col, R, r, l) #5

        self.restart()  #6

    def setparams(self, xc, yc, col, R, r, l):
        #spiro parameter
        self.xc=xc
        self.yc=yc
        self.R=int(R)
        self.r=int(r)
        self.l=l
        self.col=col

        #reduce r/R
        gcdVal = gcd(self.r, self.R)
        self.nRot=self.r // gcdVal

        self.k=r/float(R)

        #set color
        self.t.color(*col)

        self.a=0 #angle pen

    def restart(self):
        #set flag
        self.drawingComplete= False
        #show turtle cursor
        self.t.showturtle()

        self.t.up() #pen up
        R,k,l=self.R, self.k, self.l
        a=0.0 #set angle
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    def draw(self):
        R,k,l=self.R, self.k, self.l
        for i in range(0, 360*self.nRot + 1, self.step ):
            a = math.radians(i) #  angle
            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
            self.t.setpos(self.xc + x, self.yc + y)

        self.t.hideturtle() #hide turtle cursor


    def update(self):
        if self.drawingComplete:
            return

        self.a += self.step
        R, k, l=self.R, self.k, self.l

        #set angle
        a = math.radians(self.a)  # angle
        x = self.R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = self.R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)

        #set flag
        if self.a >= 360*self.nRot:
            self.drawingComplete=True
            self.t.hideturtle()

    def clear(self):
        self.t.clear()


#anime spiro class

class SpiroAnimator:
    def __init__(self, N):
        #set miliseconds
        self.deltaT=10

        #get window size
        self.width= turtle.window_width()
        self.height=turtle.window_height()
        #make spiro object
        self.spiros=[]
        for i in range(N):
            #generate random parameters
            rparams = self.genRandomParams()
            spiro=Spiro(*rparams)
            self.spiros.append(spiro)

         #timer start
        turtle.ontimer(self.update, self.deltaT)


    def restart(self):
        for spiro in self.spiros:

            #clear mode
            spiro.clear()

            #generate random parameters
            rparams=self.genRandomParams()

            #set pen parameters
            spiro.setparams(*rparams)

            #drawing restart
            spiro.restart()

    def genRandomParams(self):
        width, height=self.width, self.height
        R=random.randint(50, min(width, height)//2)
        r=random.randint(10, 9*R//10)
        l=random.uniform(0.1, 0.9) #also generate random float number
        xc=random.randint(-width//2, width//2)
        yc=random.randint(-height//2, height//2)
        col=(random.random(),
             random.random(),
             random.random())
        return (xc, yc, col, R, r, l)


    def update(self):
        #update all spiro angles
        nComplete=0
        for spiro in self.spiros:
           #update
           spiro.update()
           if spiro.drawingComplete:
               nComplete += 1

        if nComplete == len(self.spiros):
           self.restart()

         #timer start
        turtle.ontimer(self.update, self.deltaT)

    def toggleTurtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t. showturtle()

def saveDrawing():
        turtle.hideturtle()
        dateStr=(datetime.now()).strftime("%d%b%Y-%H%M%S")
        fileName='spiro-' + dateStr
        print('save drawing in file %s.eps/png' % fileName)
        canvas= turtle.getcanvas()
        canvas.postscript(file = fileName + '.eps')
        img= Image.open(fileName + '.eps')
        img.save(fileName + '.png', 'png')
        turtle.showturtle()

def main():

         print("Spirograph generate")

         descStr='''This program draw Spiro and use turtle module.'''

         parser= argparse. ArgumentParser(description=descStr)

         parser. add_argument('--sparams', nargs=3, dest='sparams', required=False,
                              help='Trzy argumenty w sparams: R, r, l')

         args=parser.parse_args()

         turtle.setup(width=0.8)
         turtle.shape('turtle')
         turtle.title("Spirografy")
         turtle.onkey('saveDrawing', "s")
         turtle.listen()

         turtle.hideturtle()


         if args.sparams:
             params=[float(x) for x in args.sparams]

             col=(0.0, 0.0, 0.0)
             spiro= Spiro(0,0,col, *params)
             spiro.draw()
         else:
             spiroAnim = SpiroAnimator(4)
             turtle.onkey(spiroAnim.toggleTurtles, "t")
             turtle.onkey(spiroAnim.restart, "space")


         turtle.mainloop()


if __name__ =='__main__':
        main()