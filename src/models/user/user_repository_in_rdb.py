from models.ports.user_repository import UserRepository
from mysql.connector import MySQLConnection
from models.user.user import User
from hashlib import sha512


class UserRepositoryInRDB(UserRepository):
    def __init__(self, connection: MySQLConnection):
        self.connection = connection
        self.cursor = connection.cursor()

    def get_user_by_password(self, user: User) -> User | None:
        SQL = "SELECT * FROM user WHERE username=%s AND password=%s"
        self.cursor.execute(
            SQL,
            (
                user.get_username(),
                sha512(user.get_password().encode("utf-8")).hexdigest(),
            ),
        )
        result = self.cursor.fetchone()

        if result is None:
            return None

        return User(id=result[0], username=result[1])

    def register(self, user: User) -> None:
        SQL = "INSERT INTO user (username, password) VALUES (%s, %s)"
        self.cursor.execute(
            SQL,
            (
                user.get_username(),
                sha512(user.get_password().encode("utf-8")).hexdigest(),
            ),
        )
        self.connection.commit()
