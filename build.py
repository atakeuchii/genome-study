#!/usr/bin/env python3
"""
build.py — days/ 内の day-*.html を走査して index.html を自動生成する。
"""
import re, pathlib

ROOT = pathlib.Path(__file__).parent
DAYS_DIR = ROOT / "days"
INDEX = ROOT / "index.html"

CURRICULUM = [
    # (day, トピック, フェーズ見出し)
    (1,  "がん細胞生物学の最小単位①（細胞周期・アポトーシス）", "フェーズ1：土台づくり"),
    (2,  "がん細胞生物学の最小単位②（シグナル伝達の基本形）",   "フェーズ1：土台づくり"),
    (3,  "がん遺伝子 vs がん抑制遺伝子（アクセル/ブレーキ）",   "フェーズ1：土台づくり"),
    (4,  "Hallmarks of Cancer 総論",                          "フェーズ1：土台づくり"),
    (5,  "Hallmark：増殖シグナルの維持",                       "フェーズ1：土台づくり"),
    (6,  "Hallmark：増殖抑制の回避",                           "フェーズ1：土台づくり"),
    (7,  "Hallmark：細胞死への抵抗性",                         "フェーズ1：土台づくり"),
    (8,  "Hallmark：複製の不死化",                             "フェーズ1：土台づくり"),
    (9,  "Hallmark：血管新生の誘導",                           "フェーズ1：土台づくり"),
    (10, "Hallmark：浸潤と転移",                               "フェーズ1：土台づくり"),
    (11, "Hallmark：ゲノム不安定性／変異",                     "フェーズ1：土台づくり"),
    (12, "Hallmark：免疫からの逃避",                           "フェーズ1：土台づくり"),
    (13, "Hallmark：エネルギー代謝の再編",                     "フェーズ1：土台づくり"),
    (14, "Hallmark：がんを促す炎症",                           "フェーズ1：土台づくり"),
    (15, "制度とレポートの流れ",                               "フェーズ1：土台づくり"),
    (16, "パネルの違い・エビデンスレベル",                     "フェーズ1：土台づくり"),
    (17, "MAPK/ERK経路",                                      "フェーズ2：パスウェイ各論"),
    (18, "PI3K/AKT/mTOR経路",                                 "フェーズ2：パスウェイ各論"),
    (19, "細胞周期制御経路",                                   "フェーズ2：パスウェイ各論"),
    (20, "アポトーシス経路（BCL-2系）",                        "フェーズ2：パスウェイ各論"),
    (21, "Wnt/β-catenin経路",                                 "フェーズ2：パスウェイ各論"),
    (22, "低酸素応答経路（HIF/VEGF）",                        "フェーズ2：パスウェイ各論"),
]

SUPPLEMENT = [
    ("TP53 — がんゲノムの主役",                "supplement/tp53.html"),
    ("RB1 — 細胞周期G1/Sの門番",              "supplement/rb1.html"),
    ("PTEN — PI3K経路のブレーキ",             "supplement/pten.html"),
    ("KRAS / NRAS — 二大幹線の分岐点",        "supplement/kras-nras.html"),
    ("BRAF — V600Eと阻害薬の組み合わせ",      "supplement/braf.html"),
    ("EGFR — 受容体そのものが標的",           "supplement/egfr.html"),
    ("HER2（ERBB2）— 増幅と抗HER2療法",       "supplement/her2.html"),
    ("MET — エクソン14スキッピングと増幅",    "supplement/met.html"),
    ("PIK3CA — PI3K経路のアクセル",           "supplement/pik3ca.html"),
    ("AKT / mTOR — PI3K経路の中枢",           "supplement/akt-mtor.html"),
    ("CDK4/6 — 細胞周期の鍵を回す役",        "supplement/cdk4-6.html"),
    ("CDKN2A（p16）— CDKのブレーキ役",        "supplement/cdkn2a.html"),
    ("MDM2 — p53の分解係",                    "supplement/mdm2.html"),
    ("BCL-2ファミリー — アポトーシス制御",    "supplement/bcl2.html"),
    ("APC — Wnt経路のブレーキ役",             "supplement/apc.html"),
    ("VHL — HIF1αのブレーキ役",               "supplement/vhl.html"),
    ("BRCA1 / BRCA2 — 合成致死とPARP阻害薬", "supplement/brca.html"),
    ("ATM — 損傷を感知する見張り役",          "supplement/atm.html"),
]

def find_day_files():
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
        title = re.sub(r"^Day\s*\d+\s*[:：]\s*", "", title)
        return title
    return path.stem

def build():
    found = find_day_files()
    rows_by_phase = {}
    done = 0
    total = len(CURRICULUM)

    for day, topic, phase in CURRICULUM:
        rows_by_phase.setdefault(phase, [])
        if day in found:
            done += 1
            href = f"days/{found[day].name}"
            title = extract_title(found[day])
            link = f'<a href="{href}">{title}</a>'
            status = '<span class="done">✓ 作成済み</span>'
        else:
            link = topic
            status = '<span class="todo">未作成</span>'
        rows_by_phase[phase].append((day, link, status))

    sections = []
    for phase in dict.fromkeys(p for _, _, p in CURRICULUM):
        rows = rows_by_phase.get(phase, [])
        body = "\n".join(
            f'      <tr><td class="day">Day {d}</td><td>{lk}</td><td>{st}</td></tr>'
            for d, lk, st in rows
        )
        sections.append(f"""  <div class="phase">
    <h2>{phase}</h2>
    <table class="toc">
      <tr><th>Day</th><th>内容</th><th>状態</th></tr>
{body}
    </table>
  </div>""")

    # 補足（遺伝子別）セクション
    sup_rows = []
    for title, path in SUPPLEMENT:
        full = ROOT / path
        if full.exists():
            sup_rows.append(f'      <tr><td colspan="2"><a href="{path}">{title}</a></td><td><span class="done">✓</span></td></tr>')
        else:
            sup_rows.append(f'      <tr><td colspan="2">{title}</td><td><span class="todo">未作成</span></td></tr>')

    sup_section = f"""  <div class="phase">
    <h2>補足：遺伝子別リファレンス</h2>
    <p style="font-size:14px;color:#777">パスウェイを学んだあと、特定の遺伝子の詳細を確認したいときに参照する。</p>
    <table class="toc">
      <tr><th colspan="2">遺伝子</th><th>状態</th></tr>
{chr(10).join(sup_rows)}
    </table>
  </div>"""

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
<p>進捗：<strong>{done} / {total} 日</strong> 作成済み。</p>
{chr(10).join(sections)}
{sup_section}
<footer class="site">build.py により自動生成。</footer>
</body>
</html>
"""
    INDEX.write_text(html, encoding="utf-8")
    print(f"index.html を生成しました（{done}/{total} 日 作成済み）。")

if __name__ == "__main__":
    build()
