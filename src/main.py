import flet as ft

from controllers.todo_controller import TodoController


def main(page: ft.Page) -> None:
    """
    アプリケーションのエントリポイント
    """
    page.title = "ToDo App"
    page.scroll = ft.ScrollMode.ADAPTIVE

    # コントローラーを初期化してページに追加
    todo_app = TodoController()
    page.add(todo_app.view)


ft.app(target=main)
