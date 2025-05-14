import streamlit as st
from PIL import Image
from datetime import datetime

st.title("📸 旅の思い出ボード")

# ボードタイトルの入力
board_title = st.text_input("この旅のボードのタイトルを入力してください", "福井の恐竜博物館")

st.markdown("---")

# セッションに思い出一覧を保持
if "memories" not in st.session_state:
    st.session_state.memories = []

# 写真アップロード
uploaded_file = st.file_uploader("写真を選んでください", type=["jpg", "jpeg", "png"])

# 感想入力（スマホの音声入力キーボードもOK）
comment = st.text_input("お子さんの感想を入力してください（音声入力OK）")

# ピン止め処理
if st.button("📌 ピン止めする") and uploaded_file and comment:
    image = Image.open(uploaded_file)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.memories.append({
        "image": image,
        "comment": comment,
        "timestamp": timestamp
    })
    st.success("思い出をピン止めしました！")

st.markdown("## ✨ 旅の思い出たち")

# 思い出を表示（新しい順）
for memory in st.session_state.memories[::-1]:
    st.image(memory["image"], width=300)
    st.markdown(f"📝 {memory['comment']}")
    st.caption(f"📅 {memory['timestamp']}")
    st.markdown("---")
