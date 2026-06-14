#!/usr/bin/env python3
"""
build.py — days/ 内の day-*.html を走査して index.html を自動生成する。

使い方:
    python3 build.py

- day-<N>-<slug>.html という命名のファイルを拾う（Nはday番号）。
- 各ファイルの <h1> をタイトルとして抜き出す。
- 下の CURRICULUM 表と突き合わせ、未作成のdayは「未作成」と表示する。
- 目次（index.html）を docs ルートに書き出す。
"""

import re
import pathlib

ROOT = pathlib.Path(__file__).parent
DAYS_DIR = ROOT / "days"
INDEX = ROOT / "index.html"

# カリキュラム定義（Day番号 → (トピック, フェーズ)）。生きた目次の基準表。
CURRICULUM = [
    # (day, トピック, フェーズ見出し)
    (1,  "がん細胞生物学の最小単位①（細胞周期・アポトーシス）", "フェーズ1：土台づくり"),
    (2,  "がん細胞生物学の最小単位②（シグナル伝達の基本形）", "フェーズ1：土台づくり"),
    (3,  "がん遺伝子 vs がん抑制遺伝子（アクセル/ブレーキ）", "フェーズ1：土台づくり"),
    (4,  "Hallmarks of Cancer 総論", "フェーズ1：土台づくり"),
    (5,  "Hallmark：増殖シグナルの維持／増殖抑制の回避", "フェーズ1：土台づくり"),
    (6,  "Hallmark：細胞死への抵抗性／複製の不死化", "フェーズ1：土台づくり"),
    (7,  "Hallmark：血管新生の誘導／浸潤と転移", "フェーズ1：土台づくり"),
    (8,  "Hallmark：ゲノム不安定性／変異", "フェーズ1：土台づくり"),
    (9,  "Hallmark：免疫からの逃避", "フェーズ1：土台づくり"),
    (10, "Hallmarks 統合・復習", "フェーズ1：土台づくり"),
    (11, "制度とレポートの流れ", "フェーズ1：土台づくり"),
    (12, "パネルの違い・エビデンスレベル", "フェーズ1：土台づくり"),
    (13, "TP53", "フェーズ2：頻出ドライバー遺伝子"),
    (14, "RB1", "フェーズ2：頻出ドライバー遺伝子"),
    (15, "PTEN", "フェーズ2：頻出ドライバー遺伝子"),
    (16, "KRAS / NRAS", "フェーズ2：頻出ドライバー遺伝子"),
    (17, "BRAF", "フェーズ2：頻出ドライバー遺伝子"),
    (18, "EGFR", "フェーズ2：頻出ドライバー遺伝子"),
    (19, "PIK3CA", "フェーズ2：頻出ドライバー遺伝子"),
    (20, "AKT / mTOR", "フェーズ2：頻出ドライバー遺伝子"),
    (21, "BRCA1 / BRCA2", "フェーズ2：頻出ドライバー遺伝子"),
    (22, "ATM", "フェーズ2：頻出ドライバー遺伝子"),
    (23, "ミスマッチ修復系（MLH1/MSH2 等）", "フェーズ2：頻出ドライバー遺伝子"),
    (24, "ALK", "フェーズ2：頻出ドライバー遺伝子"),
    (25, "ROS1 / RET", "フェーズ2：頻出ドライバー遺伝子"),
    (26, "HER2 (ERBB2)", "フェーズ2：頻出ドライバー遺伝子"),
    (27, "MET", "フェーズ2：頻出ドライバー遺伝子"),
    (28, "MYC", "フェーズ2：頻出ドライバー遺伝子"),
    (29, "NTRK融合 ほか tumor-agnostic", "フェーズ2：頻出ドライバー遺伝子"),
    (30, "総まとめ・チートシート集約", "フェーズ2：頻出ドライバー遺伝子"),
]


def find_day_files():
    """day番号 -> ファイルパス の辞書を返す。"""
    found = {}
    if not DAYS_DIR.exists():
        return found
    for p in DAYS_DIR.glob("day-*.html"):
        m = re.match(r"day-(\d+)-", p.name)
        if m:
            found[int(m.group(1))] = p
    return found


def extract_title(path):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"<h1>(.*?)</h1>", text, re.S)
    if m:
        title = re.sub(r"\s+", " ", m.group(1)).strip()
        # 「内容」列では Day番号が別列にあるので、先頭の「Day N：」を取り除く
        title = re.sub(r"^Day\s*\d+\s*[:：]\s*", "", title)
        return title
    return path.stem


def build():
    found = find_day_files()
    rows_by_phase = {}
    done = 0
    for day, topic, phase in CURRICULUM:
        rows_by_phase.setdefault(phase, [])
        if day in found:
            done += 1
            href = f"days/{found[day].name}"
            title = extract_title(found[day])
            link = f'<a href="{href}">{title}</a>'
            status = '<span class="done">✓ 作成済み</span>'
        else:
            link = f"{topic}"
            status = '<span class="todo">未作成</span>'
        rows_by_phase[phase].append((day, link, status))

    sections = []
    for phase in dict.fromkeys(p for _, _, p in CURRICULUM):
        rows = rows_by_phase.get(phase, [])
        body = "\n".join(
            f'      <tr><td class="day">Day {d}</td><td>{link}</td><td>{st}</td></tr>'
            for d, link, st in rows
        )
        sections.append(f"""  <div class="phase">
    <h2>{phase}</h2>
    <table class="toc">
      <tr><th>Day</th><th>内容</th><th>状態</th></tr>
{body}
    </table>
  </div>""")

    total = len(CURRICULUM)
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>がんゲノム学習ノート</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site"><span class="home">がんゲノム学習ノート</span></header>
<h1>がんゲノム学習ノート</h1>
{chr(10).join(sections)}
</body>
</html>
"""
    INDEX.write_text(html, encoding="utf-8")
    print(f"index.html を生成しました（{done}/{total} 日 作成済み）。")

if __name__ == "__main__":
    build()
