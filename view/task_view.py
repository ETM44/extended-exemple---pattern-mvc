from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox
)
import sys

# TaskView
class TaskView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task and User Manager")

        # Layout principal
        self.layout = QVBoxLayout()

        # Widgets pour les tâches
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a task")
        self.task_add_button = QPushButton("Add Task", self)
        self.task_list_widget = QListWidget(self)

        # Widgets pour les utilisateurs
        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("Enter a user")
        self.user_add_button = QPushButton("Add User", self)
        self.user_list_widget = QListWidget(self)

        # Ajouter les widgets au layout
        self.layout.addWidget(self.task_input)
        self.layout.addWidget(self.task_add_button)
        self.layout.addWidget(self.task_list_widget)
        self.layout.addWidget(self.user_input)
        self.layout.addWidget(self.user_add_button)
        self.layout.addWidget(self.user_list_widget)

        self.setLayout(self.layout)

    def show_error(self, message: str):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()