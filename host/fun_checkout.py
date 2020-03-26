from datetime import datetime
from tkinter import *
import pymongo

from bill import bill
from remove import remove


def new_checkout() :

    # creating main window
    checkout_window = Tk()

    # declaring variables
    room_num = IntVar()
    date_of_checkout = StringVar()

    # creating entry wigets
    e1 = Entry(checkout_window , textvariable = room_num)
    e2 = Entry(checkout_window , textvariable = date_of_checkout)

    # creating label wigets to show message
    l1 = Label(checkout_window , text = "Room Number")
    l2 = Label(checkout_window , text = "Date Of Checkout")

    # declaring function to enter data in mongoDB about checkout
    def mongodb() :

        # taking input from entry boxes
        room_num1 = room_num.get()
        date_of_checkout1 = date_of_checkout.get()

        date_of_checkout1 = datetime.strptime(date_of_checkout1 , "%d/%m/%Y")


        # connecting and entering data in MongoDB
        client = pymongo.MongoClient()

        db = client.hotel123

        db.hotel123.update_one({"room_num" : room_num1} , { "$set" : {"date_of_checkout" : date_of_checkout1} })
        

        bill(room_num1)
        remove(room_num1)

        checkout_window.destroy()


    # creating button to call above function
    button1 = Button(checkout_window , text = "Submit" , command = mongodb)

    # putting things on the screen
    e1.grid(row = 1 , column = 1)
    e2.grid(row = 2 , column = 1)
    
    l1.grid(row = 1 , column = 0)
    l2.grid(row = 2 , column = 0)


    button1.grid(row = 3 , column = 0 , columnspan = 2)


    mainloop()

new_checkout()   