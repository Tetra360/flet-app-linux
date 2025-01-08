from collections.abc import Callable

import flet as ft


class TodoView(ft.Column):
    """
    アプリケーション全体のビュー。
    """

    def __init__(
        self,
        add_task: Callable[[ft.ControlEvent], None],
        clear_completed: Callable[[ft.ControlEvent], None],
        filter_tasks: Callable[[ft.ControlEvent], None],
    ) -> None:
        super().__init__()
        self.new_task_input: ft.TextField = ft.TextField(
            hint_text="What needs to be done?",
            on_submit=add_task,
            expand=True,
        )
        self.task_list: ft.Column = ft.Column()
        self.filter_tabs: ft.Tabs = ft.Tabs(
            tabs=[
                ft.Tab(text="all"),
                ft.Tab(text="active"),
                ft.Tab(text="completed"),
            ],
            on_change=filter_tasks,
        )
        self.items_left: ft.Text = ft.Text("0 items left")

        self.controls: list[ft.Control] = [
            ft.Row([ft.Text(value="Todos", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)]),
            ft.Row(
                controls=[
                    self.new_task_input,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task),
                ],
            ),
            self.filter_tabs,
            self.task_list,
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.items_left,
                    ft.OutlinedButton(text="Clear completed", on_click=clear_completed),
                ],
            ),
        ]
