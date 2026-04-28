import streamlit as st
import random

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

st.title("天気記号クイズ（完全版）")

# セッション初期化
if "current" not in st.session_state:
    st.session_state.current = random.choice(list(ws.keys()))
if "score" not in st.session_state:
    st.session_state.score = 0

def draw_symbol(s):
    base = s[0]
    rest = s[1:]

    html = f"""
    <div style="position:relative;width:120px;height:120px;margin:auto;">
      <div style="position:absolute;font-size:100px;">{base}</div>
    """

    for ch in rest:
        if ch in "ツニキ":  # 小カタカナ右下
            html += f"""
            <div style="position:absolute;right:5px;bottom:0;font-size:30px;">
              {ch}
            </div>
            """
        elif ch == "＊":  # 回転
            html += """
            <div style="position:absolute;left:30px;top:20px;font-size:60px;
                        transform:rotate(90deg);">
              *
            </div>
            """
        else:  # 中央
            html += f"""
            <div style="position:absolute;left:30px;top:20px;font-size:60px;">
              {ch}
            </div>
            """

    html += "</div>"
    return html


# 記号表示
st.markdown(draw_symbol(st.session_state.current), unsafe_allow_html=True)

# スコア表示
st.write(f"連続正解数：{st.session_state.score}")

# Enterで回答（form）
with st.form(key="quiz_form", clear_on_submit=True):
    answer = st.text_input("意味を入力")
    submit = st.form_submit_button("回答")

if submit:
    if answer == ws[st.session_state.current]:
        st.success("正解！")
        st.session_state.score += 1  # ②スコア加算
        st.session_state.current = random.choice(list(ws.keys()))  # ①次の問題
    else:
        st.error(f"不正解：{ws[st.session_state.current]}")
        st.session_state.score = 0  # ミスでリセット
