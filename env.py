import os 
os.environ["MONGO_URI"] = "mongodb+srv://admin:Password1@myfirstcluster-qjzok.mongodb.net/test?retryWrites=true&w=majority"

#'majority pymongo.errors.WriteConcernError: No write concern mode named 'majority  ' found in replica set configuration