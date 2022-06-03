from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


#Endpoints ===========================================================

@app.route('/')
def start_here():
    return render_template('homepage.html')

@app.route('/games')
def games_to_play():
    return render_template('gamestoplay.html')

@app.route('/friends')
def friends_games():
    return render_template('friendsgames.html')

@app.route('/howitworks')
def how_it_works():
    return render_template('howitworks.html')

#Model Definitions ===========================================================

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    steam_id = db.Column(db.String(100), nullable=False)
    friend_list=db.Column(db.Integer, db.ForeignKey('friends.id'), nullable=False)

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
    price = db.Column(db.Decimal, nullable=False)

class Friends(db.Model):

    __tablename__ = 'friends'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")


