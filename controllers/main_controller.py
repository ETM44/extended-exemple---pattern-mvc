from controllers.task_controller import TaskController
from controllers.user_controller import UserController
from views.main_window import MainWindow


class MainController:
    def __init__(self):
        self.main_window = MainWindow()

        # Instanciation des contrôleurs
        self.task_controller = TaskController()
        self.user_controller = UserController()

        # Ajout des vues au QStackedWidget
        self.main_window.stack.addWidget(self.task_controller.view)  # Index 0 : TaskView
        self.main_window.stack.addWidget(self.user_controller.view)  # Index 1 : UserView

        # Connexion des boutons
        self.main_window.btn_tasks.triggered.connect(self.showPageTasks)
        self.main_window.btn_users.triggered.connect(self.showPageUsers)

    def showPageTasks(self):
        """ Affiche la vue des tâches """
        self.main_window.stack.setCurrentIndex(0)

    def showPageUsers(self):
        """ Affiche la vue des utilisateurs """
        self.main_window.stack.setCurrentIndex(1)

    def start(self):
        """ Démarre l'application """
        self.main_window.show()