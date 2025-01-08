from collections.abc import Callable

import flet as ft


class TaskView(ft.Column):
    """
    個々のタスクを表示するビュー
    """

    def __init__(
        self,
        task_name: str,
        completed: bool,
        on_status_change: Callable[[bool], None],
        on_delete: Callable[[], None],
        on_edit: Callable[[str], None],
    ) -> None:
        """
        TaskViewの初期化

        Args:
            task_name (str): タスク名
            completed (bool): 完了状態
            on_status_change (Callable[[bool], None]): ステータス変更時のコールバック
            on_delete (Callable[[], None]): 削除時のコールバック
            on_edit (Callable[[str], None]): 編集時のコールバック
        """
        super().__init__()
        self.task_name = task_name
        self.on_status_change = on_status_change
        self.on_delete = on_delete
        self.on_edit = on_edit

        # チェックボックスの設定
        self.checkbox: ft.Checkbox = ft.Checkbox(
            value=completed,
            label=task_name,
            on_change=lambda e: self.on_status_change(self.checkbox.value),
        )

        # 編集用テキストフィールド
        self.edit_name: ft.TextField = ft.TextField(expand=1)

        # 表示モード
        self.display_view: ft.Row = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.checkbox,
                ft.Row(
                    controls=[
                        ft.IconButton(ft.Icons.CREATE_OUTLINED, on_click=self.edit_clicked),
                        ft.IconButton(ft.Icons.DELETE_OUTLINE, on_click=lambda e: self.on_delete()),
                    ],
                ),
            ],
        )

        # 編集モード
        self.edit_view: ft.Row = ft.Row(
            visible=False,
            controls=[
                self.edit_name,
                ft.IconButton(ft.Icons.DONE_OUTLINE, on_click=self.save_clicked),
            ],
        )

        # 表示と編集モードを切り替え
        self.controls: list[ft.Control] = [self.display_view, self.edit_view]

    def edit_clicked(self, e: ft.ControlEvent) -> None:
        """
        編集モードに切り替えます。
        """
        self.edit_name.value = self.checkbox.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e: ft.ControlEvent) -> None:
        """
        編集内容を保存して表示モードに戻ります。
        """
        if self.edit_name.value:
            self.on_edit(self.edit_name.value)
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()
