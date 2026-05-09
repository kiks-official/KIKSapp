import streamlit as st

# 1. ページ設定の強化（学校のカラーに合わせるなどの準備）
st.set_page_config(page_title="北神総合 系列選択ナビ", page_icon="🎓", layout="centered")

# 2. サイドバー機能（追加）: 便利なリンク集
with st.sidebar:
    st.title("🔗 リンク・情報")
    st.info("このアプリは新入生が自分の興味・関心に合わせて系列を考えるためのガイドです。")
    st.divider()
    st.write("📖 **学校公式リンク**")
    st.markdown("- [北神戸総合高校 HP](https://www.google.com) ※実際のURLへ")
    st.markdown("- [学校案内パンフレット](https://www.google.com)")
    st.divider()
    if st.button("🔄 アプリをリセット"):
        st.session_state.step = 'start'
        st.session_state.result = ""
        st.rerun()

# --- メイン画面 ---
st.title("🎓 新入生のための系列選択ナビ")

# セッション状態の初期化
if 'step' not in st.session_state:
    st.session_state.step = 'start'

# 3. プログレスバー機能（追加）
# 診断ステップに応じてゲージを増やす
steps_map = {'IE': 20, 'YES': 40, 'rikei': 70, 'bunnkei': 70, 'tinomanabi': 90, 'zinnnomanabi': 90, 'goal': 100}
if st.session_state.step in steps_map:
    progress = steps_map[st.session_state.step]
    st.progress(progress / 100)
    st.caption(f"診断の進み具合: {progress}%")

# --- 既存ロジックの改善 ---

if st.session_state.step == 'start':
    st.subheader("北神戸総合高校へようこそ！")
    st.write("あなたの未来をデザインする「系列選択」をお手伝いします。")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("診断を始める", use_container_width=True, type="primary"):
            st.session_state.step = 'IE'
            st.rerun()
    with col2:
        if st.button("系列（天・地・人）の説明を見る", use_container_width=True):
            st.session_state.step = 'NO'
            st.rerun()

elif st.session_state.step == 'NO':
    st.subheader('KIKS系列体系「天・地・人」')
    st.write("本校の学びは、大きく3つの視点に分かれています。解説を選んでください。")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("✨ 天の学び"):
            st.session_state.step = 'tennkaisetu'
            st.rerun()
    with col2:
        if st.button("🌍 地の学び"):
            st.session_state.step = 'tikaisetu'
            st.rerun()
    with col3:
        if st.button("🤝 人の学び"):
            st.session_state.step = 'zinnkaisetu'
            st.rerun()
    with col4:
        if st.button("🏠 戻る"):
            st.session_state.step = 'start'
            st.rerun()

# --- 解説ページ群（内容はそのまま、UIを少し整理） ---
elif st.session_state.step == 'tennkaisetu':
    st.subheader('✨ 天の学び：科学と技術の探究')
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("宇宙・気象"):
            st.session_state.step = 'utyuukaisetu'
            st.rerun()
    with col2:
        if st.button("DX(IT技術)"):
            st.session_state.step = 'DXkaisetu'
            st.rerun()
    with col3:
        if st.button('戻る', key="back_to_no_1"):
            st.session_state.step = 'NO'
            st.rerun()

elif st.session_state.step == 'utyuukaisetu':
    st.info("### 宇宙・気象系列\nめざせ宇宙！守れ地球！宇宙に関連した産業や、地球の気候をふまえた暮らしをリードする人材を育成します。")
    if st.button("一覧に戻る"):
        st.session_state.step = 'tennkaisetu'
        st.rerun()

elif st.session_state.step == 'DXkaisetu':
    st.info("### DX系列\nAIやIoTを活用し、ビジネスモデルそのものを変革する等、新たな価値を創造する人材を育成します。")
    if st.button("一覧に戻る"):
        st.session_state.step = 'tennkaisetu'
        st.rerun()

# --- 地の学び ---
elif st.session_state.step == 'tikaisetu':
    st.subheader('🌍 地の学び：地域と実践')
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("スタートアップ"):
            st.session_state.step = 'hyogokaisetu'
            st.rerun()
    with col2:
        if st.button("防災・アウトドア"):
            st.session_state.step = 'autodoakaisetu'
            st.rerun()
    with col3:
        if st.button('戻る', key="back_to_no_2"):
            st.session_state.step = 'NO'
            st.rerun()

elif st.session_state.step == 'hyogokaisetu':
    st.success("### 兵庫からスタートアップ系列\n観光資源を生かした仕事の創出やまちおこしなど、アントレプレナーシップを有する人材を育成します。")
    if st.button("一覧に戻る"):
        st.session_state.step = 'tikaisetu'
        st.rerun()

elif st.session_state.step == 'autodoakaisetu':
    st.success("### スポーツアウトドアと防災系列\nスポーツ・アウトドアと防災活動を結びつけ、新たな価値や生きがいを創出できる人材を育成します。")
    if st.button("一覧に戻る"):
        st.session_state.step = 'tikaisetu'
        st.rerun()

# --- 人の学び ---
elif st.session_state.step == 'zinnkaisetu':
    st.subheader('🤝 人の学び：共生と教養')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("D&I"):
            st.session_state.step = 'daibakaisetu'
            st.rerun()
    with col2:
        if st.button("LA理系"):
            st.session_state.step = 'riberikaisetu'
            st.rerun()
    with col3:
        if st.button("LA文系"):
            st.session_state.step = 'ribebunnkaisetu'
            st.rerun()
    with col4:
        if st.button('戻る', key="back_to_no_3"):
            st.session_state.step = 'NO'
            st.rerun()

elif st.session_state.step == 'daibakaisetu':
    st.warning("### ダイバーシティ＆インクルージョン系列\n多様な人々と関わり理解し合うための学びを通じて、共生社会の担い手となる人材を育成します。")
    if st.button("一覧に戻る"):
        st.session_state.step = 'zinnkaisetu'
        st.rerun()

elif st.session_state.step == 'riberikaisetu' or st.session_state.step == 'ribebunnkaisetu':
    st.warning("### リベラルアーツ系列\n芸術やキャリア探究を通じて様々な視点を持ち、自分らしく生きるための基本教養を身に付けます。")
    if st.button("一覧に戻る"):
        st.session_state.step = 'zinnkaisetu'
        st.rerun()

# --- 診断ロジック ---
elif st.session_state.step == 'IE':
    st.subheader("Q1. 北神戸総合高校で、新しい自分を見つけたいですか？")
    if st.button("はい！", type="primary"):
        st.session_state.step = 'YES'
        st.rerun()

elif st.session_state.step == 'YES':
    st.subheader("Q2. あなたの得意（または好き）なのはどっち？")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("論理的に考える（思考判断）", use_container_width=True):
            st.session_state.step = 'rikei'
            st.rerun()
    with col2:
        if st.button("知識を積み上げる（暗記）", use_container_width=True):
            st.session_state.step = 'bunnkei'
            st.rerun()

elif st.session_state.step == 'rikei':
    st.subheader("Q3. どちらの分野により惹かれますか？")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("宇宙・気象"):
            st.session_state.result = "宇宙気象系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col2:
        if st.button("DX・プログラミング"):
            st.session_state.result = "DX系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col3:
        if st.button("幅広く探究したい"):
            st.session_state.result = "リベラルアーツ理系系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col4:
        if st.button("やっぱり文系かも"):
            st.session_state.step = 'bunnkei'
            st.rerun()

elif st.session_state.step == 'bunnkei':
    st.subheader("Q3. どのような活動に興味がありますか？")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("地域・観光・防災"):
            st.session_state.step = 'tinomanabi'
            st.rerun()
    with col2:
        if st.button("文化・歴史・多様性"):
            st.session_state.step = 'zinnnomanabi'
            st.rerun()
    with col3:
        if st.button("やっぱり理系かも"):
            st.session_state.step = 'rikei'
            st.rerun()

elif st.session_state.step == 'tinomanabi':
    st.subheader("Q4. 将来、身につけたい力は？")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('企画・マーケティング'):
            st.session_state.result = "兵庫からスタートアップ系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col2:
        if st.button('スポーツ・リーダーシップ'):
            st.session_state.result = "スポーツアウトドアと防災系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col3:
        if st.button('戻る', key="back_b"):
            st.session_state.step = 'bunnkei'
            st.rerun()

elif st.session_state.step == 'zinnnomanabi':
    st.subheader("Q4. 言語や芸術、多文化に関わりたいですか？")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('興味がある', key="final_yes"):
            st.session_state.result = "ダイバーシティー&インクルージョン系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col2:
        if st.button('教養を深めたい', key="final_no"):
            st.session_state.result = "リベラルアーツ文系系列"
            st.session_state.step = 'goal'
            st.rerun()
    with col3:
        if st.button('戻る', key="back_c"):
            st.session_state.step = 'bunnkei'
            st.rerun()

# --- 結果画面 ---
elif st.session_state.step == 'goal':
    st.balloons()
    result = st.session_state.result
    st.success(f"あなたにおすすめなのは…\n\n## **【{result}】**")

    # 4. アドバイス機能（追加）
    descriptions = {
        "宇宙気象系列": "めざせ宇宙！守れ地球！人類の新たなフロンティアを科学で支える君を待っています。",
        "DX系列": "デジタル技術で世界をアップデート！新しいサービスを創り出す面白さを体験しましょう。",
        "兵庫からスタートアップ系列": "兵庫の魅力をビジネスに変える！君のアイデアが地域を動かす力になります。",
        "スポーツアウトドアと防災系列": "心身を鍛え、社会を守る。スポーツと防災を掛け合わせた新しい生きがいを見つけましょう。",
        "ダイバーシティー&インクルージョン系列": "違いを力に変える。多様な人々と協力し、共生社会をリードする人材を目指しましょう。",
        "リベラルアーツ理系系列": "幅広い教養と理系的な視点を両立。自分らしい生き方の土台を作りましょう。",
        "リベラルアーツ文系系列": "芸術や社会、言葉を通して世界を見る視点を養い、豊かな教養を身に付けましょう。"
    }
    
    st.info(descriptions.get(result, ""))
    
    st.divider()
    st.write("この結果はあくまで一つの目安です。1年次の学びを通して、じっくり考えていきましょう！")

    if st.button("最初からやり直す", type="primary", use_container_width=True):
        st.session_state.step = 'start'
        st.session_state.result = ""
        st.rerun()