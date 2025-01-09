# UserModel
class UserModel:
    def __init__(self):
        self.user_list = []

    def create(self, user: str):
        self.user_list.append(user)

    def delete(self, index: int):
        if 0 <= index < len(self.user_list):
            self.user_list.pop(index)

    def reads(self):
        return self.user_list