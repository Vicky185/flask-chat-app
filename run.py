import os
from flask import Flask

# we'll initialize our new Flask application: app = Flask(__name__)
app = Flask(__name__)

#we then initialise our app route decorator which will be our index page, then we add a function which will be bound to our decorator
#here wer're going to add instructions on how to use our app
#we say /username/message because in the web link we want this to display e.g. /victoria/hi there
@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"

#note username in brackets is treated as a variable
@app.route('/<username>')
def user(username):
    return "Hi " + username
  
# here we create a function for the message
# we call the function send_message an this takes two arguments
# we use a format method to format what we're returning, a return a string, the first part will be username and then we display our message
@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)

    

# then beneath this we put app.run - this is similar to what we've done before but this time we pass it all in the bracketso that it's a shorter version
# we use os.getenv('IP') to get the IP address then we add the PORT one. This is an environment variable set by Cloud9,
# and also one that we set for ourselves in Heroku you'll remember. After this, we just need to set the names: host and port.
# then we set debug to true
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

#remember to install flask - sudo pip3 install flask
# before we commit, we want to create our requirements.txt file - we do this entering pip3 freeze --local > requirements.txt into the terminal




