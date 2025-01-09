from PyQt5.QtWidgets import (
    QApplication
)
import sys

from controller.task_controller import TaskController
from view.task_view import TaskView

# Main application
def main():
    app = QApplication(sys.argv)
    view = TaskView()
    controller = TaskController(view)
    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()