from tkinter import *
frame_width = 100
frame_height = 100
x = 100
y = 102


root = Tk()
canvas = Canvas(root, background = 'red') 
canvas.grid(column = 0, row = 0, sticky = (N,W,E,S))

root.configure(background = '#645452')
root.geometry('%dx%d+%d+%d' % (frame_width, frame_height, x, y))
root.mainloop()
