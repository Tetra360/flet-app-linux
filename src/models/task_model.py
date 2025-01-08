class TaskModel:
    """
    タスクのデータモデル。
    """

    def __init__(self, name: str, completed: bool = False) -> None:
        self.name: str = name
        self.completed: bool = completed
