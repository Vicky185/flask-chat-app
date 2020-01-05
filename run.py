import os
from flask import Flask, redirect

# we'll initialize our new Flask application: app = Flask(__name__)
app = Flask(__name__)

# now we create an empty list under where we define our Flask app, we put messages = [] which is an empty list
messages = []

#we create a function called add_messages(), which will take our username and message and append it to the list
# the function takes two arguments, we call the append() method on our messages list so we'll append a string
# we use the format method again and the two sets of {}, this time we don't use 0 and 1 as we do below, these are positional indicators (in the curly brackets) the reason is that since python 2.7 it has been option to supply the positional indicators
# if we leave out the positional indicators, the first set auto refers to first argument and second to second etc
def add_messages(username, message):
    """Add messages to the messages list"""
    messages.append("{}: {}".format(username, message))

# now we create a function which displays the messages for us
def get_all_messages():
    """Get all of the messages and separate them with a `br` break tag"""
    return "<br>".join(messages)

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
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())
  
# here we create a function for the message
# we call the function send_message an this takes two arguments
# we use a format method to format what we're returning, a return a string, the first part will be username and then we display our message
@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect to chat page"""
    #we use redirect to redirect us back to the decorator which is the user's personalised welcome page for this to work we need to import the redirect module from the flask library
    add_messages(username, message)
    return redirect("/" + username)

    

# then beneath this we put app.run - this is similar to what we've done before but this time we pass it all in the bracketso that it's a shorter version
# we use os.getenv('IP') to get the IP address then we add the PORT one. This is an environment variable set by Cloud9,
# and also one that we set for ourselves in Heroku you'll remember. After this, we just need to set the names: host and port.
# then we set debug to true
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

#remember to install flask - sudo pip3 install flask
# before we commit, we want to create our requirements.txt file - we do this entering pip3 freeze --local > requirements.txt into the terminal




