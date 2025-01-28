from PyQt5.QtWidgets import QListWidgetItem

from model.task_model import TaskModel
from view.task_view import TaskView

# TaskController
class TaskController:
    def __init__(self):
        self.model = TaskModel()
        self.view = TaskView()

        self.view.add_button.clicked.connect(self.add_task)
        self.view.task_list_widget.itemDoubleClicked.connect(self.remove_task)

    def add_task(self):
        task = self.view.task_input.text().strip()
        if task:
            self.model.create(task)
            self.update_task_list()
            self.view.task_input.clear()
        else:
            self.view.show_error("Task cannot be empty.")

    def remove_task(self, item: QListWidgetItem):
        index = self.view.task_list_widget.row(item)
        self.model.delete(index)
        self.update_task_list()

    def update_task_list(self):
        self.view.task_list_widget.clear()
        for task in self.model.reads():
            self.view.task_list_widget.addItem(task)