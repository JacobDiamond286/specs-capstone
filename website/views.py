from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def base():
    return render_template('landing.html', user=current_user)

@views.route('/home')
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/games')
def games_to_play():
    return render_template('gamestoplay.html')

@views.route('/reviews')
def reviews():
    return render_template('reviews.html')

@views.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')

@views.route('/howitworks')
def how_it_works():
    return render_template('howitworks.html')