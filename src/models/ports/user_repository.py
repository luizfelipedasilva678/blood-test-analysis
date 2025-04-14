from abc import ABC, abstractmethod
from models.user.user import User


class UserRepository(ABC):
    @abstractmethod
    def register(self, user: User) -> None:
        pass

    @abstractmethod
    def get_user_by_password(self, user: User) -> User | None:
        pass
