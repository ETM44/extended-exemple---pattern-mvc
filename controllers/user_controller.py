from PyQt5.QtWidgets import QListWidgetItem
from models.user_model import UserModel
from views.user_view import UserView


class UserController:
    def __init__(self):
        self.model = UserModel()
        self.view = UserView()

        self.view.add_button.clicked.connect(self.add_user)
        self.view.user_list_widget.itemDoubleClicked.connect(self.remove_user)

    def add_user(self):
        user = self.view.user_input.text().strip()
        if user:
            self.model.create(user)
            self.update_user_list()
            self.view.user_input.clear()
        else:
            self.view.show_error("User cannot be empty.")

    def remove_user(self, item: QListWidgetItem):
        index = self.view.user_list_widget.row(item)
        self.model.delete(index)
        self.update_user_list()

    def update_user_list(self):
        self.view.user_list_widget.clear()
        for user in self.model.reads():
            self.view.user_list_widget.addItem(user)