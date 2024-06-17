from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15))
    identity = db.Column(db.String(255))
    user = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)
    request = db.Column(db.String(255))
    status = db.Column(db.Integer)
    size = db.Column(db.Integer)
