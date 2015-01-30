from tkinter import *
import os
import platform

### FUNCTION TO KILL
def stopProg(e):
	root.destroy()

### FUCNTION THAT DOES CALCULATIONS FOR CENTER OF SCREEN
### AND THEN CENTERS THE WINDOW
def center(window,w,h):
	ws = window.winfo_screenwidth()
	hs = window.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	window.geometry('%dx%d+%d+%d' % (w, h, x, y))

### FUNCTION THAT ACTIVATES IF TIMESHEET ALREADY EXISTS
def ts_exists(timesheet):

	### FUNCTION TO KILL POPUP WINDOW
	def destroy_ts_exists(e):
		win.destroy()
	
	### FUNCTION THAT STARTS Edit.py WITH RIGHT ARGUMENTS
	### KILLS Main.py
	def edit(event, ts):
		win.destroy()
		root.destroy()
		op_s = platform.system()
		print(op_s)
		if op_s == "Windows":
			os.system("python Edit.py "+'"'+ts+'"')
		elif op_s == "Linux":
			os.system("python3.4 Edit.py "+'"'+ts+'"')
	### CREATE AND CENTER POPUP WINDOW
	win = Toplevel()
	win.title("Timesheet Found")
	center(win, 250, 125)
	
	### THERE'S THIS LINE AGAIN, PRETTY SURE IT'S OKAY NOW
	win.wm_attributes('-topmost', 1)

	### LABELS
	Label(win, text = "Timesheet Found", background = "green").pack()
	Label(win, text = timesheet).pack()
	Label(win, text = "Edit This Timesheet?").pack()
	
	### BUTTONS AND BINDINGS
	n = Button(win, text = "No")
	n.pack()
	n.bind('<Button-1>', destroy_ts_exists)
	y = Button(win, text = "Yes")
	y.pack()
	y.bind('<Button-1>', 
		lambda event, ts=timesheet: edit(event, ts))
	
### FUNCTION THAT ACTIVATES IF TIMESHEET DOES NOT EXIST
def ts_no_exist(timesheet, case):
	### FUNCTION TO KILL POPUP WINDOW
	def destroy_ts_no_exist(e):
		pop.destroy()
	
	### FUNCTION THAT STARTS Create.py WITH THE APPROPRIATE ARGUMENTS
	def edit(event, ts):
		pop.destroy() 
		root.destroy()
		
		op_s = platform.system()
		print(op_s)
		if op_s == "Windows":
			os.system("python Edit.py "+'"'+ts+'"')
		elif op_s == "Linux":
			os.system("python3.4 Edit.py "+'"'+ts+'"')

	### CREATE AND CENTER POPUP WINDOW
	pop = Toplevel()
	pop.title("Timesheet Doesn't Exist")
	center(pop, 250, 125)
	
	## THIS LINE IS A TOTAL NO-GO ---- ???? KEEPS ON TOP?? ...wtf
	pop.wm_attributes('-topmost', 1)

	### LABELS
	Label(pop, text = "Timesheet does not exist.", background = "red").pack()
	Label(pop, text = "Create Time sheet?").pack()
	
	### BUTTONS AND BINDINGS
	n = Button(pop, text = "No")
	n.pack()
	n.bind('<Button-1>', destroy_ts_no_exist)
	y = Button(pop, text = "Yes")
	y.pack()
	y.bind('<Button-1>', 
		lambda event, ts=timesheet: edit(event, ts))
		
### SUBMIT FUNCTION
### USES FIRST AND LAST NAME TO FORMAT A FILENAME
### CHECKS IF IT EXISTS, AND ACTIAVTES THE APPROPRIATE FUNCTION
def submit(e):
	first = f_name.get()
	last = l_name.get()
	case = case_no.get()
	#format a file name from user input
	full_fn = last.upper()+", "+first.upper()+" "+case.upper()+".txt"
	if os.path.isfile(full_fn) == False:
		ts_no_exist(full_fn, case)
	elif os.path.isfile(full_fn):
		ts_exists(full_fn)

		
###################
### DRAWING GUI ###		
###################

### CREATE MAIN WINDOW
root = Tk()
root.title("Select Timesheet")

### CENTER WINDOW
center(root, 252, 125)

### CREATING AND PLACING LABELS
Label(root,text = "First Name").grid(row = 0)
Label(root, text = "Last Name").grid(row = 1)
Label(root, text = "Case #").grid(row = 2)

### CREATING AND PLACING ENTRY BOXES
f_name = Entry(root)
f_name.grid(row = 0, column = 1)
l_name = Entry(root)
l_name.grid(row = 1, column = 1)
case_no= Entry(root)
case_no.grid(row = 2, column = 1)

### CREATING, PLACING AND BINDING BUTTONS
submit_but = Button(root, text = "Submit")
submit_but.grid(row = 3)
submit_but.bind('<Button-1>', submit)

### START MAINLOOP
root.mainloop()
