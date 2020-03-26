from tkinter.messagebox import showerror
from tkinter import Tk
import pymongo

# to display the data of all current guest
def viewall() :
	
    # connecting to mongoDB
    client = pymongo.MongoClient()
    db = client.hotel123

	# making blank string so that it could be used to store the message to be display
    str1 = ""
	# retrieving data from database of all students
    data = db.hotel123.find()
    data = tuple(data)
	
	#formating the str t hold informations	
    for i in data :
			
    	str1 += f"{i} \n\n"
	
	# as expaiend that showerror makes one extra blank window which we don't want to get displayed so we used Tk().withdraw() 
    Tk().withdraw()
	# displaying our data of all clients
    showerror(title = "All Client Details" , message = str1)
