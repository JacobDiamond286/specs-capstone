from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/games')
def games_to_play():
    return render_template('gamestoplay.html')

@views.route('/friends')
def friends_games():
    return render_template('friendsgames.html')

@views.route('/howitworks')
def how_it_works():
    return render_template('howitworks.html')