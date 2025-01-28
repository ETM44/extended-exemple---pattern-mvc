from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox
)

# UserView
class UserView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("Enter a user")
        self.add_button = QPushButton("Add User", self)
        self.user_list_widget = QListWidget(self)

        layout.addWidget(self.user_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.user_list_widget)

        self.setLayout(layout)

    def show_error(self, message: str):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()