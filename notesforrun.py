import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

#to create our session cookie, we add 'request' and 'session' modules from our flask library
#to generate our session ID, we need to give our app a secret key, generally in production we set it as an environment variable like we did our IP address import

# we'll initialize our new Flask application: app = Flask(__name__)
app = Flask(__name__)
app.secret_key = "randomstring123"
# now we create an empty list under where we define our Flask app, we put messages = [] which is an empty list
messages = []

#we create a function called add_messages(), which will take our username and message and append it to the list
# the function takes two arguments, we call the append() method on our messages list so we'll append a string
# we use the format method again and the two sets of {}, this time we don't use 0 and 1 as we do below, these are positional indicators (in the curly brackets) the reason is that since python 2.7 it has been option to supply the positional indicators
# if we leave out the positional indicators, the first set auto refers to first argument and second to second etc
#here we're going to use a timestamp, datetime is built into python's standard library
# we create variable 'now', then call datetime, then the strftime()method which takes a date time object and converts this to a string according to a given format. so we need to provide a format.
#we use the now() method as well to get the current time
#at the oment all of our chat info is stored in a list which is fine but doesn't allow us to access certain parts by name. we can't specify which parts of the data we want to access. 
# inside our add_messages() function, we're going to create a dictionary to store our message info, we will create a new variable call messages_dict
# inside the variable we're going to store all of our data as key value pairs, the first key is going to be timestamp and the value will be that of the 'now' variable we created etc.
def add_messages(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}
    #we then amend the below so we'll end up in a list of dictionary items
    messages.append(messages_dict)

#after creating our messages dict we can remove our get_all_messages() function because we don't need it anymore.
# now we create a function which displays the messages for us
#def get_all_messages():
#    """Get all of the messages and separate them with a `br` break tag"""
#    return "<br>".join(messages)

#we then initialise our app route decorator which will be our index page, then we add a function which will be bound to our decorator
#here wer're going to add instructions on how to use our app
#we say /username/message because in the web link we want this to display e.g. /victoria/hi there
#as this is our index, we will now render the index template - so we remove return To send a message use /USERNAME/MESSAGE" and add return render_...etc
@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    #to get our form working we need the GET and request methods to our index route
    if request.method == "POST":
       session["username"] = request.form["username"]
    # we add an if statement then we create a new variable in our session called username. so we create our session username variable ( session["username"])
    # and we want that to be equal to request.form["username"], so the username that we typed and posted from our form
    # now that our username is set, we need to check to see that it's there so that if the username exists we redirect to our personal chat page. so we say if the username in the session, then instead of returning our index.html, we're going to redirect to the contents of the session username variable.
    if "username" in session:
        return redirect(session["username"])
    return render_template("index.html")

#note username in brackets is treated as a variable
@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, messages)
  
# here we create a function for the message
# we call the function send_message an this takes two arguments
# we use a format method to format what we're returning, a return a string, the first part will be username and then we display our message
@app.route("/<username>/<message>")
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




