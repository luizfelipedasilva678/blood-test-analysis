class User:
    def __init__(self, username: str, password="", id=0):
        self.id = id
        self.username = username
        self.password = password

    def get_id(self) -> int:
        return self.id

    def get_password(self) -> str:
        return self.password

    def get_username(self) -> str:
        return self.username

    def set_username(self, username) -> None:
        self.username = username

    def set_password(self, password) -> None:
        self.password = password

    def set_id(self, id) -> None:
        self.id = id
