from app import db
from app.models.user import User


class UserRepository:
    def get_by_username(self, username: str):
        return User.query.filter_by(username=username).first()

    def create(self, username: str, password_hash: str) -> User:
        user = User(username=username, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return user

    def username_exists(self, username: str) -> bool:
        return self.get_by_username(username) is not None