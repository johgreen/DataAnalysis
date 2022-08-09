import pymongo
import pprint 

def server_connect(uri):
    '''
    Connect to a MongoDB server
    '''
    client = pymongo.MongoClient(uri, serverSelectionTimeoutMS = 2000)

    try:
        test_connection = client.server_info()
        return client
    except Exception:
        print("Connection Error")


connection = server_connect("mongodb://127.0.0.1:27017/") #create connection

#grab database and collection
db = connection.movieData 
movies = db.movies

#Get all movies with "Drama" and "Horror" genres 
genres_filter = list(db.movies.find({"genres" : {"$all" : ["Drama" , "Horror"]}}))
pprint.pprint(genres_filter)


#Only show docs with avg ratings between 9.0 and 9.5
ratings_filter = list(movies.find(
    {"$and" : [ 
        {"rating.average" : {
            "$gte" : 9.0} } , {
        "rating.average" : {
            "$lte" : 9.5
            }
        } 
            ]
        },
        {"_id" : 0 , "name" : 1 , "rating.average" : 1} 
    )
)
pprint.pprint(ratings_filter)


'''
Now let's take that same query a step further with an aggregation.
Show movies with ratings 9.0 to 9.5, then group and sort by runtimes.
'''

ratings_filter = list(movies.aggregate([
    {"$match" :                 #match works like find. Grabbing all docs with 
    {"$and" : [                 #ratings between 8.8 to 9.5
        {"rating.average" : {
            "$gte" : 8.8} } , {
                "rating.average" : {
                    "$lte" : 9.5
                }
            } 
        ]
    }
    },
    {"$group" :                 #group data by runtime and then count each group
            {"_id" : 
                {"runtime" : "$runtime"} , "movieSums" : {"$sum" : 1} 
            }
    } ,
      
    {"$sort" :                  #sort by the quantity of each group in desc order.
         {"movieSums" : -1}
        }
        ]
    )
)

pprint.pprint(ratings_filter)
