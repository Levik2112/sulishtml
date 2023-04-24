#Import the required libraries
from tkinter import *
import math

class forgato:
    canvas=0
    vonalak=[]
    szog=0
    szogsebesseg=0.5
    def __init__(self,canvas,vonalak):
        self.canvas=canvas
        self.vonalak=vonalak

    for i,betu in enumerate(self.vonalak):
        betu+=betu[:2]
        betu=nagyit(betu,10)
        self.vonalak[i]=self.eltol(betu,200,200)
    def rajzol(self):
        szog=0
        canvas.delete("all")
        self.szog+=self.szogsebesseg
        #print(szog)
        
        for betu in self.vonalak:
            betu=self.eltol(betu,-kozep[0],-kozep[1])
            betu=self.nagyit(betu,0.5)
            betu=self.forgat(betu,self.szog)
            betu=self.eltol(betu,kozep[0],kozep[1])
            
            self.canvas.create_line(betu,fill="green",width=1)
          
    def eltol(self,pontok,x,y):
        vissza=[]
        for i, pont in enumerate(pontok):
            if i%2==0:
                vissza.append(pont+x)
            else:
                vissza.append(pont+y)
        return vissza

    def nagyit(self,pontok,meret=1):
        vissza=[]
        for pont in pontok:
            vissza.append(pont*meret)
        return vissza

    def forgat(self,pontok,szog):
        vissza=[]

        for i, pont in enumerate(pontok):
            if i%2==0:
                szogRadian=math.radians(szog)
                
                x=pontok[i]*math.cos(szogRadian)-pontok[i+1]*math.sin(szogRadian)
                y=pontok[i]*math.sin(szogRadian)+pontok[i+1]*math.cos(szogRadian)
                vissza.append(x)
                vissza.append(y)
                
        return vissza


# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("600x700")

# Create a canvas widget
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
canvas.pack(fill = BOTH,expand = 1)

# Add a line in canvas widget
"""canvas.create_line(10,10,30,10, fill="green", width=5)
canvas.create_line(30,10,90,60, fill="green", width=5)
canvas.create_line(90,60,150,10, fill="green", width=5)
canvas.create_line(150,10,170,10, fill="green", width=5)
canvas.create_line(150,170,170,170, fill="green", width=5)
canvas.create_line(10,170,30,170, fill="green", width=5)
canvas.create_line(10,10,10,170, fill="green", width=5)
canvas.create_line(30,30,30,170, fill="green", width=5)
canvas.create_line(170,10,170,170, fill="green", width=5)
canvas.create_line(150,30,150,170, fill="green", width=5)
canvas.create_line(30,30,90,80, fill="green", width=5)
canvas.create_line(90,80,150,30, fill="green", width=5)
"""

pontok0 = [10,10,30,10,30,10,90,60,90,60,150,10,150,10,170,10,150,170,170,170,10,170,30,170,10,10,10,170,30,30,30,170,170,10,170,170,150,30,150,170,30,30,90,80,90,80,150,30]

M = [10,10,30,10,90,60,150,10,170,10,170,170,150,170,150,30,90,80,30,30,30,170,10,170,10,10]
nev=[M]
elso=forgato(canvas,nev)
#for i in range(5):
 #   nev.append(eltol(M,100*i,10))

#canvas.create_line(M, fill="red", width=5)
m2=eltol(M,100,50)
#canvas.create_line(m2,fill="green",width=6)
kozep=[0,0]
db=0
for betu in nev:
    xK=betu[::2]
    yK=betu[1::2]
    kozep[0]+=sum(xK)
    kozep[1]+=sum(yK)
    db+=len(xK)
kozep[0]/=db
kozep[1]/=db

while True:
    elso.rajzol()
    win.update_idletasks()
    win.update()

