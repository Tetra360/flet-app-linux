# Flet linux

## 実装予定の環境

-   Windows11(wsl2:ubuntu)

## 必要な環境

ホスト環境（windows）に VSCode
仮想環境（wsl2:ubuntu）に Python がインストールされている必要があります。

-   VSCode [インストール](https://code.visualstudio.com/Download)
-   Python 3.13.0 (Pyenv からインストール)
-   venv(Python 3.3 以降に標準搭載)
-   pip（Python 3.4 以降に標準搭載）

---

## セットアップ手順

### 1. 仮想環境の作成 -PowerShell（管理者権限）

```bash
python -m venv venv
```

### 2. 仮想環境のアクティベート -VSCode ターミナル

アクティベートに成功するとターミナルの先頭に`venv` が表示される

```bash
source venv/bin/activate
```

### 3. 依存パッケージのインストール -VSCode ターミナル

```bash
pip install -r requirements.txt
```

### 4. Python バージョンの確認 -VSCode ターミナル

```bash
python --version
```

### 5. インストールした依存パッケージの確認 -VSCode ターミナル

```bash
pip list
```

### 6. 仮想環境を終了する方法 -VSCode ターミナル

```bash
deactivate
```

---

## 開発ルール

### コード分割

MVC パターン（Model-View-Controller）に基づいてディレクトリを分割。

-   models：データ構造やデータベース関連のコードを配置。
-   views：画面デザインや UI に関するコードを配置。
-   controllers：アプリのロジックやユーザー操作に対応するコードを配置。
-   components：再利用可能な UI コンポーネントを配置。
-   assets:アイコンや画像などを配置。

### 開発環境

このプロジェクトではコードの整形や補完など、開発を支援する強力なツールを VSCode 環境に統合して使用しています。
VSCode でワークスペースを開くと、必要なアドオンのインストールポップアップが出現するので、インストールしてください。

### 採用しているコード整形ツール

-   **Ruff**: コード整形,PEP8 準拠の静的解析,インポート文の整理
-   **mypy**: 型ヒントの記述をチェック。
-   **pylance**: 高速なコード補完と解析支援ツール。

`.vscode` フォルダに記載された設定`settings.json`および推奨アドオン`extensions.json`を使用することで、効率的で統一された開発環境を構築できます。

## 使用ライブラリ

windows 動作の GUI アプリを作成するために[Flet](https://flet.dev/)を使用しています。

-   flet v0.25.1<br>
    詳細は、`requirements.txt` を確認してください。

---

## ディレクトリ構成

```plaintext
.
├─.vscode                # VSCodeの設定（ワークスペース起動時読み込み）
│  ├─extensions.json     # 開発環境に必要なアドオン
│  └─settings.json       # 開発環境の設定ファイル
│
├─assets                 # アプリケーションで使用する静的ファイル
│  ├─icons               # アイコンファイル
│  └─images              # 画像ファイル
│
├─src                    # アプリケーションのソースコード
│  ├─components          # UIコンポーネント
│  ├─controllers         # ロジック・制御部分
│  ├─models              # データモデル
│  ├─views               # 画面設計・ビュー
│  └─main.py             # プロジェクトのメイン処理を記述したファイル
│
├─tests                  # テストコード
│
├─venv          # Python仮想環境（ローカル専用）
│  ├─Include
│  ├─Lib
│  │  └─site-packages    # 仮想環境でインストールされたライブラリ
│  └─Scripts             # 仮想環境の実行ファイル
│
├─pyproject.toml         # Ruffとmypyの設定ファイル
└─requirements.txt       # プロジェクトの依存関係を管理するファイル
```

## ホットリロードでの実行

### 開発用の実行コマンド

-   GUI アプリとして実行
    [オプション]

1. デバッグモード
2. ホットリロード

```bash
flet run -d -r src/main.py
```

-   WEB アプリとして実行
    [オプション]

1. デバッグモード
2. ホットリロード
3. web アプリモード

```bash
flet run -d -r --web src/main.py
```

### ホットリロードについて

Flet はホットリロードに対応しており、開発時に都度再実行をせずに保存するだけで修正内容を反映させることができる。<br>

-   VSCode の実行ボタンから実行した場合、ホットリロードが対応しないので注意。
