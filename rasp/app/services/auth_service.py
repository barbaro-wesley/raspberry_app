from flask_jwt_extended import create_access_token
from app import bcrypt
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self):
        self.repository = UserRepository()

    def register(self, username: str, password: str):
        if not username or not password:
            raise ValueError("Usuário e senha são obrigatórios.")

        if len(password) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")

        if self.repository.username_exists(username):
            raise ValueError(f"Usuário '{username}' já existe.")

        password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
        user = self.repository.create(username, password_hash)
        return {"id": user.id, "username": user.username}

    def get_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id)

    def login(self, username: str, password: str):
        user = self.repository.get_by_username(username)

        if user is None or not bcrypt.check_password_hash(user.password_hash, password):
            raise PermissionError("Credenciais inválidas.")

        token = create_access_token(identity=str(user.id))
        return {"access_token": token}