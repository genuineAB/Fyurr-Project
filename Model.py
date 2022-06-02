
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ARRAY
db = SQLAlchemy()

def db_setup(app):
    db.app = app
    db.init_app(app)
    Migrate(app,db)


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    facebook_link = db.Column(db.String(120), nullable=False)
    webdsite_link = db.Column(db.String(120), nullable=False)
    seeking_talent = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.string(500), nullable = False)
    genres = db.Column(db.String(), nullable=False)
    shows = db.relationship('Show', backref='venue', lazy=False)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120),  nullable=False)
    phone = db.Column(db.String(120),  nullable=False)
    genres = db.Column(db.String(120),  nullable=False)
    image_link = db.Column(db.String(500),  nullable=False)
    facebook_link = db.Column(db.String(120),  nullable=False)
    seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500), nullable = False)
    shows = db.relationship('Show', backref='artist', lazy=False)


class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column(db.Integer, primiary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable = False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
