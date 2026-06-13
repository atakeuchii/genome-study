# がんゲノム学習ノート

エキスパートパネルのレポートを自力で読み解くための、約1ヶ月のインプット学習ノート。
各dayのHTMLを `days/` に置き、`build.py` で目次（`index.html`）を自動生成して GitHub Pages で公開する。

## 構成

```
.
├── index.html          # 自動生成される目次（build.py が出力）
├── build.py            # days/ を走査して index.html を生成
├── Makefile            # make build / make serve / make commit
├── assets/
│   └── style.css       # 全dayで共通利用するスタイル
├── days/
│   └── day-13-tp53.html   # 1日1ファイル
└── .github/workflows/pages.yml  # push時に自動ビルド＆公開
```

## 日々の流れ

1. このチャットで「day N の学習内容を表示して」と送る。
2. 生成された `day-N-xxx.html` を `days/` に置く。
3. `make build`（= `python3 build.py`）で目次を更新。
4. `make commit` で add → commit → push。
5. GitHub Actions が走り、数分後に Pages に反映。

## ローカル確認

```
make serve   # http://localhost:8000 で確認
```

## 命名規則

`days/day-<番号>-<slug>.html`（例：`day-13-tp53.html`）。
`build.py` はファイル名の番号と `CURRICULUM` 表を突き合わせて目次を作る。
カリキュラムの並びを変えたいときは `build.py` の `CURRICULUM` を編集する。
