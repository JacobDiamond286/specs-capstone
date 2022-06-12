from website.models import Users, Games, Reviews
from website import db
from werkzeug.security import generate_password_hash, check_password_hash
from random import choice
from flask_login import UserMixin

games=["Elden Ring", "Dark Souls", "Team Fortress 2", "Counter Strike Global Offensive", "Terraria", "Rocket League", "Stardew Valley", "Red Dead Redemption", "Left 4 Dead 2", "Among Us"]
prices=[10, 20, 30, 40, 50, 60]
for title in games:
    add_game = Games(title=title, price=choice(prices))
    db.session.add(add_game)
    db.session.commit()

for i in range(10):
    new_email=str(f"user{i+2}@email.com")
    username = f"user{i+2}"
    steam_id = f"steam_id{i+2}"
    password = f"userspassword{i+2}"
    add_user = Users(id=i+2, email=new_email, username=username, steam_id=steam_id, password=password)
    db.session.add(add_user)
    db.session.commit()

minecraft = Games(id=11, title="Minecraft", price=30)
db.session.add(minecraft)
db.session.commit()