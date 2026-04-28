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

st.title("天気記号クイズ（重ね表示）")

# セッション状態
if "current" not in st.session_state:
    st.session_state.current = random.choice(list(ws.keys()))

def draw_symbol(s):
    base = s[0]
    rest = s[1:]

    html = f"""
    <div style="position:relative;width:120px;height:120px;margin:auto;">
      <div style="position:absolute;font-size:100px;">{base}</div>
    """

    for ch in rest:
        # カタカナ → 右下小さく
        if ch in "ツニキ":
            html += f"""
            <div style="position:absolute;
                        right:5px;bottom:0;
                        font-size:30px;">
              {ch}
            </div>
            """

        # ＊ → 回転
        elif ch == "＊":
            html += """
            <div style="position:absolute;
                        left:30px;top:20px;
                        font-size:60px;
                        transform:rotate(90deg);">
              *
            </div>
            """

        # その他 → 中央
        else:
            html += f"""
            <div style="position:absolute;
                        left:30px;top:20px;
                        font-size:60px;">
              {ch}
            </div>
            """

    html += "</div>"
    return html


# 表示
st.markdown(draw_symbol(st.session_state.current), unsafe_allow_html=True)

# 入力
answer = st.text_input("意味を入力")

# 判定
if st.button("回答"):
    if answer == ws[st.session_state.current]:
        st.success("正解！")
        st.session_state.current = random.choice(list(ws.keys()))
    else:
        st.error(f"不正解：{ws[st.session_state.current]}")
