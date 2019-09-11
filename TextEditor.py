# Text Editor 

import tkinter
import tkinter.scrolledtext as ScrolledText
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox



# Root for main window
root = tkinter.Tk(className = " Text Editor")

# set the weight of each of the grid's rows and columns to 1 to allow resizing of grid within root
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
root.resizable(width = True, height = True) # allow the width and height of the root to be resizable

def function(): # place holder function
	return

def open_file():
    file = filedialog.askopenfile(parent = root, mode = "rb", title = "Select a text file")
    
    if file != None:
    	contents = file.read()
    	textArea.insert('1.0', contents)
    	file.close()

def save_file():
	file = filedialog.asksaveasfile(mode="w")

	if file != None:
		# slice off the last character from get, as an extra return (enter) is added
		data = textArea.get('1.0', tkinter.END + "-1c")
		file.write(data)
		file.close()

def about():
	label = messagebox.showinfo("About", "A text editor based on DiogoTheCoder's python text editor, made by AhmedHaj")


def exit_root():
	if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
		root.destroy()

	

# ScrolledText is class name, root and width height as params.
textArea = ScrolledText.ScrolledText(root)
textArea.grid(sticky = "NEWS") # stretches the text area in all 4 directions (NORTH EAST WEST SOUTH)


# creating a root menu to insert all the sub menus
root_menu = tkinter.Menu(root)
root.config(menu = root_menu)

# creating sub menus in the root menu
file_menu = tkinter.Menu(root_menu) # it intializes a new su menu in the root menu
root_menu.add_cascade(label = "File", menu = file_menu) # it creates the name of the sub menu
file_menu.add_command(label = "New File", command = function) # it adds a option to the sub menu 'command' parameter is used to do some action
file_menu.add_command(label = "Open...", command = open_file)
file_menu.add_command(label = "Save", command = save_file)
file_menu.add_separator() # it adds a line after the 'save' option
file_menu.add_command(label = "About", command = about)
file_menu.add_command(label = "Exit", command = exit_root)


# creating another sub menu
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", command = function) # TODO
edit_menu.add_command(label = "Redo", command = function) # TODO

# keeps the window open
root.mainloop()

