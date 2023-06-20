from flask import Flask

# Import the handlers defined in the Blueprint for myapp1_handlers
from myapp1 import myapp1_handlers 

app = Flask(__name__)

# Register your blueprint so that any route matching 
# what you've defined in the blueprint will get routed to it
app.register_blueprint(myapp1_handlers)


@app.route("/") 
def home():
    return "Main App - This is home page"


@app.route("/1/") 
def home_1():
    return "Main App - This is page 1"
