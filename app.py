from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json
import os

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

class Data(db.Model):
    __tablename__ = "tblMessageImport"
    __table_args__ = {'implicit_returning':False}

    id = db.Column(db.Integer(), primary_key=True)
    payload = db.Column(db.String(2048), nullable=True)

    def __init__(self, payload):
        self.payload = payload

    def __repr__(self):
        return 'Data("' + self.payload + '")'

db.init_app(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        save_data_to_db()
        return 'Received POST to /', 200

    return "<p>Particle Counter API GET</p>"

@app.route('/<name>', methods = ['POST'])
def route_with_name(name):
    save_data_to_db()
    return 'Received POST to /%s' % name, 200

def save_data_to_db():
    jsonstring = json.dumps(request.json)
    data = Data(jsonstring)
    db.session.add(data)
    db.session.commit()

if __name__ == "__main__":
    app.run()