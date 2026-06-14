#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_phase1.py — フェーズ1（Day 1–12）のHTMLを一括生成する。
各dayの本文は PAGES に定義。共通のヘッダ／Next-Backナビ／フッタを付けて days/ に書き出す。
Day 13（TP53）は既存なので、Day 12 の Next は day-13-tp53.html を指す。
"""

import pathlib

DAYS = pathlib.Path(__file__).parent / "days"
DAYS.mkdir(exist_ok=True)

# (day, slug, h1, tags_html, body_html)
# slug は day-<n>-<slug>.html の <slug> 部分
# ナビは day 番号順で前後に自動リンク。最後（12）の次は day-13-tp53.html。

NEXT_OVERRIDE = {12: "day-13-tp53.html"}  # 既存ファイルへ接続

PAGES = []

def add(day, slug, h1, tags, body):
    PAGES.append((day, slug, h1, tags, body))

# ------------------------------------------------------------------ Day 1
add(1, "cellcycle-apoptosis",
    "Day 1：がん細胞生物学の最小単位①（細胞周期・アポトーシス）",
    '<span class="tag hall">フェーズ1：土台づくり</span> <span class="tag hall">全パスウェイの共通言語</span>',
    """
<div class="pos">
<strong>全体マップの中での位置づけ</strong><br>
フェーズ1の初日。ここで扱う「細胞周期」と「アポトーシス」は、特定のパスウェイの話ではなく、以降に出てくるほぼ全ての経路・遺伝子が最終的に行き着く<strong>出力（アウトプット）</strong>にあたる。がんとは煎じ詰めれば「増えるべきでない細胞が増え、死ぬべき細胞が死なない」状態なので、その「増える＝細胞周期」「死ぬ＝アポトーシス」の2つを最初に押さえておくと、後の経路がすべて「この2つをどちらに傾けるか」の話として読める。既知の内容と思うので、用語の確認と"なぜ骨格の土台になるか"に絞る。
</div>

<h2>① 細胞周期 ── 細胞が分裂するときの4段階</h2>
<p>細胞が1個から2個に分裂するまでの一連の流れが細胞周期。4つの局面をぐるぐる回る。</p>
<ul>
  <li><strong>G1期</strong>：分裂の準備期。細胞が大きくなり、DNA複製の材料を揃える。「分裂する／しない」を決める最重要の岐路がここ。</li>
  <li><strong>S期</strong>：DNAを複製する（Synthesis）。ゲノムが2セットにコピーされる。</li>
  <li><strong>G2期</strong>：分裂前の最終点検期。複製がうまくいったかを確認する。</li>
  <li><strong>M期</strong>：実際に細胞が2つに分かれる（Mitosis）。</li>
</ul>
<p>分裂しない成熟細胞は、G1から外れて <strong>G0期</strong>（お休み状態）に入る。正常な体ではほとんどの細胞がG0で待機し、必要なときだけ周期に復帰する。</p>

<h2>② チェックポイント ── 周期を進めてよいか確認する関所</h2>
<p>細胞周期には「次に進んでいいか？」を判定する<strong>チェックポイント（関所）</strong>がある。傷を持ったまま分裂すると傷ごとコピーされるため、関所で止めて修理する仕組みが要る。とくに重要なのが2つ：</p>
<ul>
  <li><strong>G1/Sチェックポイント</strong>：DNA複製を始める前の関所。「設計図に傷はないか？」を確認。守る代表選手が <strong>Rb（RB1）</strong> と <strong>p53（TP53）</strong>。← Day 13・14 で主役に</li>
  <li><strong>G2/Mチェックポイント</strong>：分裂を始める前の関所。「複製は正しく終わったか？」を確認。</li>
</ul>
<p>ここが核心。<strong>がん抑制遺伝子（ブレーキ系）の多くはこの関所の番人</strong>で、壊れると関所が機能せず傷ついた細胞が分裂を続ける。逆に<strong>がん遺伝子（アクセル系）の多くは関所を強引に通過させる</strong>。フェーズ2の遺伝子の意味づけは、ほぼこの構図に収まる。</p>

<div class="fig">
<svg viewBox="0 0 520 360" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, Helvetica, Arial, sans-serif">
  <defs><marker id="cyc" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="#2c6e8f"/></marker></defs>
  <text x="260" y="28" text-anchor="middle" font-size="17" font-weight="700" fill="#222">細胞周期と2つの関所</text>
  <circle cx="260" cy="200" r="110" fill="none" stroke="#cfe0e8" stroke-width="2"/>
  <path d="M260,90 A110,110 0 0,1 370,200" fill="none" stroke="#2c6e8f" stroke-width="3" marker-end="url(#cyc)"/>
  <path d="M370,200 A110,110 0 0,1 260,310" fill="none" stroke="#2c6e8f" stroke-width="3" marker-end="url(#cyc)"/>
  <path d="M260,310 A110,110 0 0,1 150,200" fill="none" stroke="#2c6e8f" stroke-width="3" marker-end="url(#cyc)"/>
  <path d="M150,200 A110,110 0 0,1 260,90" fill="none" stroke="#2c6e8f" stroke-width="3" marker-end="url(#cyc)"/>
  <text x="260" y="78" text-anchor="middle" font-size="14" font-weight="700" fill="#1f4d5e">M期</text>
  <text x="260" y="64" text-anchor="middle" font-size="10.5" fill="#777">分裂</text>
  <text x="392" y="204" text-anchor="middle" font-size="14" font-weight="700" fill="#1f4d5e">G1期</text>
  <text x="392" y="220" text-anchor="middle" font-size="10.5" fill="#777">準備</text>
  <text x="260" y="332" text-anchor="middle" font-size="14" font-weight="700" fill="#1f4d5e">S期</text>
  <text x="260" y="348" text-anchor="middle" font-size="10.5" fill="#777">DNA複製</text>
  <text x="128" y="204" text-anchor="middle" font-size="14" font-weight="700" fill="#1f4d5e">G2期</text>
  <text x="128" y="220" text-anchor="middle" font-size="10.5" fill="#777">点検</text>
  <text x="260" y="196" text-anchor="middle" font-size="12" fill="#999">細胞周期</text>
  <text x="260" y="212" text-anchor="middle" font-size="11" fill="#bbb">（時計回り）</text>
  <rect x="348" y="270" width="168" height="46" rx="8" fill="#fdecea" stroke="#c0392b" stroke-width="1.3"/>
  <text x="432" y="290" text-anchor="middle" font-size="11.5" font-weight="700" fill="#a5281b">G1/S チェックポイント</text>
  <text x="432" y="306" text-anchor="middle" font-size="10" fill="#a5281b">番人：Rb・p53</text>
  <line x1="360" y1="270" x2="330" y2="250" stroke="#c0392b" stroke-width="1.2"/>
  <rect x="4" y="270" width="150" height="46" rx="8" fill="#fdecea" stroke="#c0392b" stroke-width="1.3"/>
  <text x="79" y="290" text-anchor="middle" font-size="11.5" font-weight="700" fill="#a5281b">G2/M チェックポイント</text>
  <text x="79" y="306" text-anchor="middle" font-size="10" fill="#a5281b">複製の正しさを点検</text>
  <line x1="150" y1="272" x2="178" y2="250" stroke="#c0392b" stroke-width="1.2"/>
</svg>
<div class="caption">独自作図。青い矢印が周期の進行方向、赤い枠が「進めてよいか確認する関所」。</div>
</div>

<h2>③ アポトーシス ── 細胞の「自殺プログラム」</h2>
<p>アポトーシスは細胞があらかじめ持つ<strong>計画的な自滅の仕組み</strong>。事故的に破裂して周囲に害を及ぼす壊死（ネクローシス）と違い、内容物を撒き散らさず静かに片付けられる管理された死。</p>
<ul>
  <li><strong>傷ついた細胞の処分</strong>：DNAの傷が直しきれないとき、生かしておくとがん化リスクになる。だから「直せないなら死なせる」最終手段がある。p53はこの引き金役の一人。</li>
  <li><strong>不要な細胞の整理</strong>：発生過程（指の間の水かきが消える等）や役目を終えた細胞の除去にも使う、生体に必須の正常機能。</li>
</ul>
<p>がんでは<strong>「死ぬべき細胞が死ねなくなる（アポトーシス抵抗性）」</strong>のが大問題。これはHallmark「細胞死への抵抗性」（Day 6）そのもので、BCL-2系がこのバランスを握る。</p>

<div class="note">
<strong>この日の要点（後ろへのつながり）</strong><br>
・がん＝「増える（細胞周期）」と「死ぬ（アポトーシス）」のバランス破綻。以降の全パスウェイはこの2つのどちらかを動かす話に帰着する。<br>
・<strong>細胞周期の関所＝がん抑制遺伝子（ブレーキ）の主戦場</strong>。Day 13・14 に直結。<br>
・<strong>アポトーシスを止めない仕組み＝Hallmark「細胞死への抵抗性」</strong>。Day 6 に直結。<br>
・次の Day 2 は、これらの「出力」を動かす「入力と配線」＝シグナル伝達を扱う。
</div>
""")

# ------------------------------------------------------------------ Day 2
add(2, "signal-transduction",
    "Day 2：がん細胞生物学の最小単位②（シグナル伝達の基本形）",
    '<span class="tag hall">フェーズ1：土台づくり</span> <span class="tag gas">以降の経路図を読む下地</span>',
    """
<div class="pos">
<strong>全体マップの中での位置づけ</strong><br>
Day 1 が「増える／死ぬ」という<strong>出力</strong>の話だったのに対し、今日はその出力を動かす<strong>入力と配線</strong>＝シグナル伝達を扱う。フェーズ2の遺伝子（EGFR・KRAS・BRAF…）の大半はこの配線図のどこかの<strong>部品</strong>で、活性化型変異とは「その部品がスイッチ入りっぱなしで固定される」こと。今日の"型"が入っていれば、Day 16 以降の経路図は「同じ型の具体例」として読める。
</div>

<h2>① シグナル伝達とは ── 細胞の「指示の伝言ゲーム」</h2>
<p>細胞は勝手に増えるのではなく、<strong>外から来る指示</strong>を受けて動く。指示が外から核まで届く流れがシグナル伝達。基本形はどの経路でもほぼ共通で、4段階の伝言ゲーム。</p>
<ul>
  <li><strong>(1) シグナル分子（リガンド／増殖因子）</strong>：細胞の外を漂う「指示書」。</li>
  <li><strong>(2) 受容体</strong>：細胞膜の「受け取り口」。がんで重要なのは <strong>RTK（受容体型チロシンキナーゼ）</strong>。EGFR（Day 18）・HER2（Day 26）・MET（Day 27）が仲間。</li>
  <li><strong>(3) 中継分子（細胞内リレー）</strong>：情報を核までバケツリレー。KRAS（Day 16）→ BRAF（Day 17）→ … がこのリレー部隊。</li>
  <li><strong>(4) 転写因子 → 遺伝子オン</strong>：終点。核内で遺伝子をオンにし「増殖タンパクを作れ」と実行。これがDay 1の細胞周期を回す。</li>
</ul>

<h2>② スイッチの仕組み ── リン酸化という「オン/オフのボタン」</h2>
<p>リレーで情報を渡す主な方法が <strong>リン酸化</strong>。ある分子が次にリン酸基を付けるとスイッチが入る。<strong>キナーゼ</strong>＝「次の分子にリン酸を付けてオンにする酵素」。RTKの "K" もキナーゼのK。ポイントは<strong>増幅</strong>（下るほど反応が大きくなる）と<strong>可逆性</strong>（ホスファターゼで外れ、正常では一時的）。</p>

<div class="fig">
<svg viewBox="0 0 560 560" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, Helvetica, Arial, sans-serif">
  <defs><marker id="a2" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="#2c6e8f"/></marker></defs>
  <text x="280" y="28" text-anchor="middle" font-size="17" font-weight="700" fill="#222">シグナル伝達の基本形（4段階の伝言ゲーム）</text>
  <text x="20" y="58" font-size="11" fill="#999">細胞外</text>
  <rect x="200" y="48" width="160" height="40" rx="20" fill="#eef2fb" stroke="#2f3f8f" stroke-width="1.4"/>
  <text x="280" y="66" text-anchor="middle" font-size="12.5" font-weight="700" fill="#2f3f8f">(1) シグナル分子</text>
  <text x="280" y="81" text-anchor="middle" font-size="10.5" fill="#566">増殖因子（リガンド）</text>
  <path d="M280,88 L280,112" fill="none" stroke="#2c6e8f" stroke-width="1.8" marker-end="url(#a2)"/>
  <rect x="0" y="120" width="560" height="26" fill="#f3ede2"/>
  <text x="20" y="137" font-size="11" fill="#b29a5f">細胞膜</text>
  <rect x="230" y="108" width="100" height="50" rx="6" fill="#fff4d6" stroke="#caa23a" stroke-width="1.8"/>
  <text x="280" y="129" text-anchor="middle" font-size="12" font-weight="700" fill="#7a5c10">(2) 受容体</text>
  <text x="280" y="144" text-anchor="middle" font-size="10" fill="#9a7d2e">RTK（例：EGFR）</text>
  <path d="M280,158 L280,182" fill="none" stroke="#2c6e8f" stroke-width="1.8" marker-end="url(#a2)"/>
  <text x="20" y="210" font-size="11" fill="#999">細胞内</text>
  <rect x="205" y="186" width="150" height="36" rx="8" fill="#eaf4f9" stroke="#2c6e8f" stroke-width="1.3"/>
  <text x="280" y="203" text-anchor="middle" font-size="11.5" font-weight="700" fill="#1d4e64">(3) 中継分子 ①</text>
  <text x="280" y="217" text-anchor="middle" font-size="10" fill="#557">例：KRAS</text>
  <text x="372" y="208" font-size="11" fill="#a5281b">─P→ ON</text>
  <path d="M280,222 L280,242" fill="none" stroke="#2c6e8f" stroke-width="1.8" marker-end="url(#a2)"/>
  <rect x="205" y="246" width="150" height="36" rx="8" fill="#eaf4f9" stroke="#2c6e8f" stroke-width="1.3"/>
  <text x="280" y="263" text-anchor="middle" font-size="11.5" font-weight="700" fill="#1d4e64">中継分子 ②</text>
  <text x="280" y="277" text-anchor="middle" font-size="10" fill="#557">例：BRAF → MEK</text>
  <text x="372" y="268" font-size="11" fill="#a5281b">─P→ ON</text>
  <path d="M280,282 L280,302" fill="none" stroke="#2c6e8f" stroke-width="1.8" marker-end="url(#a2)"/>
  <rect x="205" y="306" width="150" height="36" rx="8" fill="#eaf4f9" stroke="#2c6e8f" stroke-width="1.3"/>
  <text x="280" y="323" text-anchor="middle" font-size="11.5" font-weight="700" fill="#1d4e64">中継分子 ③</text>
  <text x="280" y="337" text-anchor="middle" font-size="10" fill="#557">例：ERK</text>
  <path d="M280,342 L280,366" fill="none" stroke="#2c6e8f" stroke-width="1.8" marker-end="url(#a2)"/>
  <rect x="120" y="372" width="320" height="120" rx="40" fill="#f6f3fb" stroke="#7a5ca0" stroke-width="1.6"/>
  <text x="280" y="396" text-anchor="middle" font-size="11" fill="#7a5ca0">核（遺伝子のある場所）</text>
  <rect x="190" y="408" width="180" height="34" rx="8" fill="#ede7f6" stroke="#7a5ca0" stroke-width="1.3"/>
  <text x="280" y="430" text-anchor="middle" font-size="12" font-weight="700" fill="#553f7a">(4) 転写因子 → 遺伝子ON</text>
  <path d="M280,442 L280,460" fill="none" stroke="#7a5ca0" stroke-width="1.8" marker-end="url(#a2)"/>
  <text x="280" y="478" text-anchor="middle" font-size="12.5" font-weight="700" fill="#1f5d39">出力：増殖・生存タンパクを作る</text>
  <text x="280" y="492" text-anchor="middle" font-size="10.5" fill="#3a6b4d">＝ Day 1 の細胞周期を回す</text>
  <rect x="404" y="372" width="150" height="80" rx="8" fill="#fdecea" stroke="#c0392b" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="479" y="396" text-anchor="middle" font-size="11" font-weight="700" fill="#a5281b">がんでは</text>
  <text x="479" y="414" text-anchor="middle" font-size="10" fill="#933">中継のどれかが</text>
  <text x="479" y="428" text-anchor="middle" font-size="10" fill="#933">「ON固定」になり</text>
  <text x="479" y="442" text-anchor="middle" font-size="10" fill="#933">指示なしでも増殖</text>
</svg>
<div class="caption">独自作図。上（細胞外）から下（核）への流れが基本形。「─P→ ON」はリン酸化によるスイッチ・オン。</div>
</div>

<h2>③ がんとのつながり ── 「ボタンが押されっぱなし」になる</h2>
<p>正常では一時的なはずのスイッチが、がんでは<strong>指示がなくてもオンに固定される</strong>。これが Day 3 の<strong>活性化型変異（アクセル系）</strong>の正体。受容体が勝手にオン（EGFR／Day 18）、中継分子が上流と無関係にオン固定（KRAS／Day 16、BRAF V600E／Day 17）。どこか1か所でも固定されると下流すべてが押し続けられ、増殖シグナルが鳴りやまない＝Hallmark「増殖シグナルの維持」（Day 5）。<strong>分子標的薬の多くはこの固定スイッチを薬でオフにする</strong>。アクセル系が狙いやすいのは止める場所が明確だから——Day 13 のブレーキ系の裏返し。</p>

<div class="note">
<strong>この日の要点（後ろへのつながり）</strong><br>
・基本形＝<strong>シグナル分子 → 受容体 → 中継分子 → 転写因子（遺伝子ON）</strong> の4段リレー。フェーズ2の遺伝子はこの配線図の部品。<br>
・主役は<strong>リン酸化（キナーゼがスイッチを押す）</strong>。正常では一時的・可逆的。<br>
・<strong>活性化型変異＝どこかの部品が「ON固定」</strong>（Day 5「増殖シグナルの維持」）。<br>
・次の Day 3 で「ON固定（アクセル）」と「関所の番人の故障（ブレーキ）」を、<strong>がん遺伝子 vs がん抑制遺伝子</strong>として正式に対比する。
</div>
""")

# ------------------------------------------------------------------ Day 3
add(3, "oncogene-vs-suppressor",
    "Day 3：がん遺伝子 vs がん抑制遺伝子（アクセル/ブレーキ）",
    '<span class="tag gas">アクセル系</span> <span class="tag brake">ブレーキ系</span> <span class="tag hall">フェーズ2の全遺伝子を分類する軸</span>',
    """
<div class="pos">
<strong>全体マップの中での位置づけ</strong><br>
Day 1（出力＝細胞周期・アポトーシス）と Day 2（入力＝シグナル伝達）で体感した「アクセル／ブレーキ」を、ここで正式な用語と分類軸として固める。フェーズ2で出てくる遺伝子は、まずこの2分類のどちらかに振り分けてから中身を見る。<strong>常に問う1問目「アクセル系かブレーキ系か？」の基準を作る回</strong>。
</div>

<h2>① 2つのタイプ ── アクセルを踏む遺伝子と、ブレーキをかける遺伝子</h2>
<p>がんに関わる遺伝子は、大きく2タイプに分けると整理しやすい。</p>
<ul>
  <li><strong>がん遺伝子（oncogene／アクセル系）</strong>：正常では「増えろ」の指示を適切に伝える部品。これが<strong>活性化型変異</strong>で「踏みっぱなし」になると、指示なしで増殖が進む。Day 2 の配線図で「ON固定」になった部品がこれ。</li>
  <li><strong>がん抑制遺伝子（tumor suppressor／ブレーキ系）</strong>：正常では「止めろ・直せ・死ね」を担う番人。これが<strong>機能喪失型変異</strong>で「効かなく」なると、暴走を止められない。Day 1 の関所の番人（Rb・p53）がこれ。</li>
</ul>

<h2>② 変異の入り方が逆 ── 「片方でいい」か「両方やられる必要がある」か</h2>
<p>2タイプは、壊れ方の論理も対照的。ここがレポート読解で効く。</p>
<ul>
  <li><strong>アクセル系は「1か所」で十分</strong>：2本ある遺伝子コピーの片方が活性化変異を起こすだけで、踏みっぱなしになる（顕性／優性的に働く）。少しの変異で効く＝検出されたら意味が大きいことが多い。</li>
  <li><strong>ブレーキ系は原則「両方」やられて初めて効く</strong>：片方が壊れてももう片方が効いていればブレーキは残る。両コピーが失われて初めて機能喪失＝<strong>ツーヒット（two-hit）仮説</strong>。遺伝性のがんでは「生まれつき片方が壊れている」ぶん、もう1ヒットで発症しやすい。</li>
</ul>
<p><strong>例外として覚えておく</strong>：p53（Day 13）は、変異型が残った正常コピーの足を引っ張る<strong>優性阻害（dominant-negative）</strong>があり、1ヒット的に効くことがある。原則と例外をセットにしておくと、TP53の振る舞いが腑に落ちる。</p>

<div class="fig">
<svg viewBox="0 0 620 300" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, Helvetica, Arial, sans-serif">
  <text x="310" y="28" text-anchor="middle" font-size="16" font-weight="700" fill="#222">アクセル系とブレーキ系の対比</text>
  <rect x="20" y="50" width="280" height="220" rx="12" fill="#eef2fb" stroke="#2f3f8f" stroke-width="1.4"/>
  <text x="160" y="78" text-anchor="middle" font-size="14" font-weight="700" fill="#2f3f8f">がん遺伝子（アクセル）</text>
  <text x="160" y="104" text-anchor="middle" font-size="12" fill="#333">活性化型変異で「ON固定」</text>
  <text x="160" y="128" text-anchor="middle" font-size="12" fill="#333">片方の変異で効く（1ヒット）</text>
  <text x="160" y="152" text-anchor="middle" font-size="12" fill="#333">＝踏みっぱなし</text>
  <text x="160" y="186" text-anchor="middle" font-size="11.5" fill="#666">薬：固定スイッチをOFFにする</text>
  <text x="160" y="206" text-anchor="middle" font-size="11.5" fill="#1f5d39">＝狙いやすい（阻害薬）</text>
  <text x="160" y="240" text-anchor="middle" font-size="11" fill="#888">例：KRAS / BRAF / EGFR / HER2</text>
  <rect x="320" y="50" width="280" height="220" rx="12" fill="#fdecea" stroke="#c0392b" stroke-width="1.4"/>
  <text x="460" y="78" text-anchor="middle" font-size="14" font-weight="700" fill="#a5281b">がん抑制遺伝子（ブレーキ）</text>
  <text x="460" y="104" text-anchor="middle" font-size="12" fill="#333">機能喪失型変異で「効かない」</text>
  <text x="460" y="128" text-anchor="middle" font-size="12" fill="#333">原則 両方やられて効く（2ヒット）</text>
  <text x="460" y="152" text-anchor="middle" font-size="12" fill="#333">＝番人の不在</text>
  <text x="460" y="186" text-anchor="middle" font-size="11.5" fill="#666">薬：失われた機能を戻す必要</text>
  <text x="460" y="206" text-anchor="middle" font-size="11.5" fill="#a5281b">＝狙いにくい</text>
  <text x="460" y="240" text-anchor="middle" font-size="11" fill="#888">例：TP53 / RB1 / PTEN / BRCA</text>
</svg>
<div class="caption">独自作図。レポートで遺伝子を見たら、まずこの左右どちらかに振り分けるのが第一歩。</div>
</div>

<h2>③ もうひとつの分け方 ── 門番（gatekeeper）と管理人（caretaker）</h2>
<p>ブレーキ系はさらに2役に分けると見通しがよい。<strong>門番（gatekeeper）</strong>＝増殖そのものを直接止める番人（Rb・p53・PTEN）。<strong>管理人（caretaker）</strong>＝DNAの傷を修理してゲノムを守る係（BRCA・ミスマッチ修復系）。管理人が壊れると、傷が溜まって他の遺伝子の変異が雪だるま式に増える（Day 8「ゲノム不安定性」）。フェーズ2後半のDNA修復系（Day 21–23）はこの管理人グループ。</p>

<div class="note">
<strong>この日の要点（後ろへのつながり）</strong><br>
・<strong>アクセル系＝活性化型・1ヒット・狙いやすい（引き算）／ブレーキ系＝機能喪失・原則2ヒット・狙いにくい（足し算）</strong>。<br>
・例外：p53 の優性阻害（Day 13 で再登場）。<br>
・ブレーキ系は<strong>門番</strong>（増殖を止める）と<strong>管理人</strong>（DNAを守る）に分けられる。後者はDay 8・21–23へ。<br>
・次の Day 4 から、これらを束ねる骨格 <strong>Hallmarks of Cancer</strong> に入る。
</div>
""")

# ------------------------------------------------------------------ Day 4
add(4, "hallmarks-overview",
    "Day 4：Hallmarks of Cancer 総論",
    '<span class="tag hall">最重要骨格の入口</span>',
    """
<div class="pos">
<strong>全体マップの中での位置づけ</strong><br>
この学習全体の<strong>背骨</strong>。Day 1–3 で部品（細胞周期・シグナル伝達・アクセル/ブレーキ）を見てきたが、Hallmarks は「正常細胞ががん細胞になるために獲得する能力の一覧」で、すべてのパスウェイ・遺伝子をぶら下げるフォルダ構造になる。上司の言う「がんの気持ちになればわかる」とは、この一覧から演繹する見方のこと。Day 4–10 で1週間かけてじっくり扱う、その総論。
</div>

<h2>① Hallmarks of Cancer とは</h2>
<p>2000年に Hanahan と Weinberg が提唱した枠組みで、「種類の違うどんながんでも、共通して獲得している能力がある」とまとめたもの。最初は6つ、2011年の改訂で計10項目（6つの中核＋2つの新興能力＋2つの土台的特性）に整理された。丸暗記ではなく、<strong>「がん細胞が生き延びて増え続けるには、これらの能力が要る」という必然性で理解する</strong>のがコツ。</p>

<h2>② 10項目の一覧（Day 5–9 への割り当て）</h2>
<ul>
  <li><strong>増殖シグナルの維持</strong>（自分でアクセルを踏み続ける）— Day 5</li>
  <li><strong>増殖抑制の回避</strong>（ブレーキを無視する）— Day 5</li>
  <li><strong>細胞死への抵抗性</strong>（死ねと言われても死なない）— Day 6</li>
  <li><strong>複製の不死化</strong>（無限に分裂できる）— Day 6</li>
  <li><strong>血管新生の誘導</strong>（自前の血管を引き込み栄養を確保）— Day 7</li>
  <li><strong>浸潤と転移</strong>（周囲に侵入し、遠くへ広がる）— Day 7</li>
  <li><strong>ゲノム不安定性と変異</strong>（土台的特性：変異を生みやすくする）— Day 8</li>
  <li><strong>免疫からの逃避</strong>（免疫の監視をかわす）— Day 9</li>
  <li>（新興）<strong>エネルギー代謝の再編</strong>／（土台）<strong>がんを促す炎症</strong> — Day 8–9 で簡単に触れる</li>
</ul>
<p>※2022年にはさらに「表現型可塑性」など新次元が提案され、いまも更新が続く生きた枠組み。本学習では中核10項目を骨格にする。</p>

<div class="fig">
<svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, Helvetica, Arial, sans-serif">
  <text x="320" y="28" text-anchor="middle" font-size="16" font-weight="700" fill="#222">Hallmarks ＝ がん細胞が獲得する能力のフォルダ</text>
  <circle cx="320" cy="200" r="48" fill="#fff4d6" stroke="#caa23a" stroke-width="2"/>
  <text x="320" y="196" text-anchor="middle" font-size="13" font-weight="700" fill="#7a5c10">がん細胞</text>
  <text x="320" y="214" text-anchor="middle" font-size="10.5" fill="#9a7d2e">10の能力</text>
  <g font-size="11.5" fill="#1f4d5e">
    <text x="320" y="70" text-anchor="middle">増殖シグナルの維持</text>
    <text x="540" y="120" text-anchor="middle">増殖抑制の回避</text>
    <text x="600" y="200" text-anchor="middle">細胞死への抵抗性</text>
    <text x="540" y="285" text-anchor="middle">複製の不死化</text>
    <text x="320" y="335" text-anchor="middle">血管新生の誘導</text>
    <text x="100" y="285" text-anchor="middle">浸潤と転移</text>
    <text x="40" y="200" text-anchor="middle">ゲノム不安定性</text>
    <text x="100" y="120" text-anchor="middle">免疫からの逃避</text>
  </g>
  <g stroke="#cfe0e8" stroke-width="1.2">
    <line x1="320" y1="152" x2="320" y2="80"/>
    <line x1="362" y1="178" x2="500" y2="128"/>
    <line x1="368" y1="200" x2="540" y2="200"/>
    <line x1="362" y1="222" x2="500" y2="278"/>
    <line x1="320" y1="248" x2="320" y2="322"/>
    <line x1="278" y1="222" x2="140" y2="278"/>
    <line x1="272" y1="200" x2="90" y2="200"/>
    <line x1="278" y1="178" x2="140" y2="128"/>
  </g>
</svg>
<div class="caption">独自作図。中心の「がん細胞」に8つの代表能力をぶら下げたイメージ。各能力に代表パスウェイ・遺伝子が紐づく。</div>
</div>

<div class="note">
<strong>この日の要点（後ろへのつながり）</strong><br>
・Hallmarks＝<strong>がん細胞が獲得する能力の一覧＝全パスウェイを束ねるフォルダ構造</strong>。<br>
・丸暗記でなく「増え続けるには何が要るか」という<strong>必然性</strong>で捉える。<br>
・Day 5–9 で1項目ずつ代表経路と結びつけ、Day 10 で統合する。<br>
・<strong>常に問う2問</strong>：①どのHallmarkに効く？ ②アクセルかブレーキか？ ── このうち①の土俵がここで完成する。
</div>
""")

# ------------------------------------------------------------------ Day 5
add(5, "hallmark-proliferation",
    "Day 5：Hallmark｜増殖シグナルの維持／増殖抑制の回避",
    '<span class="tag hall">Hallmark</span> <span class="tag gas">アクセル：MAPK・PI3K</span> <span class="tag brake">ブレーキ：Rb・p53</span>',
    """
<div class="pos">
<strong>全体マップの中での位置づけ</strong><br>
Hallmarksの中核2つを<strong>「アクセルとブレーキの両輪」</strong>としてまとめて扱う。Day 2 の配線図と Day 3 の分類が、ここで初めて具体的な経路名（MAPK・PI3K・Rb・p53）と結びつく。フェーズ2の主力遺伝子が最も密集する領域でもある。
</div>

<h2>① 増殖シグナルの維持（アクセルを踏み続ける）</h2>
<p>正常細胞は増殖因子が来たときだけ増える。がん細胞は<strong>自前でアクセルを踏み続ける</strong>。代表経路が2本：</p>
<ul>
  <li><strong>MAPK/ERK経路</strong>：RTK→RAS→RAF→MEK→ERK。増殖の号令を核へ運ぶ主幹線。KRAS（Day 16）・BRAF（Day 17）・EGFR（Day 18）が乗る。Day 16 で図を厚くする。</li>
  <li><strong>PI3K/AKT/mTOR経路</strong>：生存・代謝・増殖の中枢。PIK3CA（Day 19）・AKT/mTOR（Day 20）が乗り、ブレーキ役のPTEN（Day 15）が外れると暴走する。</li>
</ul>

<h2>② 増殖抑制の回避（ブレーキを無視する）</h2>
<p>正常細胞は「もう増えるな」の合図でG1/S関所（Day 1）に止まる。がん細胞はこのブレーキを壊して無視する。主役は<strong>Rb（RB1／Day 14）</strong>と<strong>p53（TP53／Day 13）</strong>。Rbは「増殖開始を直接押しとどめる門番」、p53は「傷を見つけたら止める・直す・殺すの統括」。どちらもブレーキ系で、両輪のもう片側を担う。</p>

<div class="fig">
<svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, Helvetica, Arial, sans-serif">
  <defs><marker id="a5" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="#2f3f8f"/></marker></defs>
  <text x="320" y="26" text-anchor="middle" font-size="16" font-weight="700" fill="#222">増殖の両輪：アクセルとブレーキ</text>
  <rect x="30" y="50" width="250" height="210" rx="12" fill="#eef2fb" stroke="#2f3f8f" stroke-width="1.3"/>
  <text x="155" y="74" text-anchor="middle" font-size="13" font-weight="700" fill="#2f3f8f">アクセル（踏み続ける）</text>
  <rect x="60" y="92" width="190" height="30" rx="6" fill="#fff" stroke="#2f3f8f"/>
  <text x="155" y="112" text-anchor="middle" font-size="11.5" fill="#2f3f8f">MAPK：RAS→RAF→MEK→ERK</text>
  <rect x="60" y="132" width="190" height="30" rx="6" fill="#fff" stroke="#2f3f8f"/>
  <text x="155" y="152" text-anchor="middle" font-size="11.5" fill="#2f3f8f">PI3K→AKT→mTOR</text>
  <text x="155" y="190" text-anchor="middle" font-size="11" fill="#666">KRAS / BRAF / EGFR / PIK3CA</text>
  <text x="155" y="226" text-anchor="middle" font-size="11" fill="#1f5d39">→ 阻害薬で止めやすい</text>
  <rect x="360" y="50" width="250" height="210" rx="12" fill="#fdecea" stroke="#c0392b" stroke-width="1.3"/>
  <text x="485" y="74" text-anchor="middle" font-size="13" font-weight="700" fill="#a5281b">ブレーキ（壊して無視）</text>
  <rect x="390" y="92" width="190" height="30" rx="6" fill="#fff" stroke="#c0392b"/>
  <text x="485" y="112" text-anchor="middle" font-size="11.5" fill="#a5281b">Rb：G1/S を直接止める門番</text>
  <rect x="390" y="132" width="190" height="30" rx="6" fill="#fff" stroke="#c0392b"/>
  <text x="485" y="152" text-anchor="middle" font-size="11.5" fill="#a5281b">p53：止める・直す・殺す統括</text>
  <text x="485" y="190" text-anchor="middle" font-size="11" fill="#666">RB1 / TP53 / PTEN</text>
  <text x="485" y="226" text-anchor="middle" font-size="11" fill="#a5281b">→ 機能喪失。狙いにくい</text>
</svg>
<div class="caption">独自作図。増殖は「アクセルの踏みすぎ」と「ブレーキの故障」の両面で進む。</div>
</div>

<div class="note">
<strong>この日の要点（後ろへのつながり）</strong><br>
・増殖は<strong>アクセル過剰（MAPK・PI3K）＋ブレーキ故障（Rb・p53）</strong>の両輪で進む。<br>
・この2経路と2番人に、フェーズ2の主力遺伝子が集中する。<br>
・次の Day 6 は「増えた細胞が死なない・無限に増える」能力へ。
</div>
""")

# ------------------------------------------------------------------ Day 6
add(6, "hallmark-cell-death",
    "Day 6：Hallmark｜細胞死への抵抗性／複製の不死化",
    '<span class="tag hall">Hallmark</span> <span class="tag brake">アポトーシス制御</span>',
    """
<div class="pos">
<strong>全体マップの中での位置づけ</strong><br>
Day 1 で触れたアポトーシス（自殺プログラム）と、細胞の分裂回数の限界の話を、Hallmarkとして掘り下げる。増殖を止められない（Day 5）だけでなく、<strong>死なない・無限に増える</strong>能力がそろうと、がん細胞は実質的に不滅に近づく。
</div>

<h2>① 細胞死への抵抗性 ── BCL-2系という綱引き</h2>
<p>アポトーシスは、細胞内のシグナル（内因性経路）と外からの死の指令（外因性経路）の2系統で起こる。中でも内因性の要が <strong>BCL-2ファミリー</strong>。このファミリーには<strong>アポトーシスを進める係（促進側）</strong>と<strong>止める係（抑制側）</strong>がいて、両者の綱引きで生死が決まる。がん細胞は<strong>抑制側（BCL-2など）を増やす／促進側を抑える</strong>ことで、死の指令が来ても死なずに済む。これが「細胞死への抵抗性」。抗がん剤や放射線の多くは「アポトーシスを起こさせて殺す」ので、ここが壊れていると<strong>治療抵抗性</strong>にも直結する。</p>

<h2>② 複製の不死化 ── テロメアとテロメラーゼ</h2>
<p>正常細胞は分裂のたびに染色体の末端<strong>テロメア</strong>が少しずつ短くなり、限界まで縮むと分裂を止める（老化）。これは「無限に増えない」ための安全装置。がん細胞は<strong>テロメラーゼ（TERT）</strong>という酵素を再び働かせてテロメアを延ばし続け、この回数券の制限を踏み倒す。結果、<strong>無限に分裂できる</strong>ようになる。</p>

<div class="fig">
<svg viewBox="0 0 600 230" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, Helvetica, Arial, sans-serif">
  <text x="300" y="26" text-anchor="middle" font-size="16" font-weight="700" fill="#222">死なない・無限に増える</text>
  <rect x="30" y="48" width="260" height="150" rx="12" fill="#e9f6ee" stroke="#2e7d4f" stroke-width="1.3"/>
  <text x="160" y="72" text-anchor="middle" font-size="13" font-weight="700" fill="#1f5d39">BCL-2系の綱引き</text>
  <text x="160" y="100" text-anchor="middle" font-size="11.5" fill="#333">促進側 ⇄ 抑制側</text>
  <text x="160" y="124" text-anchor="middle" font-size="11.5" fill="#333">がん：抑制側を増やす</text>
  <text x="160" y="148" text-anchor="middle" font-size="11.5" fill="#a5281b">→ 死の指令が来ても死なない</text>
  <text x="160" y="178" text-anchor="middle" font-size="11" fill="#666">＝治療抵抗性にも直結</text>
  <rect x="310" y="48" width="260" height="150" rx="12" fill="#eef2fb" stroke="#2f3f8f" stroke-width="1.3"/>
  <text x="440" y="72" text-anchor="middle" font-size="13" font-weight="700" fill="#2f3f8f">テロメア／TERT</text>
  <text x="440" y="100" text-anchor="middle" font-size="11.5" fill="#333">正常：分裂ごとに短縮→老化</text>
  <text x="440" y="124" text-anchor="middle" font-size="11.5" fill="#333">がん：テロメラーゼ再活性化</text>
  <text x="440" y="148" text-anchor="middle" font-size="11.5" fill="#2f3f8f">→ 回数券の制限を踏み倒す</text>
  <text x="440" y="178" text-anchor="middle" font-size="11" fill="#666">＝無限に分裂</text>
</svg>
<div class="caption">独自作図。死なない仕組み（左）と、増え続ける仕組み（右）。</div>
</div>

<div class="note">
<strong>この日の要点（後ろへのつながり）</strong><br>
・細胞死への抵抗性＝<strong>BCL-2系の綱引きを抑制側に傾ける</strong>。治療抵抗性にもつながる。<br>
・複製の不死化＝<strong>テロメラーゼ（TERT）でテロメアを延ばし、分裂回数の限界を踏み倒す</strong>。<br>
・次の Day 7 は、増えた腫瘍が「広がる」ための能力（血管新生・浸潤転移）へ。
</div>
""")

# ------------------------------------------------------------------ Day 7
add(7, "hallmark-angiogenesis-metastasis",
    "Day 7：Hallmark｜血管新生の誘導／浸潤と転移",
    '<span class="tag hall">Hallmark</span> <span class="tag gas">VEGF・HIF</span> <span class="tag gas">EMT・Wnt</span>',
    """
<div class="pos">
<strong>全体マップの中での位置づけ</strong><br>
ここまでは「1個の細胞が増え続ける」話。今日は腫瘍が塊として<strong>大きくなり、広がる</strong>ための能力を扱う。臨床的な悪性度（転移）に直結する領域で、抗血管新生薬の土台にもなる。
</div>

<h2>① 血管新生の誘導 ── 自前の補給線を引く</h2>
<p>腫瘍が一定以上大きくなると、内部が酸素・栄養不足になる。低酸素を感知する <strong>HIF</strong> というセンサーが働き、<strong>VEGF</strong> という「血管を伸ばせ」の信号を出させる。これで腫瘍は<strong>自分専用の血管を引き込み</strong>、補給線を確保して成長を続ける。VEGFを狙う抗血管新生薬（補給線を断つ発想）はこの仕組みに対応する。</p>

<h2>② 浸潤と転移 ── 仕切りを壊して遠くへ</h2>
<p>がん細胞は本来の場所にとどまらず、周囲の組織に侵入（浸潤）し、血流やリンパに乗って遠くの臓器へ移動して住み着く（転移）。鍵になる現象が <strong>EMT（上皮間葉転換）</strong>：きっちり並んで動かない上皮細胞が、ばらけて動き回れる間葉系の性質に切り替わる。この切り替えには <strong>Wnt経路</strong> などが関わる。転移はがんの予後を最も大きく左右する段階。</p>

<div class="fig">
<svg viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system, Helvetica, Arial, sans-serif">
  <defs><marker id="a7" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="#2c6e8f"/></marker></defs>
  <text x="300" y="26" text-anchor="middle" font-size="16" font-weight="700" fill="#222">大きくなる／広がる</text>
  <rect x="30" y="50" width="250" height="140" rx="12" fill="#eef2fb" stroke="#2f3f8f" stroke-width="1.3"/>
  <text x="155" y="74" text-anchor="middle" font-size="13" font-weight="700" fill="#2f3f8f">血管新生</text>
  <text x="155" y="100" text-anchor="middle" font-size="11.5" fill="#333">低酸素 → HIF が感知</text>
  <text x="155" y="124" text-anchor="middle" font-size="11.5" fill="#333">→ VEGF「血管を伸ばせ」</text>
  <text x="155" y="148" text-anchor="middle" font-size="11.5" fill="#2f3f8f">→ 自前の補給線を確保</text>
  <text x="155" y="174" text-anchor="middle" font-size="11" fill="#666">抗VEGF薬で補給線を断つ</text>
  <rect x="320" y="50" width="250" height="140" rx="12" fill="#e9f6ee" stroke="#2e7d4f" stroke-width="1.3"/>
  <text x="445" y="74" text-anchor="middle" font-size="13" font-weight="700" fill="#1f5d39">浸潤・転移</text>
  <text x="445" y="100" text-anchor="middle" font-size="11.5" fill="#333">EMT：上皮 → 動ける間葉系へ</text>
  <text x="445" y="124" text-anchor="middle" font-size="11.5" fill="#333">Wnt 経路などが関与</text>
  <text x="445" y="148" text-anchor="middle" font-size="11.5" fill="#1f5d39">→ 遠くの臓器へ移動・定着</text>
  <text x="445" y="174" text-anchor="middle" font-size="11" fill="#666">予後を最も左右する段階</text>
</svg>
<div class="caption">独自作図。栄養を引き込む力（左）と、広がる力（右）。</div>
</div>

<div class="note">
<strong>この日の要点（後ろへのつながり）</strong><br>
・血管新生＝<strong>低酸素→HIF→VEGF</strong> で自前の補給線を引く。抗血管新生薬の標的。<br>
・浸潤・転移＝<strong>EMT</strong> で動ける性質に切り替わり遠くへ。Wnt 等が関与。<br>
・次の Day 8 は、これらの能力を生み出す土台＝<strong>ゲノム不安定性</strong>へ。
</div>
""")

# ------------------------------------------------------------------ Day 8
add(8, "hallmark-genome-instability",
    "Day 8：Hallmark｜ゲノム不安定性／変異",
    '<span class="tag hall">土台的特性</span> <span class="tag brake">DNA損傷応答・BRCA</span>',
    """
<div class="pos">
<strong>全体マップの中での位置づけ</strong><br>
他のHallmarksを<strong>生み出す土台</strong>にあたる特性。変異が起きやすい状態（ゲノム不安定性）があるからこそ、アクセル変異やブレーキ故障が次々生まれる。フェーズ2後半のDNA修復系（BRCA・ATM・ミスマッチ修復／Day 21–23）に直結し、PARP阻害薬や免疫療法の効きどころの理解につながる、実務的に重要な回。
</div>

<h2>① なぜ「土台」なのか</h2>
<p>がん化には複数の遺伝子変異の蓄積が要る。ところが正常細胞は変異が起きにくいよう厳重に守られている。そこでがん細胞は、まず<strong>DNAの傷を直す仕組みそのものを壊す</strong>。すると変異率が跳ね上がり、他のHallmarkに必要な変異が次々手に入る。これがゲノム不安定性が「能力を生む能力」と呼ばれる理由（Day 3 の<strong>管理人＝caretaker</strong>の故障）。</p>

<h2>② DNA損傷応答と修復の種類</h2>
<p>細胞には傷の種類別に複数の修復システムがある。レポートで頻出するのは2つ：</p>
<ul>
  <li><strong>相同組換え修復（HR）</strong>：DNAの両側が切れる重大な傷（二本鎖切断）を、正確に直す高精度システム。中心選手が <strong>BRCA1/2（Day 21）</strong>・<strong>ATM（Day 22）</strong>。ここが壊れた状態を <strong>HRD（相同組換え修復欠損）</strong> と呼ぶ。</li>
  <li><strong>ミスマッチ修復（MMR）</strong>：複製時の「打ち間違い」を直す校正係。<strong>MLH1・MSH2 など（Day 23）</strong>。壊れると小さな反復配列がズレやすくなり <strong>MSI-High（高頻度マイクロサテライト不安定性）</strong> になる。</li>
</ul>

<h2>③ 修復破綻が治療に直結する</h2>
<p>修復の壊れ方は、そのまま薬の効きどころになる。<strong>HRD（BRCA変異など）→ PARP阻害薬</strong>（合成致死／Day 21 で詳説）、<strong>MSI-High → 免疫チェックポイント阻害薬</strong>（変異が多い腫瘍ほど免疫に見つかりやすい／Day 9・23）。修復破綻は「弱点」でもあり、そこを突くのが現代の治療戦略。<strong>TMB（腫瘍遺伝子変異量）</strong>もこの文脈の指標で、パネル検査の出力に出てくる。</p>

<div class="note">
<strong>この日の要点（後ろへのつながり）</strong><br>
・ゲノム不安定性＝<strong>修復を壊して変異率を上げ、他の能力を獲得しやすくする土台</strong>（管理人の故障）。<br>
・頻出は <strong>HR（BRCA・ATM）→ HRD</strong> と <strong>MMR（MLH1/MSH2）→ MSI-High</strong>。<br>
・破綻は弱点＝<strong>HRD→PARP阻害薬／MSI-High→免疫療法</strong>。Day 21–23 へ直結。<br>
・次の Day 9 は、変異が増えた腫瘍が免疫の目をどうかわすか（免疫逃避）。
</div>
""")

# ------------------------------------------------------------------ Day 9
add(9, "hallmark-immune-evasion",
    "Day 9：Hallmark｜免疫からの逃避",
    '<span class="tag hall">Hallmark</span> <span class="tag gas">PD-1 / PD-L1</span>',
    """
<div class="pos">
<strong>全体マップの中での位置づけ</strong><br>
免疫療法（免疫チェックポイント阻害薬）の土台になる回。Day 8 の変異の多さ（MSI-High・TMB）が、ここで「免疫に見つかりやすさ」として効いてくる。分子標的薬とは別系統の治療軸なので、レポートでの意味づけも独立して押さえる。
</div>

<h2>① 免疫の「ブレーキ」をがんが悪用する</h2>
<p>体の免疫（特にT細胞）は、異常な細胞を見つけて攻撃する。暴走を防ぐため、T細胞には<strong>「攻撃をやめる」ブレーキ＝免疫チェックポイント</strong>が備わっている。代表が <strong>PD-1</strong>（T細胞側）と <strong>PD-L1</strong>（相手側）。がん細胞は表面に PD-L1 を掲げてこのブレーキを押し、T細胞に「攻撃するな」と信号を送って<strong>免疫の攻撃をかわす</strong>。</p>

<h2>② 免疫チェックポイント阻害薬 ── ブレーキ解除</h2>
<p>そこで、PD-1とPD-L1の握手を薬で邪魔して<strong>ブレーキを解除し、T細胞の攻撃力を取り戻す</strong>のが免疫チェックポイント阻害薬。狙うのはがん細胞そのものではなく<strong>免疫の側</strong>という点が、分子標的薬と決定的に違う。</p>

<h2>③ どんな腫瘍に効きやすいか（Day 8 とつながる）</h2>
<p>変異が多い腫瘍ほど、免疫から見て「異物らしい目印（ネオアンチゲン）」が多く、攻撃の的になりやすい。だから <strong>MSI-High</strong> や <strong>TMB-High</strong>（Day 8）はチェックポイント阻害薬が効きやすいバイオマーカーになる。<strong>臓器を問わず</strong>これらの指標で適応が決まる例があり、Day 29 の tumor-agnostic（臓器横断的）治療の考え方にもつながる。</p>

<div class="note">
<strong>この日の要点（後ろへのつながり）</strong><br>
・がんは <strong>PD-L1</strong> を掲げて T細胞のブレーキ（<strong>PD-1</strong>）を押し、攻撃をかわす。<br>
・<strong>免疫チェックポイント阻害薬＝ブレーキ解除</strong>。標的は「がん」ではなく「免疫の側」。<br>
・効きやすい目印は <strong>MSI-High／TMB-High</strong>（Day 8 と連結）。<br>
・次の Day 10 で 10項目を統合・復習し、骨格を固める。
</div>
""")

# ------------------------------------------------------------------ Day 10
add(10, "hallmarks-integration",
    "Day 10：Hallmarks 統合・復習",
    '<span class="tag hall">骨格の固定化</span>',
    """
<div class="pos">
<strong>全体マップの中での位置づけ</strong><br>
フェーズ1の山場の締め。Day 4–9 で1つずつ見た能力を一望し、<strong>各Hallmarkに代表経路・遺伝子を即答できる</strong>状態にする。ここが固まると、フェーズ2は「この遺伝子はどのフォルダ？」と振り分けるだけの作業になる。
</div>

<h2>① 10項目 ↔ 代表経路・遺伝子 早見表</h2>
<table class="toc">
  <tr><th>Hallmark（能力）</th><th>代表経路</th><th>頻出遺伝子</th><th>系統</th></tr>
  <tr><td>増殖シグナルの維持</td><td>MAPK / PI3K</td><td>KRAS・BRAF・EGFR・PIK3CA</td><td>アクセル</td></tr>
  <tr><td>増殖抑制の回避</td><td>Rb・p53 関所</td><td>RB1・TP53・PTEN</td><td>ブレーキ</td></tr>
  <tr><td>細胞死への抵抗性</td><td>BCL-2 系</td><td>（BCL-2 等）</td><td>—</td></tr>
  <tr><td>複製の不死化</td><td>テロメラーゼ</td><td>TERT</td><td>—</td></tr>
  <tr><td>血管新生の誘導</td><td>HIF / VEGF</td><td>VEGF（VHL 等）</td><td>—</td></tr>
  <tr><td>浸潤と転移</td><td>EMT / Wnt</td><td>（APC・CTNNB1 等）</td><td>混在</td></tr>
  <tr><td>ゲノム不安定性</td><td>DNA 修復（HR・MMR）</td><td>BRCA1/2・ATM・MLH1/MSH2</td><td>ブレーキ（管理人）</td></tr>
  <tr><td>免疫からの逃避</td><td>PD-1 / PD-L1</td><td>（MSI・TMB が指標）</td><td>—</td></tr>
</table>

<h2>② 2問フレームで総点検</h2>
<p>任意の遺伝子について、<strong>①どのHallmarkに効く？ ②アクセルかブレーキか？</strong> を即答できるか試す。例：BRCA1 → ゲノム不安定性／ブレーキ（管理人）。KRAS → 増殖シグナルの維持／アクセル。TP53 → 増殖抑制の回避＋ゲノム不安定性／ブレーキ。この2問が反射になれば骨格は完成。</p>

<div class="note">
<strong>この日の要点（後ろへのつながり）</strong><br>
・早見表の<strong>「能力 ↔ 経路 ↔ 遺伝子」</strong>を一望できる状態がゴール。<br>
・<strong>2問フレーム（Hallmark／アクセル・ブレーキ）</strong>が反射になればフェーズ2は振り分け作業。<br>
・次の Day 11–12 で、知識を<strong>実務（制度・レポート・エビデンス）</strong>に接続する。
</div>
""")

# ------------------------------------------------------------------ Day 11
add(11, "system-report-flow",
    "Day 11：制度とレポートの流れ",
    '<span class="tag hall">実務文脈の接続</span>',
    """
<div class="pos">
<strong>全体マップの中での位置づけ</strong><br>
ここから2日は、生物学の知識を<strong>実際の検査・レポートの文脈</strong>に接続する。エキスパートパネルが何を議論する場なのか、レポートがどう作られ流れるのかを押さえると、フェーズ2の「変異→薬」の知識が実務の地図の上に乗る。
</div>

<h2>① がん遺伝子パネル検査の流れ</h2>
<p>日本の保険診療では、おおむね次の流れ。<strong>検体採取（がん組織または血液）→ 次世代シークエンサーで多数の遺伝子を一括解析 → 結果を C-CAT に登録 → エキスパートパネルで検討 → 主治医から患者へ結果説明</strong>。検査申し込みから結果説明まで数週間かかる。多くの場合、<strong>標準治療が無い／終わった段階</strong>で次の選択肢を探すために使われる（包括的がんゲノムプロファイリング検査の主用途）。</p>

<h2>② C-CAT とエキスパートパネル</h2>
<p><strong>C-CAT（がんゲノム情報管理センター）</strong>は、全国の検査結果と臨床情報を集約・保管する国の基盤。登録された情報は本人の治療に役立つだけでなく、匿名化のうえ研究にも活用される。<strong>エキスパートパネル</strong>は、臨床医・病理医・分子遺伝学者・バイオインフォマティシャンなど多職種が集まり、<strong>検出された変異それぞれに臨床的な意味があるか（actionability）を議論して、推奨をまとめる会議</strong>。レポートはこの議論の土台であり結論の記録でもある。</p>

<h2>③ レポートに含まれる主な要素</h2>
<ul>
  <li><strong>検出された変異（バリアント）</strong>：遺伝子名・変異の種類・表記（例：BRAF V600E）。</li>
  <li><strong>その意味づけ</strong>：対応する薬・治験があるか、エビデンスの強さ（Day 12）。</li>
  <li><strong>付随する指標</strong>：MSI、TMB（Day 8–9 の免疫療法の手がかり）。</li>
  <li><strong>二次的所見</strong>：遺伝性腫瘍に関わる生殖細胞系列の所見など（開示の扱いは別途配慮）。</li>
</ul>

<div class="note">
<strong>この日の要点（後ろへのつながり）</strong><br>
・流れ＝<strong>検体→シーケンス→C-CAT登録→エキスパートパネル→結果説明</strong>。<br>
・エキスパートパネルは<strong>各変異の actionability を多職種で議論する会議</strong>。<br>
・レポートは<strong>変異・意味づけ・指標（MSI/TMB）・二次的所見</strong>から成る。<br>
・次の Day 12 で、パネルごとの違いと<strong>エビデンスレベル</strong>を詳しく見る。
</div>
""")

# ------------------------------------------------------------------ Day 12
add(12, "panels-evidence-levels",
    "Day 12：パネルの違い・エビデンスレベル",
    '<span class="tag hall">レポート読解の鍵</span>',
    """
<div class="pos">
<strong>全体マップの中での位置づけ</strong><br>
フェーズ1の最終日。レポートの「同じ変異でも意味づけが違う」を支える<strong>エビデンスレベル</strong>と、検査の土台である<strong>パネルの違い</strong>を押さえる。ここがフェーズ2（各遺伝子の薬・エビデンス）を読む直接の足場になる。
</div>

<h2>① 保険収載されている主なパネル</h2>
<p>2025年時点で保険診療で使えるパネルは複数あり、<strong>組織を使うもの</strong>と<strong>血液（リキッド）を使うもの</strong>に分かれる。代表例：</p>
<ul>
  <li><strong>OncoGuide NCC オンコパネル</strong>：国内開発。組織＋血液のペア解析。約124遺伝子。MSI・TMBも算出。</li>
  <li><strong>GenMineTOP</strong>：組織＋血液のペア解析。DNA・RNA両パネルで、RNAにより<strong>融合遺伝子</strong>の検出に強い。対象遺伝子数が多い。</li>
  <li><strong>FoundationOne CDx</strong>：組織。約324遺伝子。コンパニオン診断（特定薬の適否判定）も兼ねる。</li>
  <li><strong>FoundationOne Liquid CDx</strong>：血液（リキッド）。組織が採れない場合に有用。</li>
  <li><strong>Guardant360 CDx</strong>：血液（リキッド）。採血のみで実施。</li>
</ul>
<p>違いの勘所は<strong>検体（組織／血液）・遺伝子数・融合やMSI/TMBの検出可否・遺伝性腫瘍の評価可否</strong>。どのパネルかで「何が分かるか／分からないか」が変わるので、レポートを読む前提として把握しておく。</p>

<h2>② エビデンスレベル ── 同じ変異でも意味づけが変わる</h2>
<p>検出された変異に<strong>どれだけ確かな治療的根拠があるか</strong>を段階で示すのがエビデンスレベル。日本では3学会合同の「遺伝子パネル検査に基づくがん診療ガイダンス」が、おおむね <strong>A〜F</strong> の段階で分類している（大枠）：</p>
<ul>
  <li><strong>A</strong>：当該がん種で、その変異に対する薬が承認済み（最も強い根拠）。</li>
  <li><strong>B</strong>：当該がん種で、専門家コンセンサスや確立した知見で推奨される。</li>
  <li><strong>C</strong>：別のがん種では承認/ガイドライン記載があり、当該がん種では臨床試験段階。</li>
  <li><strong>D〜F</strong>：根拠がより限定的（小規模試験・症例報告・前臨床など）になるほど下位。</li>
</ul>
<p>※区分の文言・運用はガイダンスの版によって更新される。重要なのは細かい字面より<strong>「強い根拠（承認薬あり）から、弱い根拠（治験・前臨床）まで連続している」という考え方</strong>。Day 13 で見た「同じTP53でも変異により意味づけが変わる」は、まさにこのレベルの違い。</p>

<h2>③ なぜこれがレポート読解の鍵か</h2>
<p>エキスパートパネルの議論は突き詰めると<strong>「検出された各変異を、エビデンスレベルの軸でどう評価し、次の一手につなげるか」</strong>。フェーズ2で各遺伝子の薬を学ぶとき、<strong>その薬が「どのがん種で、どのレベルか」をセットで意識する</strong>と、知識が実務の判断にそのまま使える形になる。</p>

<div class="note">
<strong>この日の要点（後ろへのつながり）</strong><br>
・パネルは<strong>検体・遺伝子数・融合/MSI/TMBの検出可否</strong>で性格が違う。<br>
・エビデンスレベル＝<strong>治療的根拠の強さの段階（A〜F、承認薬ありが最上位）</strong>。版で更新される。<br>
・<strong>同じ変異でも、がん種とレベルで意味づけが変わる</strong>。これがレポート読解の核心。<br>
・ここでフェーズ1は完了。次の Day 13（TP53）からフェーズ2＝頻出ドライバー遺伝子に入る。
</div>
""")

# ====================================================================
# テンプレート組み立てと書き出し
# ====================================================================

PAGES.sort(key=lambda x: x[0])
by_day = {p[0]: p for p in PAGES}

def filename(day):
    if day in NEXT_OVERRIDE:  # 12 -> day-13...
        pass
    p = by_day.get(day)
    if p:
        return f"day-{day}-{p[1]}.html"
    return None

def nav_html(day):
    # Back
    prev_day = day - 1
    prev_file = filename(prev_day)
    if prev_file:
        prev_title = by_day[prev_day][2]
        prev_title = prev_title.split("：", 1)[-1]
        back = f'<a class="back" href="{prev_file}"><span class="navlabel">← 前へ</span><span class="navtitle">Day {prev_day}：{prev_title}</span></a>'
    else:
        back = '<a class="back toindex" href="../index.html"><span class="navlabel">&nbsp;</span><span class="navtitle">目次</span></a>'
    # Next
    next_day = day + 1
    if day in NEXT_OVERRIDE:
        next_file = NEXT_OVERRIDE[day]
        next_label = "Day 13：TP53"
        nxt = f'<a class="next" href="{next_file}"><span class="navlabel">次へ →</span><span class="navtitle">{next_label}</span></a>'
    else:
        next_file = filename(next_day)
        if next_file:
            next_title = by_day[next_day][2].split("：", 1)[-1]
            nxt = f'<a class="next" href="{next_file}"><span class="navlabel">次へ →</span><span class="navtitle">Day {next_day}：{next_title}</span></a>'
        else:
            nxt = '<span class="disabled next"><span class="navlabel">次へ →</span><span class="navtitle">（未作成）</span></span>'
    return f'<nav class="daynav">{back}{nxt}</nav>'

TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{h1} | がんゲノム学習ノート</title>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header class="site"><a class="home" href="../index.html">← 目次にもどる</a></header>

<h1>{h1}</h1>
<p>{tags}</p>
{body}
{nav}
<footer class="site">がんゲノム学習ノート — Day {day}</footer>
</body>
</html>
"""

for day, slug, h1, tags, body in PAGES:
    html = TEMPLATE.format(h1=h1, tags=tags, body=body.strip(), nav=nav_html(day), day=day)
    out = DAYS / f"day-{day}-{slug}.html"
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out.name}")

print("done.")
