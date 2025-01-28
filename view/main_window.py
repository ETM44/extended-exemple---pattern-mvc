from PyQt5.QtWidgets import ( QMainWindow, QToolBar, QAction, QStackedWidget )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task and User Manager")
        self.setGeometry(100, 100, 500, 400)

        # Barre de Navigation
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        self.btn_tasks = QAction("Tâches", self)
        self.btn_users = QAction("Users", self)

        self.toolbar.addAction(self.btn_tasks)
        self.toolbar.addAction(self.btn_users)

        # Gestionnaire de pages (QStackedWidget)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)