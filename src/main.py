import flet as ft

from controllers.controller import TodoController


def main(page: ft.Page) -> None:
    """
    アプリケーションのエントリポイント。
    """
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    # TodoControllerの初期化とページへの追加
    todo_app = TodoController()
    page.add(todo_app.view)  # アプリのビューをページに追加


ft.app(main)
