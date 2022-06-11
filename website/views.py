from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Users, Games, Reviews
from . import db


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

@views.route('/reviews', methods=['GET', 'POST'])
@login_required
def reviews():
    if request.method == "POST":
        review = request.form.get('reviewtext')
        game = request.form.get('gamechoice')
        score = request.form.get('score')

        if len(review) < 1:
            flash('Review is too short!', category="error")
        else:
            new_review = Reviews(data=review, user_id=current_user.id)
            db.session.add(new_review)
            db.session.commit()
            flash('Review posted!', category="success")

    return render_template('reviews.html', user=current_user)