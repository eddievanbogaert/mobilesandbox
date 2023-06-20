from flask import Blueprint
myapp1_handlers = Blueprint('myapp1_handlers', __name__, 
template_folder='templates')


@myapp1_handlers.route("/myapp1/") 
def home():
    return "myapp1 - This is home page"

@admin_handlers.route("/admin/1/") 
def home_1():
    return "myapp1 - This is page 1"
