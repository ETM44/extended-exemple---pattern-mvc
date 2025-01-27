from PyQt5.QtWidgets import QListWidgetItem

from model.task_model import TaskModel
from model.user_model import UserModel
from view.task_view import TaskView

# TaskController
class TaskController:
    def __init__(self):
        self.task_model = TaskModel()
        self.user_model = UserModel()
        self.view = TaskView()
        
        self.view.show()

        # Connecter les signaux de la vue aux méthodes du contrôleur
        self.view.task_add_button.clicked.connect(self.add_task)
        self.view.task_list_widget.itemDoubleClicked.connect(self.remove_task)
        self.view.user_add_button.clicked.connect(self.add_user)
        self.view.user_list_widget.itemDoubleClicked.connect(self.remove_user)

    def add_task(self):
        task = self.view.task_input.text().strip()
        if task:
            self.task_model.create(task)
            self.update_task_list()
            self.view.task_input.clear()
        else:
            self.view.show_error("Task cannot be empty.")

    def remove_task(self, item: QListWidgetItem):
        index = self.view.task_list_widget.row(item)
        self.task_model.delete(index)
        self.update_task_list()

    def update_task_list(self):
        tasks = self.task_model.reads()
        self.view.task_list_widget.clear()
        for task in tasks:
            self.view.task_list_widget.addItem(task)

    def add_user(self):
        user = self.view.user_input.text().strip()
        if user:
            self.user_model.create(user)
            self.update_user_list()
            self.view.user_input.clear()
        else:
            self.view.show_error("User cannot be empty.")

    def remove_user(self, item: QListWidgetItem):
        index = self.view.user_list_widget.row(item)
        self.user_model.delete(index)
        self.update_user_list()

    def update_user_list(self):
        users = self.user_model.reads()
        self.view.user_list_widget.clear()
        for user in users:
            self.view.user_list_widget.addItem(user)