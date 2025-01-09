# TaskModel
class TaskModel:
    def __init__(self):
        self.task_list = []

    def create(self, task: str):
        self.task_list.append(task)

    def delete(self, index: int):
        if 0 <= index < len(self.task_list):
            self.task_list.pop(index)

    def reads(self):
        return self.task_list