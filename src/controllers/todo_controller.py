import flet as ft

from models.task_model import TaskModel
from views.task_view import TaskView
from views.todo_view import TodoView


class TodoController:
    """
    タスク管理のコントローラー
    """

    def __init__(self) -> None:
        """
        コントローラーの初期化処理。
        """
        self.tasks: list[TaskModel] = []  # 全タスクのリスト
        self.view = TodoView(self.add_task, self.clear_completed, self.filter_tasks)
        self.filter_type = "all"  # 現在選択されているフィルター

    def add_task(self, e: ft.ControlEvent) -> None:
        """
        新しいタスクを追加します。

        Args:
            e (ft.ControlEvent): イベントオブジェクト
        """
        task_name = self.view.get_new_task_name()
        if task_name:
            new_task = TaskModel(task_name)
            self.tasks.append(new_task)  # タスクリストに追加
            self.update_view()

    def update_task_status(self, task: TaskModel, completed: bool) -> None:
        """
        タスクの完了状態を更新します。

        Args:
            task (TaskModel): 更新対象のタスク
            completed (bool): 完了状態
        """
        task.completed = completed
        self.update_view()

    def delete_task(self, task: TaskModel) -> None:
        """
        指定されたタスクを削除します。

        Args:
            task (TaskModel): 削除対象のタスク
        """
        self.tasks.remove(task)
        self.update_view()

    def edit_task(self, task: TaskModel, new_name: str) -> None:
        """
        タスク名を編集します。

        Args:
            task (TaskModel): 編集対象のタスク
            new_name (str): 新しいタスク名
        """
        task.update_name(new_name)
        self.update_view()

    def clear_completed(self, e: ft.ControlEvent) -> None:
        """
        完了済みのタスクをすべて削除します。

        Args:
            e (ft.ControlEvent): イベントオブジェクト
        """
        self.tasks = [task for task in self.tasks if not task.completed]
        self.update_view()

    def filter_tasks(self, e: ft.ControlEvent) -> None:
        """
        タスクをフィルタリングします。

        Args:
            e (ft.ControlEvent): イベントオブジェクト
        """
        self.filter_type = self.view.get_selected_filter()
        self.update_view()

    def get_filtered_tasks(self) -> list[TaskModel]:
        """
        現在のフィルター設定に基づき、タスクを取得します。

        Returns:
            list[TaskModel]: フィルタリングされたタスクリスト
        """
        if self.filter_type == "active":
            return [task for task in self.tasks if not task.completed]
        if self.filter_type == "completed":
            return [task for task in self.tasks if task.completed]
        return self.tasks

    def update_view(self) -> None:
        """
        ビューを更新します。
        """
        filtered_tasks = self.get_filtered_tasks()
        self.view.update_task_list(
            [
                TaskView(
                    task_name=task.name,
                    completed=task.completed,
                    on_status_change=lambda completed, t=task: self.update_task_status(t, completed),
                    on_delete=lambda t=task: self.delete_task(t),
                    on_edit=lambda new_name, t=task: self.edit_task(t, new_name),
                )
                for task in filtered_tasks
            ],
        )
        # 未完了のタスク数をビューに表示
        self.view.update_items_left(len([task for task in self.tasks if not task.completed]))
