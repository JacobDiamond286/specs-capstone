from website import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    steam_id = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(64), nullable=False)

class Reviews(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    like_dislike = db.Column(db.Boolean, nullable=False)

class Games(db.Model):

    __tablename__ = 'games'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)