from tkinter import *
import os

def initialize_program():
    global root
    global window
    root = Tk()
    root.title("Mouse movements visualised")
    root.wm_title("Mouse plot")
    window = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    window.pack()


def format_coord(line):
    split_line = line.split(' ')
    x = split_line[0]
    y = split_line[1].strip('\n')
    return x,y


def text_file_line_count(file):
    with open(file, 'r') as f:
        return sum(1 for line in f)


def draw_mouse_coords(file):
    with open(file,'r') as coords_file:
        a = 0
        for line in coords_file:
            a = a + 1
            if a == 1:
                coord_1 = format_coord(line)
            elif a % 2 == 0:
                coord_2 = format_coord(line)
                window.create_line(coord_1[0],coord_1[1],coord_2[0],coord_2[1])
            else:
                coord_1 = format_coord(line)
                window.create_line(coord_2[0],coord_2[1],coord_1[0],coord_1[1])


def average_point_file(file):                                          #iterates through a text file full of points and returns the average x and average y
    i = text_file_line_count(file)
    total_x = 0
    total_y = 0
    with open(file, 'r') as f:
        for line in f:
            split_line = line.split(" ")
            total_x += int(split_line[0])
            total_y += int(split_line[1].strip("\n"))
    average_x = total_x/i
    average_y = total_y/i
    return average_x, average_y


def average_point_directory(directory):                           #iterates through every file in a directory and returns the average x and average y out of all the files
    total_x = 0
    total_y = 0
    i = 0
    for file in os.listdir(directory):
        i += 1
        total_x += average_point_file(os.path.join(directory, file))[0]
        total_y += average_point_file(os.path.join(directory, file))[1]
    average_x = total_x/i
    average_y = total_y/i
    return average_x, average_y


mouse_coord_directory = 'C:\Python34\Scripts\Tracking mouse\mouse_coords_file'
mouse_coord_example_file = os.path.join(mouse_coord_directory, "mouse_coords14.txt")

print(average_point_directory(mouse_coord_directory))




#initialize_program()
# window.create_oval(average_x - 5, average_y - 5, average_x + 5, average_y + 5, fill = 'red')
#root.mainloop()