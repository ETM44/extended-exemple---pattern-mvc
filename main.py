from PyQt5.QtWidgets import (
    QApplication
)
import sys

from controllers.main_controller import MainController

# Main application
def main():
    app = QApplication(sys.argv)
    controller = MainController()
    controller.start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()