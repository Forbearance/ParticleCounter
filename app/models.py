# Imports from the app package
from app import db

# Data SQLAlchemy model
class Data(db.Model):
    __tablename__ = "tblMessageImport"
    __table_args__ = {'implicit_returning':False}

    id = db.Column(db.Integer(), primary_key=True)
    payload = db.Column(db.String(2048), nullable=True)

    def __init__(self, payload):
        self.payload = payload

    def __repr__(self):
        return 'Data("' + self.payload + '")'
