import flet as ft

from models.task_model import TaskModel
from views.task_view import TaskView
from views.todo_view import TodoView


class TodoController:
    """
    タスク管理のコントローラー。
    """

    def __init__(self) -> None:
        self.tasks: list[TaskModel] = []
        self.view: TodoView = TodoView(self.add_task, self.clear_completed, self.filter_tasks)

    def add_task(self, e: ft.ControlEvent) -> None:
        """
        新しいタスクを追加します。

        Args:
            e (ft.ControlEvent): イベントオブジェクト。
        """
        task_name: str = self.view.new_task_input.value
        if task_name:
            task_model = TaskModel(task_name)
            self.tasks.append(task_model)

            task_view = TaskView(
                task_name=task_model.name,
                on_status_change=lambda completed: self.update_task_status(task_model, completed),
                on_delete=lambda: self.delete_task(task_model),
                on_edit=lambda new_name: self.edit_task(task_model, new_name),
            )
            self.view.task_list.controls.append(task_view)
            self.view.new_task_input.value = ""
            self.view.update()

    def update_task_status(self, task_model: TaskModel, completed: bool) -> None:
        """
        タスクのステータスを更新します。

        Args:
            task_model (TaskModel): 対象タスク。
            completed (bool): タスクが完了しているか。
        """
        task_model.completed = completed
        self.view.update()

    def delete_task(self, task_model: TaskModel) -> None:
        """
        タスクを削除します。

        Args:
            task_model (TaskModel): 削除対象のタスク。
        """
        self.tasks.remove(task_model)
        self.view.task_list.controls = [
            task
            for task in self.view.task_list.controls
            if isinstance(task, TaskView) and task.task_name != task_model.name
        ]
        self.view.update()

    def edit_task(self, task_model: TaskModel, new_name: str) -> None:
        """
        タスクの名前を編集します。

        Args:
            task_model (TaskModel): 編集対象のタスク。
            new_name (str): 新しい名前。
        """
        task_model.name = new_name
        self.view.update()

    def clear_completed(self, e: ft.ControlEvent) -> None:
        """
        完了したタスクを削除します。

        Args:
            e (ft.ControlEvent): イベントオブジェクト。
        """
        self.tasks = [task for task in self.tasks if not task.completed]
        self.view.task_list.controls = [
            task_view
            for task_view in self.view.task_list.controls
            if isinstance(task_view, TaskView) and not task_view.checkbox.value
        ]
        self.view.update()

    def filter_tasks(self, e: ft.ControlEvent) -> None:
        """
        タスクをフィルタリングします。

        Args:
            e (ft.ControlEvent): イベントオブジェクト。
        """
        selected_filter: str = self.view.filter_tabs.tabs[self.view.filter_tabs.selected_index].text
        for task_view in self.view.task_list.controls:
            if isinstance(task_view, TaskView):
                task_view.visible = (
                    selected_filter == "all"
                    or (selected_filter == "active" and not task_view.checkbox.value)
                    or (selected_filter == "completed" and task_view.checkbox.value)
                )
        self.view.update()
