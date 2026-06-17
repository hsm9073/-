import streamlit as st
import pandas as pd

# 1. 공통 데이터 구축
data = {
    "연도": [1998, 2001, 2005, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "단백질(g)": [76.1, 73.5, 77.7, 68.6, 69.2, 70.7, 77.5, 76.4, 75.3, 74.2, 74.1, 76.7, 76.7, 75.5, 74.8, 75.5, 74.3, 74.0, 72.1, 73.0, 75.7],
    "칼슘(mg)": [503.7, 503.3, 560.5, 477.5, 495.3, 499.8, 534.4, 518.0, 508.3, 500.3, 494.6, 510.1, 526.5, 524.4, 517.3, 492.1, 486.6, 486.3, 488.4, 495.2, 499.0],
    "나트륨(mg)": [4951.2, 5430.2, 5691.8, 4854.9, 5006.5, 5073.3, 5225.6, 5211.0, 4942.1, 4176.3, 4033.2, 4188.7, 3585.5, 3586.5, 3488.4, 3455.6, 3350.4, 3224.1, 3213.3, 3282.3, 3279.6]
}
df = pd.DataFrame(data)
df.set_index("연도", inplace=True)


# --- 2. 페이지별 화면 정의 ---

# [페이지 1] 홈 / 종합 대시보드 (★그래프 왜곡 전면 수정!)
def show_home():
    st.title("🍽️ 한국인의 식탁 20년 변천사")
    st.markdown("### **국민건강영양조사 데이터로 보는 우리 식습관의 명과 암**")
    st.write("💡 왼쪽 사이드바 메뉴를 클릭하시면 영양소별 아주 상세한 개별 분석을 보실 수 있습니다.")
    st.divider()
    
    # 1. 상단 권장량 대조 및 현황 섹션
    st.subheader("📊 하루 평균 섭취량 vs 권장량 기준")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 🧂 나트륨")
        st.metric(label="2024년 평균", value="3,279.6 mg", delta="-1,671.6 mg")
        st.caption("🚨 **WHO 기준: 2,000mg 미만**")
        st.error("권장량의 **약 1.6배** 과다 섭취")
        
    with col2:
        st.markdown("#### 🥩 단백질")
        st.metric(label="2024년 평균", value="75.7 g", delta="-0.4 g", delta_color="off")
        st.caption("✅ **한국인 기준: 약 55~65g**")
        st.success("권장량 대비 **충분하고 안정적**")
        
    with col3:
        st.markdown("#### 🥛 칼슘")
        st.metric(label="2024년 평균", value="499.0 mg", delta="-4.7 mg", delta_color="inverse")
        st.caption("❌ **한국인 기준: 약 700~800mg**")
        st.warning("권장량의 **약 65%** 만성 부족")
        
    st.divider()
    
    # 2. 왜곡 없는 개별 미니 차트 대시보드 배치 (★핵심 수정 변경 구간)
    st.subheader("📉 3대 영양소 20개년 트렌드 요약")
    st.markdown("각 영양소의 고유 단위와 스케일을 살려 개별적으로 시각화한 요약 대시보드입니다.")
    
    g_col1, g_col2, g_col3 = st.columns(3)
    
    with g_col1:
        st.markdown("**🧂 나트륨 추이 (mg)**")
        st.line_chart(df["나트륨(mg)"], height=200)
        st.caption("2005년 정점 이후 확실한 우하향 감소세")
        
    with g_col2:
        st.markdown("**🥩 단백질 추이 (g)**")
        st.line_chart(df["단백질(g)"], height=200)
        st.caption("70g대 중반을 유지하며 안정적인 기반")
        
    with g_col3:
        st.markdown("**🥛 칼슘 추이 (mg)**")
        st.bar_chart(df["칼슘(mg)"], height=200)
        st.caption("20년째 500mg 안팎에서 정체 중")

    st.divider()
    
    # 종합 인사이트 요약
    st.subheader("💡 데이터가 주는 최종 메시지")
    st.markdown("""
    지난 20년간 대한민국 국민들의 식생활 성적표는 **'절반의 성공'**입니다.
    
    * **명(明) - 나트륨 대폭 감소:** 한국인의 짜게 먹는 습관은 확실히 개선되고 있습니다.
    * **유지 - 단백질의 안정성:** 우리 몸의 기초 버팀목인 단백질은 권장 기준치를 상회하며 든든하게 유지 중입니다.
    * **암(暗) - 칼슘의 정체:** 가장 큰 문제입니다. 뼈 건강을 책임지는 칼슘은 20년 전이나 지금이나 여전히 권장 기준선에 한참 미달입니다.
    
    🎯 **앞으로의 과제:** "싱겁게 먹으면서도, 칼슘은 똑똑하게 채우는 식단"을 만드는 것입니다!
    """)
    
    st.divider()
    with st.expander("🔍 원본 통합 데이터 전체 보기"):
        st.dataframe(df.style.format({
            "단백질(g)": "{:.1f} g",
            "칼슘(mg)": "{:.1f} mg",
            "나트륨(mg)": "{:,.1f} mg"
        }), use_container_width=True)


# [페이지 2] 나트륨 상세
def show_sodium():
    st.title("📉 1. 명(明): '짠맛'과의 전쟁에서 승리 중")
    st.markdown("### **한국인은 짜게 먹는 습관을 고쳤을까?**")
    st.divider()
    st.subheader("나트륨 섭취량 추이 (mg)")
    st.line_chart(df["나트륨(mg)"])
    st.info("""
    * **성공적인 변화:** 2005년 **5,691.8mg**에 달하던 압도적인 나트륨 섭취량이 2024년 **3,279.6mg**으로 뚝 떨어졌습니다!
    * *⚠️ 단, 세계보건기구(WHO) 권장량인 **2,000mg**에 도달하려면 아직 조금 더 노력이 필요합니다.*
    """)

# [페이지 3] 단백질 상세
def show_protein():
    st.title("🥩 2. 유지: 든든하게 자리를 지킨 기초 체력")
    st.markdown("### **흔들림 없는 영양소의 버팀목**")
    st.divider()
    st.subheader("단백질 섭취량 추이 (g)")
    st.line_chart(df["단백질(g)"])
    st.success("""
    * **안정적인 영양소:** 우리 성인 일일 단백질 권장량인 **55~65g**을 상회하는 수치(75.7g)로, 아주 안정적으로 유지되고 있습니다.
    """)

# [페이지 4] 칼슘 상세
def show_calcium():
    st.title("⚠️ 3. 암(暗): 20년째 풀지 못한 '칼슘 부족'")
    st.markdown("### **나트륨을 줄이다 이것까지 놓쳤을까?**")
    st.divider()
    st.subheader("칼슘 섭취량 추이 (mg)")
    st.bar_chart(df["칼슘(mg)"])
    st.warning("""
    * **고질적인 만년 꼴찌:** 칼슘은 20년 전이나 지금이나 여전히 **500mg 안팎에서 정체**되어 있어 하루 권장량(**700~800mg**)에 한참 못 미치는 수준입니다.
    """)


# --- 3. 멀티페이지 네비게이션 설정 ---
page_home = st.Page(show_home, title="종합 대시보드", icon="🏠")
page_sodium = st.Page(show_sodium, title="🧂 나트륨 분석", icon="📉")
page_protein = st.Page(show_protein, title="🥩 단백질 분석", icon="💪")
page_calcium = st.Page(show_calcium, title="🥛 칼슘 분석", icon="⚠️")

pg = st.navigation([page_home, page_sodium, page_protein, page_calcium])
st.set_page_config(page_title="한국인 식습관 20년 변천사", page_icon="📊", layout="centered")
pg.run()
