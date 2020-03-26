from tkinter.messagebox import showerror
from tkinter import Tk

def about() :
	
	# don't try to play with this string cause this string is for creadits and practically 
	# formatted avoid to edit this cause it can ruin the whole creadits window
	str1 = """ 
            This program is 
output of hard and kind efforts of our team who spent more than 2 weeks to bring this 
program and make it working and finally hats of to the developer bench :- 

       Founding Members : 

          Kunal Sharma 
(frontend , logic developer),
         Aman Sharma
(backend , logic developer)
	
      Supportive Members :

Himanshu Jha , Vikas Kumar , Suraj Shukla , Dhrijan Kumar , Vasnavi Sharma

     Special Thanks To : 
	
        Shri Vinod sir
	
	"""

	# as expaiend that showerror makes one extra blank window which we don't want to get displayed so we used Tk().withdraw() 
	Tk().withdraw()
	# displaying our data of all clients
	showerror(title = "About" , message = str1)

about()