class Analysis:
    def __init__(self, title, details, user_id=0, id=0):
        self.id = id
        self.title = title
        self.details = details
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_details(self):
        return self.details

    def set_id(self, id):
        self.id = id

    def set_title(self, title):
        self.title = title

    def set_details(self, details):
        self.details = details

    def set_user_id(self, user_id):
        self.user_id = user_id
