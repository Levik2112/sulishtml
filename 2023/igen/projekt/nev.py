from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

# Rajzolás
canvas.create_line(10, 50, 40, 50, width=2)  # L betű
canvas.create_line(60, 50, 60, 20, 50, 20, 50, 40, 60, 40, width=2)  # E betű
canvas.create_line(70, 20, 90, 50, 70, 50, 85, 35, 75, 35, 75, 25, 85, 25, width=2)  # V betű
canvas.create_line(100, 50, 100, 20, 110, 20, 110, 40, 100, 40, width=2)  # E betű
canvas.create_line(120, 20, 120, 50, 130, 50, 130, 20, 120, 20,  width=2)  # N betű
canvas.create_line(140, 50, 170, 50, width=2)  # T betű

root.mainloop()
