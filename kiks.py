import streamlit as st
import random

# 1. ページ設定
st.set_page_config(page_title="北神総合 系列選択ナビ", page_icon="🎓", layout="centered")

# --- データ定義 (既存の文言・ロジックは一切変更なし) ---
DESCRIPTIONS = {
    "宇宙気象系列": "めざせ宇宙！守れ地球！の理数学習を進める。宇宙・気象への興味関心を高め、人類が今後目指すことになる宇宙に関連した産業や、地球の気候をふまえた暮らしや産業をリードする人材を育成する。",
    "DX系列": "ＡＩやＩｏＴを始めとするデジタル技術を活用して、産業社会における製品やサービス、ビジネスモデルそのものを変革する等、新たな価値を創造する人材を育成する。",
    "兵庫からスタートアップ系列": "豊かな観光資源に恵まれた兵庫の魅力について学び、それを生かした仕事の創出やまちおこし、観光ビジネスに力を発揮できる、アントレプレナーシップを有する人材を育成する。",
    "スポーツアウトドアと防災系列": "スポーツやアウトドアアクティビティといった活動と、防災活動、ボランティア活動、スポーツビジネスといった人間の社会生活を結びつけ、新たな価値や生きがいを創出することのできる人材を育成する。",
    "ダイバーシティー&インクルージョン系列": "文化や年齢・様々な特性等を超えて、多様な人々と関わり理解し合うための学びを通じて、互いを認め合い生かし合えるグローバルなビジネスや文化、共生社会の担い手となる人材を育成する。",
    "リベラルアーツ理系系列": "普通科の教育課程に準じた科目配置に加えて、芸術系の科目や「キャリア探究」を設置し、複雑化する社会の諸問題に対して様々な視点を持ち、自分らしく生きるための基本となる教養を身に付ける。",
    "リベラルアーツ文系系列": "普通科の教育課程に準じた科目配置に加えて、芸術系の科目や「キャリア探究」を設置し、複雑化する社会の諸問題に対して様々な視点を持ち、自分らしく生きるための基本となる教養を身に付ける。"
}

# 追加機能：向いているキーワード
KEYWORDS = {
    "宇宙気象系列": ["宇宙開発", "環境保護", "気象観測", "理数探究"],
    "DX系列": ["プログラミング", "AI活用", "ビジネス変革", "論理的思考"],
    "兵庫からスタートアップ系列": ["地域創生", "起業家精神", "観光ビジネス", "企画力"],
    "スポーツアウトドアと防災系列": ["リーダーシップ", "野外活動", "地域防災", "健康科学"],
    "ダイバーシティー&インクルージョン系列": ["国際理解", "共生社会", "多様性", "コミュニケーション"],
    "リベラルアーツ理系系列": ["幅広い教養", "芸術的感性", "キャリア探究", "理系基礎"],
    "リベラルアーツ文系系列": ["多角的視点", "文化・芸術", "自己探究", "文系基礎"]
}

# --- セッション状態の初期化 ---
if 'step' not in st.session_state:
    st.session_state.step = 'start'
if 'result' not in st.session_state:
    st.session_state.result = ""
if 'history_steps' not in st.session_state:
    st.session_state.history_steps = ['start']  # 戻る機能用の遷移履歴
if 'diagnosis_history' not in st.session_state:
    st.session_state.diagnosis_history = []  # 診断結果履歴

# --- 関数定義 ---
def move_to(next_step):
    """次のステップへ進む（履歴に保存）"""
    st.session_state.history_steps.append(next_step)
    st.session_state.step = next_step

def go_back():
    """一つ前のステップに戻る"""
    if len(st.session_state.history_steps) > 1:
        st.session_state.history_steps.pop()  # 現在のステップを削除
        st.session_state.step = st.session_state.history_steps[-1] # 一つ前に戻る

def reset_app():
    """アプリを初期化"""
    st.session_state.step = 'start'
    st.session_state.result = ""
    st.session_state.history_steps = ['start']

def save_diagnosis(res):
    """診断結果を履歴に保存（重複回避）"""
    if not st.session_state.diagnosis_history or st.session_state.diagnosis_history[-1] != res:
        st.session_state.diagnosis_history.append(res)

# --- サイドバー ---
with st.sidebar:
    st.title("🔗 リンク・情報")
    st.info("このアプリは新入生が自分の興味・関心に合わせて系列を考えるためのガイドです。")
    
    # 追加機能：診断履歴
    st.divider()
    st.subheader("📜 診断履歴")
    if st.session_state.diagnosis_history:
        for idx, item in enumerate(reversed(st.session_state.diagnosis_history)):
            st.write(f"{len(st.session_state.diagnosis_history)-idx}. {item}")
    else:
        st.caption("履歴はまだありません")

    st.divider()
    st.write("📖 **学校公式リンク**")
    st.markdown("- [北神戸総合高校 HP](https://dmzcms.hyogo-c.ed.jp/kitakobesogo-hs/NC3/)")
    st.markdown("- [学校案内パンフレット](https://dmzcms.hyogo-c.ed.jp/kitakobesogo-hs/NC3/wysiwyg/file/download/1/151)")
    # ... インスタリンクは既存コード通り (省略せず表示)
    st.markdown("- [KIKS男子ソフトテニスインスタグラム](https://www.instagram.com/kiks_soft.tennis_club01/)")
    st.markdown("- [KIKS女子ソフトテニスインスタグラム](https://www.instagram.com/kiks1__soft_tennis/)")
    st.markdown("- [KIKS卓球部インスタグラム](https://www.instagram.com/kiks_ttc/)")
    st.markdown("- [KIKS陸上競技部一期生インスタグラム](https://www.instagram.com/kiks._.tf1/)")
    st.markdown("- [KIKS陸上競技部二期生インスタグラム](https://www.instagram.com/kiksss2_tf/?hl=ja)")
    st.markdown("- [KIKS写真部インスタグラム](https://www.instagram.com/kikssyashinbu/)")
    st.markdown("- [KIKS放送部インスタグラム](https://www.instagram.com/kiks_hbc_official/)")
    st.divider()
    
    if st.button("🔄 アプリをリセット", use_container_width=True):
        reset_app()
        st.rerun()

# --- メイン画面 ---
st.title("🎓 新入生のための系列選択ナビ")

# プログレスバー
steps_map = {'IE': 20, 'YES': 40, 'rikei': 70, 'bunnkei': 70, 'tinomanabi': 90, 'zinnnomanabi': 90, 'goal': 100}
if st.session_state.step in steps_map:
    progress = steps_map[st.session_state.step]
    st.progress(progress / 100)
    st.caption(f"診断の進み具合: {progress}%")

# --- 各画面の出し分け ---

# 1. スタート画面
if st.session_state.step == 'start':
    st.subheader("北神戸総合高校へようこそ！")
    st.write("あなたの未来をデザインする「系列選択」をお手伝いします。")
    
    # 追加機能：学校生活ヒント
    st.success(f"💡 **新入生へのヒント**\n{random.choice(SCHOOL_TIPS)}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("診断を始める", use_container_width=True, type="primary"):
            move_to('IE')
            st.rerun()
    with col2:
        if st.button("系列（天・地・人）の説明を見る", use_container_width=True):
            move_to('NO')
            st.rerun()

# 2. 系列解説トップ
elif st.session_state.step == 'NO':
    st.subheader('KIKS系列体系「天・地・人」')
    st.write("本校の学びは、大きく3つの視点に分かれています。解説を選んでください。")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✨ 天の学び", use_container_width=True): move_to('tennkaisetu'); st.rerun()
    with col2:
        if st.button("🌍 地の学び", use_container_width=True): move_to('tikaisetu'); st.rerun()
    with col3:
        if st.button("🤝 人の学び", use_container_width=True): move_to('zinnkaisetu'); st.rerun()

# --- 解説詳細（ロジック維持） ---
elif st.session_state.step == 'tennkaisetu':
    st.subheader('✨ 天の学び')
    col1, col2 = st.columns(2)
    with col1:
        if st.button("宇宙・気象系列"): move_to('utyuukaisetu'); st.rerun()
    with col2:
        if st.button("DX系列"): move_to('DXkaisetu'); st.rerun()

elif st.session_state.step == 'utyuukaisetu':
    st.info(f"### 宇宙・気象系列\n{DESCRIPTIONS['宇宙気象系列']}")
    if st.button("一覧に戻る"): go_back(); st.rerun()

elif st.session_state.step == 'DXkaisetu':
    st.info(f"### DX系列\n{DESCRIPTIONS['DX系列']}")
    if st.button("一覧に戻る"): go_back(); st.rerun()

elif st.session_state.step == 'tikaisetu':
    st.subheader('🌍 地の学び')
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ひょうごからスタートアップ系列"): move_to('hyogokaisetu'); st.rerun()
    with col2:
        if st.button("スポーツ・アウトドアと防災系列"): move_to('autodoakaisetu'); st.rerun()

elif st.session_state.step == 'hyogokaisetu':
    st.success(f"### 兵庫からスタートアップ系列\n{DESCRIPTIONS['兵庫からスタートアップ系列']}")
    if st.button("一覧に戻る"): go_back(); st.rerun()

elif st.session_state.step == 'autodoakaisetu':
    st.success(f"### スポーツ・アウトドアと防災系列\n{DESCRIPTIONS['スポーツアウトドアと防災系列']}")
    if st.button("一覧に戻る"): go_back(); st.rerun()

elif st.session_state.step == 'zinnkaisetu':
    st.subheader('🤝 人の学び')
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ダイバーシティ＆インクルージョン系列"): move_to('daibakaisetu'); st.rerun()
    with col2:
        if st.button("リベラルアーツ系列"): move_to('riberikaisetu'); st.rerun()

elif st.session_state.step == 'daibakaisetu':
    st.warning(f"### ダイバーシティ系列＆インクルージョン系列\n{DESCRIPTIONS['ダイバーシティー&インクルージョン系列']}")
    if st.button("一覧に戻る"): go_back(); st.rerun()

elif st.session_state.step == 'riberikaisetu':
    st.warning(f"### リベラルアーツ系列\n{DESCRIPTIONS['リベラルアーツ文系系列']}")
    if st.button("一覧に戻る"): go_back(); st.rerun()

# --- 診断ロジック（ロジック維持＋機能追加） ---
elif st.session_state.step == 'IE':
    st.subheader("Q1. 北神戸総合高校で、新しい自分を見つけたいですか？")
    if st.button("はい！", type="primary"): move_to('YES'); st.rerun()

elif st.session_state.step == 'YES':
    st.subheader("Q2. あなたの得意（または好き）なのはどっち？")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("論理的に考える（思考判断）", use_container_width=True): move_to('rikei'); st.rerun()
    with col2:
        if st.button("知識を積み上げる（暗記）", use_container_width=True): move_to('bunnkei'); st.rerun()

elif st.session_state.step == 'rikei':
    st.subheader("Q3. どちらの分野により惹かれますか？")
    if st.button("宇宙・気象", use_container_width=True): st.session_state.result = "宇宙気象系列"; move_to('goal'); st.rerun()
    if st.button("DX・プログラミング", use_container_width=True): st.session_state.result = "DX系列"; move_to('goal'); st.rerun()
    if st.button("幅広く探究したい", use_container_width=True): st.session_state.result = "リベラルアーツ理系系列"; move_to('goal'); st.rerun()

elif st.session_state.step == 'bunnkei':
    st.subheader("Q3. どのような活動に興味がありますか？")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("地域・観光・防災", use_container_width=True): move_to('tinomanabi'); st.rerun()
    with col2:
        if st.button("文化・歴史・多様性", use_container_width=True): move_to('zinnnomanabi'); st.rerun()

elif st.session_state.step == 'tinomanabi':
    st.subheader("Q4. 将来、身につけたい力は？")
    if st.button('企画・マーケティング', use_container_width=True): st.session_state.result = "兵庫からスタートアップ系列"; move_to('goal'); st.rerun()
    if st.button('スポーツ・リーダーシップ', use_container_width=True): st.session_state.result = "スポーツアウトドアと防災系列"; move_to('goal'); st.rerun()

elif st.session_state.step == 'zinnnomanabi':
    st.subheader("Q4. 言語や芸術、多文化に関わりたいですか？")
    if st.button('興味がある', use_container_width=True): st.session_state.result = "ダイバーシティー&インクルージョン系列"; move_to('goal'); st.rerun()
    if st.button('教養を深めたい', use_container_width=True): st.session_state.result = "リベラルアーツ文系系列"; move_to('goal'); st.rerun()

# --- 結果画面 ---
elif st.session_state.step == 'goal':
    st.balloons()
    res = st.session_state.result
    save_diagnosis(res) # 履歴保存
    st.success(f"あなたにおすすめなのは…\n\n## **【{res}】**")
    
    st.info(DESCRIPTIONS.get(res, ""))
    
    # 追加機能：向いているキーワード
    st.write("---")
    st.write("**🔍 この系列に向いているキーワード**")
    k_cols = st.columns(len(KEYWORDS.get(res, [])))
    for i, kw in enumerate(KEYWORDS.get(res, [])):
        k_cols[i].markdown(f"✅ {kw}")
    
    st.divider()
    if st.button("最初からやり直す", type="primary", use_container_width=True):
        reset_app()
        st.rerun()

# --- 共通の戻るボタン (スタート画面と結果画面以外で表示) ---
if st.session_state.step not in ['start', 'goal']:
    st.divider()
    if st.button("← 前の画面に戻る"):
        go_back()
        st.rerun()