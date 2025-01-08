class TaskModel:
    """
    タスクデータモデル
    """

    def __init__(self, name: str, completed: bool = False):
        """
        タスクを初期化します。

        Args:
            name (str): タスク名
            completed (bool, optional): タスクの完了状態。デフォルトは False。
        """
        self.name = name
        self.completed = completed

    def toggle_completed(self) -> None:
        """
        タスクの完了状態を切り替えます。
        """
        self.completed = not self.completed

    def update_name(self, new_name: str) -> None:
        """
        タスク名を更新します。

        Args:
            new_name (str): 新しいタスク名
        """
        self.name = new_name
