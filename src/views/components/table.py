import flet as ft  # type: ignore
import pandas as pd


def create_table():
    # CSVファイルの読み込み
    csv_file = "src/models/sample.csv"
    data_frame = pd.read_csv(csv_file)

    # ヘッダー行とデータ行に分割
    header_rows = list(data_frame.columns)
    data_rows = data_frame.iloc[:, :].values.tolist()

    first_row = data_rows[0]
    print(first_row)

    # テーブルのヘッダー部品のコンテナ
    table_header_container = ft.Row(
        controls=[
            ft.DataTable(
                columns=[ft.DataColumn(ft.Text(col)) for col in header_rows],  # header_rowsを利用
                heading_row_height=40,
                bgcolor="#808080",
            ),
        ],
        alignment="center",
    )

    # データ部分の行を作成
    table_data = [
        ft.DataRow(cells=[ft.DataCell(ft.Text(str(cell))) for cell in row])
        for row in data_rows  # リストから直接取得
    ]

    # データ部分のコンテナ
    table_data_container = ft.Row(
        controls=[
            ft.DataTable(
                columns=[ft.DataColumn(ft.Text(col)) for col in header_rows],
                rows=table_data,
            ),
        ],
        alignment="center",
    )

    # スクロール可能なテーブルのコンテナ
    table_container = ft.Column(
        [table_data_container],  # ヘッダーとデータを含める
        scroll=ft.ScrollMode.AUTO,  # 縦スクロールを有効化
        expand=True,
        height=300,
    )

    # 画面コンテナで各コンテナを配置
    data_table = ft.Container(
        content=ft.Column(
            [
                table_header_container,
                table_container,
            ],
        ),
    )

    return data_table
