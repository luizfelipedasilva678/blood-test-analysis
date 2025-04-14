from models.ports.user_repository import UserRepository
from models.user.user import User


class LoginController:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, username, password) -> User | None:
        return self.user_repository.get_user_by_password(User(username, password))
