# importing modules

import pymongo


# remove() will be call from checkout1 so that to remove details after being checkout
def remove(room_num) :

    # connecting to mongoDB

    client = pymongo.MongoClient()
    db = client.hotel123
	
	
	# removing data from database 
    db.hotel123.remove({"room_num" : room_num})
