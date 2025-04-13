from abc import ABC, abstractmethod
from models.user.user import User


class UserRepository(ABC):
    def __init__(self, db):
        self.db = db

    @abstractmethod
    def get_user_by_id(self, id: int):
        pass

    @abstractmethod
    def register(self, user: User):
        pass
