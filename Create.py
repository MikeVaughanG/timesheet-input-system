from tkinter import *
import os
import sys

### FUNCTION TO CLEAR ALL ENTRY BOXES ###
def clear_all(e):
	atty.delete(0,END)
	crg.delete(0,END)

### FUNCTION THAT CENTERS A WINDOW ###
def center(window,w,h):
	ws = window.winfo_screenwidth()
	hs = window.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	window.geometry('%dx%d+%d+%d' % (w, h, x, y))

def write_lines(event, timesheet, case_n):
		# GET INFO
		attorney = atty.get()
		charges = charge.get()
		names = timesheet.split(",")
		last = names[0]
		first = names [1]
		print(first+" "+last)
		#WRITE LINES TO FILE
		
		
		
		
### GET TIMESHEET FROM SYS ARGUMENTS BEING PASSED FROM Main.py
ts = sys.argv[1]
case_no = sys.argv[2]
### GURANTEE TIMESHEET DOESNT EXIST, THEN CREATE IT
if os.path.isfile(ts) == False:
	file = open(ts,"w")
	file.close()

#####################
#### DRAWING GUI ####
#####################
	
### CREATING WINDOW
create = Tk()
create.title("Create Timesheet")

### CREATING AND PLACING LABELS
Label(create, text = ts, background = "lime").grid(row = 1, columnspan = 2)
Label(create, text = "Attorney:").grid(row = 2)
Label(create, text = "Case Num: "+case_no).grid(row = 3, columnspan = 2)
Label(create, text = "Charges :").grid(row = 4)

### CREATING AND PLACING ENTRY BOXES
atty = Entry(create)
atty.grid(row = 2, column = 1)
charge = Entry(create)
charge.grid(row = 4, column = 1)

### CREATING, PLACING, AND BINDING BUTTONS
sub = Button(create, text = "Submit")
sub.grid(row = 6)
sub.bind('<Button-1>', 
		lambda event, sheet=ts: write_lines(event, ts, case_no))
clear_a = Button(create, text = "Clear")
clear_a.grid(row = 7)
clear_a.bind('<Button-1>', clear_all)



create.mainloop()