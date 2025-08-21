import streamlit as st
import random

st.set_page_config(page_title="🐛 벌BTI 명언봇", page_icon="🐞")

# ===== CSS 배경 추가 =====
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://cdn-icons-png.flaticon.com/512/1864/1864514.png"); /* 벌레 아이콘 PNG */
    background-size: 150px;   /* 벌레 크기 조정 */
    background-repeat: repeat; /* 반복 패턴 */
    background-attachment: fixed;
    opacity: 0.9;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ===== 타이틀 =====
st.title("🐛 기분별 벌레 명언")
st.write("지금 기분에 맞는 벌레와 명언을 받아보세요!")

# 명언 데이터
quotes = {
    "행복": ["🦋 행복은 우리 안에 있다.", "🌸 오늘 하루는 선물이다.", "😀 웃음은 마음의 햇살이다."],
    "슬픔": ["🪲 힘들 땐 잠시 멈춰도 괜찮다.", "🌑 어두운 밤도 끝난다.", "💪 슬픔은 우리를 단단하게 한다."],
    "분노": ["🐝 화는 에너지로 바꿀 수 있다.", "🔥 강한 마음은 감정을 지배한다.", "💡 분노는 성장의 신호다."],
    "불안": ["🪰 작은 불빛도 어둠을 몰아낸다.", "✨ 불안은 준비의 신호다.", "🌌 별빛은 가장 어두운 밤에 빛난다."],
    "지침": ["🐌 천천히 가도 괜찮다.", "💤 휴식도 중요한 과정이다.", "🍂 쉬는 동안 힘을 모은다."],
    "설렘": ["🦟 새로운 시작은 설렘을 준다.", "🌞 작은 기대가 큰 행복을 만든다.", "💫 호기심은 삶의 활력이다."],
    "무기력": ["🕷️ 작은 계획도 큰 변화를 만든다.", "📌 오늘 한 가지라도 달성하자.", "📝 기록이 동기부여가 된다."],
    "용기": ["🦗 도전은 성장의 시작이다.", "💪 두려움을 직면하라.", "🔥 시도하지 않으면 변화도 없다."]
}

# 기분 선택
mood = st.selectbox(
    "지금 기분은 어떤가요?",
    ["행복 😀", "슬픔 😢", "분노 😡", "불안 😰", "지침 😴", "설렘 😍", "무기력 😶", "용기 💪"]
)

# 기분에 따른 벌레 연결
bug_map = {
    "행복": "🦋 나비",
    "슬픔": "🪲 풍뎅이",
    "분노": "🐝 말벌",
    "불안": "🪰 반딧불이",
    "지침": "🐌 달팽이",
    "설렘": "🦟 잠자리",
    "무기력": "🕷️ 거미",
    "용기": "🦗 사마귀"
}

# 세션 기록
if "history" not in st.session_state:
    st.session_state["history"] = []

if st.button("명언 받기 ✨"):
    key = mood.split()[0]
    bug = bug_map[key]
    quote = random.choice(quotes[key])
    st.subheader(f"당신의 벌레: {bug}")
    st.success(f"✨ 명언: {quote}")

    # 이펙트
    if key == "행복":
        st.balloons()
    elif key == "슬픔":
        st.snow()

    st.session_state["history"].append(f"{bug} - {quote}")

if st.session_state["history"]:
    st.write("📜 지금까지 받은 명언 기록:")
    for i, item in enumerate(st.session_state["history"], 1):
        st.write(f"{i}. {item}")
({bug_map[rand_mood]}) 기분으로 살아보는 건 어때요?")
