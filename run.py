import os
from flask import Flask

# we'll initialize our new Flask application: app = Flask(__name__)
app = Flask(__name__)

#we then initialise our app route decorator which will be our index page, then we add a function which will be bound to our decorator
@app.route('/')
def index():
    return "<h1>Hello there!</h1>"
    

# then beneath this we put app.run - this is similar to what we've done before but this time we pass it all in the bracketso that it's a shorter version
# we use os.getenv('IP') to get the IP address then we add the PORT one. This is an environment variable set by Cloud9,
# and also one that we set for ourselves in Heroku you'll remember. After this, we just need to set the names: host and port.
# then we set debug to true
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

#remember to install flask - sudo pip3 install flask
# before we commit, we want to create our requirements.txt file - we do this entering pip3 freeze --local > requirements.txt into the terminal




