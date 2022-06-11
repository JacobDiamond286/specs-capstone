from website.models import Users, Games, Reviews
from website import db
from werkzeug.security import generate_password_hash, check_password_hash
from random import choice
# from flask_login import UserMixin

games=["Elden Ring", "Dark Souls", "Team Fortress 2", "Counter Strike Global Offensive", "Terraria", "Rocket League", "Stardew Valley", "Red Dead Redemption", "Left 4 Dead 2", "Among Us"]
prices=[10, 20, 30, 40, 50, 60]
for title in games:
    add_game = Games(title=title, price=choice(prices))
    db.session.add(add_game)
    db.session.commit()

