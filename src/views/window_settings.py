from pathlib import Path

import flet as ft  # type: ignore


def setup_window(page: ft.Page, window_width: int, window_height: int) -> None:
    """
    ウィンドウの設定を行う共通関数。

    Args:
        page (ft.Page): Fletのページオブジェクト
        window_width (int): ウィンドウの幅
        window_height (int): ウィンドウの高さ
    """
    # ウィンドウサイズを固定
    page.window_resizable = False

    # ウィンドウサイズ設定
    page.window_width = window_width
    page.window_height = window_height

    # ウィンドウ初期座標
    page.window_left = 0
    page.window_top = 0
    # # Xサーバー接続の場合ウィンドウバー分オフセット
    # page.window_top = 30

    # ウィンドウを最前面に固定
    page.window_always_on_top = True

    # ページの中央配置設定
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # ソフトウェアアイコンの設定
    # icon_path = os.path.join(os.getcwd(), "assets", "icons", "タイトルロゴ.ico")
    icon_path = Path.cwd() / "assets" / "icons" / "タイトルロゴ.ico"
    page.window.icon = icon_path
