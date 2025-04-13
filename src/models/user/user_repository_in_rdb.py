from models.ports.user_repository import UserRepository
from mysql.connector import MySQLConnection
from models.user.user import User
from hashlib import sha512


class UserRepositoryInRDB(UserRepository):
    def __init__(self, connection: MySQLConnection):
        self.connection = connection
        self.cursor = connection.cursor()

    def get_user_by_id(self, id: int):
        self.cursor.execute("SELECT * FROM user WHERE id=%s", (id,))
        user = self.cursor.fetchone()
        return user

    def get_user_by_password(self, username: str, password: str):
        self.cursor.execute(
            "SELECT * FROM user WHERE username=%s AND password=%s",
            (username, sha512(password.encode("utf-8")).hexdigest()),
        )
        result = self.cursor.fetchone()
        return User(id=result[0], username=result[1])

    def register(self, user: User):
        SQL = "INSERT INTO user (username, password) VALUES (%s, %s)"
        self.cursor.execute(
            SQL,
            (user.username, sha512(user.password.encode("utf-8")).hexdigest()),
        )
        self.connection.commit()
