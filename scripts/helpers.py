from scripts import models
import bcrypt


def credentials_valid(username, password, email):
    user = User.query.filter_by(username=username).first()
    if user:
        return bcrypt.checkpw(password.encode('utf8'), user.password.encode('uft8'))
    return False


def add_user(username, password, email):
    new_user = User(username=username, email=email, password=password.decode('utf8'))
    db.session.add(new_user)
    db.session.commit()


def username_taken(username):
    with session_scope() as s:
        return User.query.filter_by(username=username).first()
