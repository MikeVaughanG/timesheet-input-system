import os
from tkinter import *

def stopProg(e):
	edit.destroy()
	
### FUNCTION TO CLEAR ALL ENTRY BOXES
def clear_all(e):
	date.delete(0,END)
	task_1.delete(0,END)
	task_2.delete(0,END)
	task_3.delete(0,END)
	hours.delete(0,END)
	miles.delete(0,END)

### FUNCTION THAT CENTERS A WINDOW
def center(window,w,h):
	ws = window.winfo_screenwidth()
	hs = window.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	window.geometry('%dx%d+%d+%d' % (w, h, x, y))

	
### GET FILENAME FROM SYSTEM ARGUMENT
ts = sys.argv[1]
# print(ts)
	
### CREATE AND CENTER WINDOW
edit = Tk()
edit.title("Edit A Timesheet")
center(edit, 250,250)

### CREATE LABELS
Label(edit,text = ts, background = "lime").grid(row = 0, columnspan =2)
Label(edit,text = "Date").grid(row = 1)
Label(edit,text = "Task 1").grid(row = 2)
Label(edit,text = "Task 2").grid(row = 3)
Label(edit,text = "Task 3").grid(row = 4)
Label(edit,text = "Hours:").grid(row = 5)
Label(edit,text = "Miles:").grid(row = 6)

### CREATE ENTRY BOXES
date = Entry(edit)
date.grid(row = 1, column = 1)
task_1 = Entry(edit)
task_1.grid(row = 2, column = 1)
task_2 = Entry(edit)
task_2.grid(row = 3, column = 1)
task_3 = Entry(edit)
task_3.grid(row = 4, column = 1)
hours = Entry(edit)
hours.grid(row = 5, column = 1)
miles = Entry(edit)
miles.grid(row = 6, column = 1)

### CREATE BUTTONS
submit = Button(edit, text = "Submit")
submit.grid(row = 7, column = 1)
clear = Button(edit, text = "Clear All", background ="red")
clear.grid(row = 8, column = 1)
clear.bind('<Button-1>', clear_all)

### START MAINLOOP
edit.mainloop()
