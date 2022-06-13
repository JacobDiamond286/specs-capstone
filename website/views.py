from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Users, Games, Reviews
from . import db
from sqlalchemy.orm import relationship



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

@views.route('/games/<game_id>')
@login_required
def game_reviews(game_id):
    game_title=Games.query.filter_by(id=game_id).first().title
    
    # username_table=db.session.query(Reviews).outerjoin(Users, Reviews.user_id==Users.id)

    # username_table=db.session.query(Users).join(Reviews, Users.id==Reviews.user_id).all()
    # # test = db.session.execute(username_table)
    # games_table=db.session.query(Games).join(username_table, Games.id==username_table.id)

    Reviews.query.filter_by(game_id=game_id).all()

    username_table=Users.query.join(Reviews)

    games_table=Games.query.join(Reviews)
    combined=username_table.join(games_table)

    # combined_table = db.session.query(Reviews, Users, Games).filter(Reviews.game_id == game_id).outerjoin(Games, Games.id == Reviews.id).all()
    # games=Reviews.query.filter_by(game_id=game_id).all()
    # print(test)
    print(username_table)

    for record in combined:
        print(record.id)
    

    return render_template('gamereviews.html', user=current_user, username_table=username_table, games=Reviews.query.filter_by(game_id=game_id).all(), current_title=game_title)