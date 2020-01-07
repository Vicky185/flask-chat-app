# Flask Chat App

This is a chat application written in Flask. The purpose of this project is to take data from a URL and store the information in a list. 


Web Session - is a way we can store data for a short period of time in our application. This is initiated by the server and when it has been opened, we're given a unique and speicfic session ID. Generally, we don't see the session ID because it's contained in the headers that are sent from the server.
When we have this unique ID, we can use it to store variables. Sometimes data can be stored in a temporary area on the server or on our computer. We store it on this app in a cookie. 
A Cookie - is a small piece of data that's stored in our computer by a web browser. Because they're small they're only limited to file KB in size but they're useful for storing things, like what we have in our shopping cart on a website, or what account we're logged in with. They can be stored as text files, but we use a session cookie here, which will be deleted when we close the browser.
We use Flask to create the cookie which will store our username so that when we visit the website it will redirect us to our personal homepage. 



# flask-chat-app


