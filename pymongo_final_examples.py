import pymongo 
from pymongo_extra_examples import server_connect, uri
import pprint


connection = server_connect(uri)

db = connection.movieData
collection = db.movies

'''
Let's practice with some of the useful methods in PyMongo
'''

#List collection names in the database
collections_list = db.list_collection_names()
pprint.pprint(collections_list)


#create a simple query with a timeout restriction.
query1 = collection.find({"rating.average" : 
                            {"$gte" : 9.3}} ,  
                        {"rating.average" :
                         1 , "_id" : 0 , "runtime" : 1 } ).max_time_ms(1)

pprint.pprint(list(query1))



#insert a new document into the collection, along with a writeConcern to control server acknowledgement
query2 = collection.insert_one({"_id" : "Delete This" , "text" : "Hello"} , 
                                {"writeConcern" : {"w" : 1 , "j" : "true" , "wtimeout" : 10}})



#Delete the new document
query3 = collection.find({"_id" : "Delete This"})
pprint.pprint(list(query3))


#create a function that takes a dictionary and adds a datetimestamp, then inserts into the database

import datetime
def update_time_doc(current_data, collection):

    current_data["datetime"] = datetime.datetime.utcnow()
    collection.insert_one(current_data)
    return current_data



example_doc = {"_id" : 1234 , "name" : "John" , "Age" : 33}
new_doc = update_time_doc(example_doc, collection)
print(new_doc)



collection.delete_one({"_id" : 1234})
collection.delete_one({"_id" : "Delete This"})

collection.find_one({{"_id" : "Delete This"}})   

                        
#aggregation

query4 = collection.aggregate([
    {"$unwind" : "$genres"},
    {"$match" : {"rating.average" : {"$gte" : 8.5}}},
    {"$project" : {"rating.average" : 1, "_id" : 0, "name" : 1}},
    {"$group" : {"_id" : "$rating.average" , "count" : {"$sum" : 1} }},
    {"$sort" : {"count" : -1}}
])


result1 = list(query4)

pprint.pprint(result1)





