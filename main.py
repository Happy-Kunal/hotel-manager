import os
from tkinter import *
from fun_viewall import viewall

# these function calls there respective commands to perform
def checkin() :

    command = "python3 fun_checkin.py"

    os.system(command)

def checkout() :

    command = "python3 fun_checkout.py"

    os.system(command)

def about() :

    command = "python3 about.py"

    os.system(command)



# creating main window on which initaial things gonna displayed
main_window = Tk()

# setting size of main_window
canvas_size = Canvas(main_window , width = 240 , height = 60)
canvas_size.pack()

main_window.title("Hotel Raj Niwas")


# creating menu
menu = Menu(main_window)
main_window.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File" , menu = filemenu)
filemenu.add_command(label = "New")
filemenu.add_command(label = "Open...")
filemenu.add_separator()
filemenu.add_command(label = "Exit" , command = main_window.quit )

creditsmenu = Menu(menu)
menu.add_cascade(label = "Credits" , menu = creditsmenu)
creditsmenu.add_command(label = "About" , command = about ) 



# creating buttons to perform tasks
button1 = Button(main_window , text = "Checkin" , command = checkin)
button2 = Button(main_window , text = "Checkout" , command = checkout)
button3 = Button(main_window , text = "Viewall" , command = viewall)



# packing the buttons
button1.pack()
button2.pack()
button3.pack()


mainloop()