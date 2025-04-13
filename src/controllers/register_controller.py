from models.ports.user_repository import UserRepository
from models.user.user import User


class RegisterController:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, username, password):
        self.user_repository.register(User(username, password))
