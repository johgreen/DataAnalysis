import pymongo
import pprint #pretty print


uri = "mongodb://127.0.0.1:27017/"
client = pymongo.MongoClient(uri) #Connect to a local MongoDB server


db = client.movieData #Access the "movieData" database
movies = db.movies #Access the "movies" collection
print(movies.find_one()) #print a document


for docs in movies.find({"runtime" : {"$gt" : 60}}): #example query
    pprint.pprint(docs)

#########################

#aggregation examples
#Find the most common movie genre from an array
pipeline = [
    {"$unwind" : "$genres"},
    {"$group" : {"_id" : "$genres" , "count" : {"$sum" : 1}}},
    {"$sort" : {"count" : -1}},
    {"$limit" : 30}
]
query1 = list(movies.aggregate(pipeline))
pprint.pprint(query1)

#find all movies with "Drama" and "Action" in the genre array

pipeline2 = [
    {"$match" : {"genres" : {"$all" : ["Drama" , "Action"]}}}
]
query2 = list(movies.aggregate(pipeline2))
pprint.pprint(query2)

#######################

#explain feature examples
explain_query = db.command('aggregate' , 'movieData' , pipeline = pipeline , explain = True)
pprint.pprint(explain_query)


explain_query2 = movies.find({"name" : "Last Resort"} , {"name" : 1 , "rating" : 1}).explain()['executionStats']
pprint.pprint(explain_query2)
