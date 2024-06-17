from app import app
from models import db, User

with app.app_context():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    user = User(username=username)
    user.set_password(password)
    
    db.session.add(user)
    db.session.commit()
    print(f"User {username} added successfully!")
