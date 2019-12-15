# after flask is set up and app is connected to heroku, install pip3 install flask-pymongo this will get flask communicating with pymongo 
# Then install dnspython " pip3 install dnspython" this is so you can use new styling connection string for mongodbs

import os
#this creates an instance of flask 
# flask is aframe work that contains these functions such as render_template ect
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId # mongodb stores its data in a json like format. 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task-manager' # put name of database. 
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

#something to bare in ind with the connection string, you need to replace the "<password>" with your user PW and "test" with database name. 
#also it would be better pracrtise to creat this project in a an environment variable to pretect passwords 
mongo = PyMongo(app) # create instance of pymongo 


@app.route('/')
#routing is a string that when we attach to a url will redirect to a particular function in our flask app
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.Tasks.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)