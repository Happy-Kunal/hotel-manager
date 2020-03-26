from datetime import datetime
from tkinter import *
import pymongo


def new_checkin() :

    # creating main window
    checkin_window = Tk()

    # declaring variables
    room_num = IntVar()
    name = StringVar()
    age = IntVar()
    gender = StringVar()
    date_of_checkin = StringVar()

    # creating entry wigets
    e1 = Entry(checkin_window , textvariable = room_num)
    e2 = Entry(checkin_window , textvariable = name)
    e3 = Entry(checkin_window , textvariable = age)
    e4 = Entry(checkin_window , textvariable = gender)
    e5 = Entry(checkin_window , textvariable = date_of_checkin)

    # creating label wigets to show message
    l1 = Label(checkin_window , text = "Room Number")
    l2 = Label(checkin_window , text = "Name")
    l3 = Label(checkin_window , text = "Age")
    l4 = Label(checkin_window , text = "Gender")
    l5 = Label(checkin_window , text = "Date Of Checkin")

    # declaring function to enter data in mongoDB
    def mongodb() :

        # taking input from entry boxes
        room_num1 = room_num.get()
        name1 = name.get()
        age1 = age.get()
        gender1 = gender.get()
        date_of_checkin1 = date_of_checkin.get()

        date_of_checkin1 = datetime.strptime(date_of_checkin1 , "%d/%m/%Y")


        # connecting and entering data in MongoDB
        client = pymongo.MongoClient()

        db = client.hotel123

        db.hotel123.insert_one({"room_num" : room_num1 , "name" : name1 , "age" : age1 , "gender" : gender1 , "date_of_checkin" : date_of_checkin1})

        checkin_window.destroy()


    # creating button to call above function
    button1 = Button(checkin_window , text = "Submit" , command = mongodb)

    # putting things on the screen
    e1.grid(row = 1 , column = 1)
    e2.grid(row = 2 , column = 1)
    e3.grid(row = 3 , column = 1)
    e4.grid(row = 4 , column = 1)
    e5.grid(row = 5 , column = 1)
    
    l1.grid(row = 1 , column = 0)
    l2.grid(row = 2 , column = 0)
    l3.grid(row = 3 , column = 0)
    l4.grid(row = 4 , column = 0)
    l5.grid(row = 5 , column = 0)

    button1.grid(row = 6 , column = 0 , columnspan = 2)


    mainloop()

new_checkin()   