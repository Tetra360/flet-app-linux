from collections.abc import Callable

import flet as ft


class TaskView(ft.Column):
    """
    タスクのUIコンポーネント。
    """

    def __init__(
        self,
        task_name: str,
        on_status_change: Callable[[bool], None],
        on_delete: Callable[[], None],
        on_edit: Callable[[str], None],
    ) -> None:
        super().__init__()
        self.task_name: str = task_name
        self.on_status_change: Callable[[bool], None] = on_status_change
        self.on_delete: Callable[[], None] = on_delete
        self.on_edit: Callable[[str], None] = on_edit

        self.checkbox: ft.Checkbox = ft.Checkbox(
            value=False,
            label=self.task_name,
            on_change=self.status_changed,
        )
        self.edit_name: ft.TextField = ft.TextField(expand=1)

        self.display_view: ft.Row = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.checkbox,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view: ft.Row = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )

        self.controls: list[ft.Control] = [self.display_view, self.edit_view]

    def edit_clicked(self, e: ft.ControlEvent) -> None:
        self.edit_name.value = self.checkbox.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e: ft.ControlEvent) -> None:
        if self.edit_name.value:
            self.on_edit(self.edit_name.value)
            self.checkbox.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e: ft.ControlEvent) -> None:
        self.on_status_change(self.checkbox.value or False)

    def delete_clicked(self, e: ft.ControlEvent) -> None:
        self.on_delete()
