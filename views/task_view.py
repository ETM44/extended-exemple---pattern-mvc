from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox
)

# TaskView
class TaskView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a task")
        self.add_button = QPushButton("Add Task", self)
        self.task_list_widget = QListWidget(self)

        layout.addWidget(self.task_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.task_list_widget)

        self.setLayout(layout)

    def show_error(self, message: str):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()