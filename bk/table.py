import flet as ft  # type: ignore
import pandas as pd


class CustomTable:
    def __init__(self) -> None:
        self.table_width = 1000
        self.cell_height = 28
        self.split_line = 1
        self.scroll_list_padding_LR = 20
        self.table_header_color = "blue"
        self.table_data_color = "white"
        self.table_text_color = "black"
        self.split_line_color = "#D3D3D3"

    def table_header(self) -> ft.Container:
        # CSVファイルからヘッダーを取得
        header_rows = list(TableSetup.get_data_frame().columns)
        cell_width = TableSetup.calculate_cell_width(self.table_width, self.split_line, self.scroll_list_padding_LR)

        return ft.Container(
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        control
                        for index, cell in enumerate(header_rows)
                        for control in [
                            # 各セルのコンテナ
                            ft.Container(
                                content=ft.Text(
                                    str(cell),
                                    size=14,
                                    weight=ft.FontWeight.BOLD,
                                    no_wrap=True,  # テキストを折り返さない
                                ),
                                alignment=ft.alignment.center,
                                width=cell_width,
                                height=self.cell_height,
                            ),
                            # 仕切り線
                            ft.Container(
                                width=self.split_line,
                                height=self.cell_height,
                                bgcolor=self.split_line_color,
                            )
                            if index < len(header_rows) - 1
                            else None,
                        ]
                        if control is not None
                    ],
                    alignment="start",
                ),
                padding=ft.Padding(top=11, right=0, bottom=3, left=self.scroll_list_padding_LR),
            ),
            bgcolor=self.table_header_color,
        )

    def scroll_list(self) -> ft.Container:
        # データ部分を取得
        header_rows = list(TableSetup.get_data_frame().columns)
        data_rows = TableSetup.get_data_frame().to_numpy().tolist()
        cell_width = TableSetup.calculate_cell_width(self.table_width, self.split_line, self.scroll_list_padding_LR)
        row_padding = 8

        data_containers = []
        for row in data_rows:
            row_container = ft.Container(
                content=ft.Row(
                    controls=[
                        control
                        for index, cell in enumerate(row)
                        for control in [
                            # 各セルの入力ボックスコンテナ
                            ft.Container(
                                content=ft.TextField(
                                    value=str(cell),  # 初期値としてセルの値を設定
                                    text_size=14,
                                    color=self.table_text_color,
                                    width=cell_width,
                                    height=self.cell_height,
                                    border_color=self.table_data_color,
                                    text_align="center",  # テキストを中央揃え
                                ),
                                padding=ft.Padding(
                                    top=0,
                                    right=0,
                                    bottom=10,
                                    left=0,
                                ),
                                alignment=ft.alignment.center,
                                width=cell_width,
                                height=self.cell_height,
                            ),
                            # 仕切り線
                            ft.Container(
                                width=self.split_line,
                                height=self.cell_height,
                                bgcolor=self.split_line_color,
                            )
                            if index < len(header_rows) - 1
                            else None,
                        ]
                        if control is not None
                    ],
                    alignment="start",
                ),
                padding=ft.Padding(
                    top=row_padding,
                    right=0,
                    bottom=row_padding,
                    left=0,
                ),
                border=ft.Border(bottom=ft.border.BorderSide(1.5, self.split_line_color)),
            )
            data_containers.append(row_container)

        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.ListView(
                        controls=data_containers,
                        height=300,
                        expand=True,
                        padding=ft.Padding(
                            top=0,
                            right=self.scroll_list_padding_LR,
                            bottom=0,
                            left=self.scroll_list_padding_LR,
                        ),
                    ),
                ],
                alignment="center",
            ),
            bgcolor=self.table_data_color,
        )

    def create_scroll_table(self) -> ft.Container:
        table_header_container = self.table_header()
        table_data_container = self.scroll_list()

        return ft.Container(
            content=ft.Column(
                [
                    table_header_container,
                    table_data_container,
                ],
                alignment="center",
                horizontal_alignment="center",
            ),
            width=self.table_width,
            alignment=ft.alignment.center,
            bgcolor=self.table_header_color,
            border_radius=10,
            margin=ft.Margin(top=0, right=40, bottom=0, left=40),
        )


class TableSetup:
    csv_file = "src/models/sample.csv"  # クラス変数として定義

    @classmethod
    def get_data_frame(cls) -> pd.DataFrame:
        return pd.read_csv(cls.csv_file)

    @classmethod
    def get_column_count(cls) -> int:
        data_frame = cls.get_data_frame()
        return data_frame.shape[1]

    @staticmethod
    def calculate_cell_width(table_width: int, split_line: int, scroll_list_padding_LR: int) -> int:
        column_count = TableSetup.get_column_count()
        offset = scroll_list_padding_LR * 2
        return (table_width - offset - ((10 * 2 + split_line) * (column_count - 1))) // column_count
