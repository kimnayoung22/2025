import streamlit as st

# -----------------------------
# 🎨 페이지 설정
# -----------------------------
st.set_page_config(page_title="💡 MBTI 직업 추천기", page_icon="✨", layout="centered")

# -----------------------------
# 💼 MBTI 직업 데이터
# -----------------------------
mbti_jobs = {
    "ISTJ": ["📊 회계사", "📈 데이터 분석가", "🏛️ 행정 공무원"],
    "ISFJ": ["🩺 간호사", "📚 교사", "🤝 사회복지사"],
    "INFJ": ["🧠 심리상담사", "✍️ 작가", "🔬 연구원"],
    "INTJ": ["📋 전략 기획가", "⚙️ 엔지니어", "💻 데이터 사이언티스트"],
    "ISTP": ["🔧 기계 엔지니어", "🛩️ 파일럿", "🚑 응급 구조사"],
    "ISFP": ["🎨 디자이너", "📷 사진작가", "🎵 작곡가"],
    "INFP": ["🖋️ 시인", "🌱 사회 운동가", "📖 편집자"],
    "INTP": ["🔍 연구원", "💻 소프트웨어 개발자", "💡 발명가"],
    "ESTP": ["💼 기업가", "⚽ 스포츠 코치", "📢 영업 관리자"],
    "ESFP": ["🎭 배우", "🎉 이벤트 플래너", "🗺️ 여행 가이드"],
    "ENFP": ["📣 마케터", "🚀 창업가", "📰 기자"],
    "ENTP": ["💡 벤처기업가", "🎯 광고 기획자", "📊 컨설턴트"],
    "ESTJ": ["📂 경영 관리자", "🎖️ 군 장교", "🛠️ 프로젝트 매니저"],
    "ESFJ": ["💖 간호사", "📢 홍보 담당자", "📚 교사"],
    "ENFJ": ["🤝 멘토", "🧑‍💼 HR 매니저", "💬 커뮤니케이션 전문가"],
    "ENTJ": ["👑 CEO", "🗺️ 전략 컨설턴트", "⚖️ 변호사"]
}

# -----------------------------
# 🌟 타이틀
# -----------------------------
st.markdown(
    "<h1 style='text-align: center; color: #FF69B4;'>🌈 MBTI 기반 직업 추천 💼✨</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; font-size: 18px;'>당신의 MBTI를 선택하고 <b>운명 직업</b>을 확인하세요! 🚀💖</p>",
    unsafe_allow_html=True
)

# -----------------------------
# 📝 MBTI 선택
# -----------------------------
selected_mbti = st.selectbox("💡 당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

# -----------------------------
# 🎯 직업 추천 결과
# -----------------------------
if selected_mbti:
    st.markdown(f"<h2 style='color: #FFD700;'>✨ {selected_mbti} 유형 추천 직업 ✨</h2>", unsafe_allow_html=True)
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"<p style='font-size: 20px;'>🌟 {job}</p>", unsafe_allow_html=True)

# -----------------------------
# 🔍 추가 정보 버튼
# -----------------------------
if st.button("📚 직업 설명 보기"):
    st.success("💡 각 직업에 대한 설명 기능은 곧 추가됩니다! 🛠️")

# -----------------------------
# 🎨 푸터
# -----------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 14px; color: gray;'>✨ Created with ❤️ using Streamlit ✨</p>",
    unsafe_allow_html=True
)

