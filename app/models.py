from app import db


class WebColor(db.Model):
    __tablename__ = 'webcolor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    color = db.Column(db.String(8)) 
