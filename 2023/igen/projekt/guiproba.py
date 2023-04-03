# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x500")


# Create a canvas widget
canvas=Canvas(win, width=500, height=300,bg="skyblue")
canvas.pack(fill = BOTH, expand = 1)

#canvas2=Canvas(win, width=500, height=300,bg="green")
#canvas2.pack(fill = BOTH, expand = 1)


# Add a line in canvas widget
#canvas.create_line(100,200,200,35, fill="green", width=10)
#canvas.create_line(0,0,200,35,20,300,700,500, fill="red", width=10)
#canvas.create_line(10, 100, 50, 0, 100, 100, fill="red")
canvas.create_line(100, 50, 100, 100, 50, 100,50,100,100,50, fill="green")



win.mainloop()
