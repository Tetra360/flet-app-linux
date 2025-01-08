from collections.abc import Callable

import flet as ft


class TodoView(ft.Column):
    """
    タスクリスト全体を表示するビュー
    """

    def __init__(
        self,
        add_task: Callable[[ft.ControlEvent], None],
        clear_completed: Callable[[ft.ControlEvent], None],
        filter_tasks: Callable[[ft.ControlEvent], None],
    ) -> None:
        """
        TodoViewの初期化

        Args:
            add_task (Callable[[ft.ControlEvent], None]): タスク追加時のコールバック
            clear_completed (Callable[[ft.ControlEvent], None]): 完了タスク削除時のコールバック
            filter_tasks (Callable[[ft.ControlEvent], None]): フィルター変更時のコールバック
        """
        super().__init__()

        # 初期スタイルの設定 (ここで色やサイズを指定)
        self.clear_completed_button = ft.OutlinedButton(
            "Clear completed",
            on_click=clear_completed,
            style=ft.ButtonStyle(color="#a0cafd"),  # 初期スタイルを設定
            width=150,
        )

        self.new_task_input = ft.TextField(
            hint_text="What needs to be done?",
            on_submit=add_task,
        )
        self.task_list = ft.Column()  # タスク一覧
        self.filter_tabs = ft.Tabs(
            tabs=[
                ft.Tab(text="all"),
                ft.Tab(text="active"),
                ft.Tab(text="completed"),
            ],
            on_change=filter_tasks,
        )
        self.items_left = ft.Text("0 items left")  # 未完了タスク数表示

        self.controls = [
            ft.Row([ft.Text(value="Todos", style="headlineMedium")]),
            ft.Row([self.new_task_input, ft.IconButton(icon=ft.Icons.ADD, on_click=add_task)]),
            self.filter_tabs,
            self.task_list,
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.items_left,
                    self.clear_completed_button,  # ボタンの参照を保持
                ],
            ),
        ]

    def get_new_task_name(self) -> str:
        """
        新しいタスク名を取得して入力欄をクリアします。

        Returns:
            str: 入力されたタスク名
        """
        task_name = self.new_task_input.value.strip()
        self.new_task_input.value = ""
        return task_name

    def get_selected_filter(self) -> str:
        """
        現在選択されているフィルターを取得します。

        Returns:
            str: 選択されているフィルター名
        """
        return self.filter_tabs.tabs[self.filter_tabs.selected_index].text

    def update_task_list(self, task_views: list[ft.Control]) -> None:
        """
        タスクリストを更新します。

        Args:
            task_views (list[ft.Control]): 更新後のタスクビューリスト
        """
        self.task_list.controls = task_views
        self.update()

    def update_items_left(self, count: int) -> None:
        """
        未完了タスク数を更新します。

        Args:
            count (int): 未完了タスク数
        """
        self.items_left.value = f"{count} items left"
        self.update()

    def set_clear_completed_button_color(self, current_filter: str) -> None:
        """
        Clear completedボタンの色を更新します。

        Args:
            current_filter (str): 現在選択されているフィルター
        """
        # デフォルトは基本カラーに設定
        color = "#a0cafd"

        # "completed"タブの時だけオレンジ色に設定
        if current_filter == "completed":
            color = ft.colors.ORANGE

        # ボタンスタイルの更新
        self.clear_completed_button.style = ft.ButtonStyle(color=color)
        self.update()  # 再描画を呼び出し
