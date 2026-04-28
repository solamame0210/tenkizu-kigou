import streamlit as st
import random

# フォント（ズレ防止）
st.markdown("""
<style>
* {
  font-family: "Noto Sans JP", "Arial Unicode MS", sans-serif;
}
</style>
""", unsafe_allow_html=True)

ws = {
"◯":"快晴",
"◯｜":"晴",
"◎":"曇",
"●":"雨",
"●ツ":"雨強し",
"●ニ":"にわか雨",
"●キ":"霧雨",
"◯＊":"雪",
"◯＊ニ":"にわか雪",
"◯＊ツ":"雪強し",
"＊◒":"みぞれ",
"◯▲":"ひょう",
"◯△":"あられ",
"◒":"雷",
"◒ツ":"雷強し",
"◯・":"霧",
"◯∞":"煙霧",
"◯S":"ちり煙霧",
"◯S⇢":"砂塵あらし",
"◯↑⇢":"地ふぶき",
"◯×":"天気不明"
}

st.title("天気記号クイズ")

# 初期化
if "current" not in st.session_state:
    st.session_state.current = random.choice(list(ws.keys()))
if "score" not in st.session_state:
    st.session_state.score = 0


# 記号描画
def draw_symbol(s):
    base = s[0]
    rest = s[1:]

    html = f"""
<div style="position:relative;width:140px;height:140px;margin:auto;">
  <div style="
    position:absolute;
    top:50%; left:50%;
    transform:translate(-50%,-50%);
    font-size:110px;">
    {base}
  </div>
"""

    for ch in rest:
        # 小カタカナ（右下）
        if ch in "ツニキ":
            html += f"""
  <div style="
    position:absolute;
    bottom:8px; right:10px;
    font-size:30px;">
    {ch}
  </div>
"""
        # ＊（回転）
        elif ch == "＊":
            html += """
  <div style="
    position:absolute;
    top:50%; left:50%;
    transform:translate(-50%,-50%) rotate(90deg);
    font-size:70px;">
    ＊
  </div>
"""
        # その他（中央）
        else:
            html += f"""
  <div style="
    position:absolute;
    top:50%; left:50%;
    transform:translate(-50%,-50%);
    font-size:70px;">
    {ch}
  </div>
"""

    html += "</div>"
    return html


# ❗ここが重要（HTMLとして表示）
st.markdown(draw_symbol(st.session_state.current), unsafe_allow_html=True)

# スコア
st.write(f"連続正解数：{st.session_state.score}")

# 入力（Enter対応）
with st.form(key="quiz_form", clear_on_submit=True):
    answer = st.text_input("意味を入力")
    submit = st.form_submit_button("回答")

if submit:
    if answer == ws[st.session_state.current]:
        st.success("正解！")
        st.session_state.score += 1
        st.session_state.current = random.choice(list(ws.keys()))
    else:
        st.error(f"不正解：{ws[st.session_state.current]}")
        st.session_state.score = 0
