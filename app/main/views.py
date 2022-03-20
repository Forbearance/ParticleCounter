# Imports from Flask
from flask import Blueprint, render_template, request
import json
#Imports from the app package
from app import db
from app.models import Data

main = Blueprint("main", __name__, template_folder="templates")

@main.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        save_data_to_db()
        return 'Received POST to /', 200

    return render_template("index.html")

@main.route('/<name>', methods = ['POST'])
def route_with_name(name):
    save_data_to_db()
    return 'Received POST to /%s' % name, 200

# 404 error handler
def page_not_found(e):
    return render_template("errors/404.html")

def save_data_to_db():
    jsonstring = json.dumps(request.json)
    data = Data(jsonstring)
    db.session.add(data)
    db.session.commit()
