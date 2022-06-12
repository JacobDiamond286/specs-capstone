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

@views.route('/games', methods=['GET', 'POST'])
@login_required
def games_to_play():
        return render_template('gamestoplay.html', user=current_user, games=Games.query.all())

@views.route('/myreviews', methods=['GET', 'POST'])
@login_required
def myreviews():
    if request.method == "POST":
        review = request.form.get('reviewtext')
        game = request.form.get('gamechoice')
        score = request.form.get('score')

        if len(review) < 1:
            flash('Review is too short!', category="error")
        else:
            new_review = Reviews(text=review, user_id=current_user.id, score=score, game_id=game)
            db.session.add(new_review)
            db.session.commit()
            flash('Review posted!', category="success")

    return render_template('myreviews.html', user=current_user, game=Games.query.all())

@views.route('/reviews/Elden%20Ring')
@login_required
def er():
    return render_template('er.html', user=current_user, games=Games.query.all())