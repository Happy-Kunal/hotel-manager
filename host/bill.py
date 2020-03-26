from datetime import datetime
from datetime import *
from tkinter.messagebox import showerror
from tkinter import *
import pymongo

def bill(room_num):

    # connecting to mongoDB

    client = pymongo.MongoClient()
    db = client.hotel123

    # retreiving data

    data = db.hotel123.find_one({"room_num" : room_num})
    
    # retreveing dates of checkin and checkout 
    date_of_checkin = data["date_of_checkin"]
    date_of_checkout = data["date_of_checkout"]


    # finding number of days
    number_of_days = date_of_checkout - date_of_checkin

    # since currently it is in deltatime format converting it into int
    number_of_days = str(number_of_days)
    number_of_days = number_of_days.partition(" ")
    
    number_of_days = int(number_of_days[0])


    # increasing room count by 1 as if the person will checkout on the same day he will have to pay minimum due it will also 
    # benificial to the hotel as if someone checkin even in late night he have to pay rent for that day also

    number_of_days += 1

    rate_per_day = 5500

    # string to be formated so that it can contain all details
    str1 = ""

	# organising the data in information
    for i in data.keys() :
		
    	str1 += str(i) + " : " + str(data[i]) + "\n"
	
    # adding bill amount clause
    str1 += "Bill amount : {}".format(number_of_days * rate_per_day)

    
	
    # withdraw is used as whenever showerroe is used it creates one additional blank tkinter window which we don't want
    Tk().withdraw()
	
    # currently I can't find to correct syntax(due to i get exuasted of daily 2GB) of showinfo to display data so I used showerror for 
    # the time being , we will update it to showinfo in later version'
    showerror(title = "Bill details" , message = str1)

