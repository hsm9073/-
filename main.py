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

# [페이지 1] 홈 / 종합 대시보드
def show_home():
    st.title("🍽️ 한국인의 식탁 20년 변천사")
    st.markdown("### **국민건강영양조사 데이터로 보는 우리 식습관의 명과 암**")
    st.write("💡 왼쪽 사이드바 메뉴를 통해 영양소별 상세 분석과 최종 총정리 페이지를 확인하실 수 있습니다.")
    st.divider()
    
    st.subheader("📊 하루 평균 섭취량 vs 권장량 기준 (2024년 기준)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 🧂 나트륨")
        st.metric(label="2024년 평균", value="3,279.6 mg", delta="-1,671.6 mg")
        st.caption("🚨 **WHO 기준: 2,000mg 미만**")
        st.error("많이 줄었지만, 여전히 권장량의 **약 1.6배 과다 섭취 중**입니다.")
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
    
    st.subheader("📈 3대 영양소 20개년 트렌드 요약")
    g_col1, g_col2, g_col3 = st.columns(3)
    with g_col1:
        st.markdown("**🧂 나트륨 추이 (mg)**")
        st.line_chart(df["나트륨(mg)"], height=200)
        st.caption("⚠️ 꾸준히 감소했으나 아직 권장량보다 높은 수준")
    with g_col2:
        st.markdown("**🥩 단백질 추이 (g)**")
        st.line_chart(df["단백질(g)"], height=200)
    with g_col3:
        st.markdown("**🥛 칼슘 추이 (mg)**")
        st.bar_chart(df["칼슘(mg)"], height=200)

    st.divider()
    with st.expander("🔍 원본 통합 데이터 전체 보기"):
        st.dataframe(df.style.format({
            "단백질(g)": "{:.1f} g",
            "칼슘(mg)": "{:.1f} mg",
            "나트륨(mg)": "{:,.1f} mg"
        }), use_container_width=True)


# [페이지 2] 나트륨 상세
def show_sodium():
    st.title("📉 명(明): '짠맛'과의 전쟁에서 승리 중")
    st.markdown("### **한국인은 짜게 먹는 습관을 고쳤을까?**")
    st.divider()
    st.subheader("나트륨 섭취량 추이 (mg)")
    st.line_chart(df["나트륨(mg)"])
    st.info("""
    * **성공적인 변화:** 2005년 **5,691.8mg**에 달하던 압도적인 나트륨 섭취량이 2024년 **3,279.6mg**으로 뚝 떨어졌습니다! 한국인의 짜게 먹는 습관은 확실히 개선되고 있습니다.
    * **⚠️ 하지만 아직 방심은 금물:** 20여 년간 눈부신 감소를 이루어냈음에도 불구하고, 현재 수치는 **세계보건기구(WHO) 하루 권장량인 2,000mg보다 여전히 확연히 높은 수준**입니다. 조금 더 싱겁게 먹기 위한 노력이 지속되어야 합니다.
    """)


# [페이지 3] 단백질 상세
def show_protein():
    st.title("🥩 유지: 든든하게 자리를 지킨 기초 체력")
    st.markdown("### **흔들림 없는 영양소의 버팀목**")
    st.divider()
    st.subheader("단백질 섭취량 추이 (g)")
    st.line_chart(df["단백질(g)"])
    st.success("""
    * **안정적인 영양소:** 우리 성인 일일 단백질 권장량인 **55~65g**을 상회하는 수치(75.7g)로, 20년 동안 아주 안정적으로 유지되고 있습니다.
    """)


# [페이지 4] 칼슘 상세
def show_calcium():
    st.title("⚠️ 암(暗): 20년째 풀지 못한 '칼슘 부족'")
    st.markdown("### **나트륨을 줄하다 이것까지 놓쳤을까?**")
    st.divider()
    st.subheader("칼슘 섭취량 추이 (mg)")
    st.bar_chart(df["칼슘(mg)"])
    st.warning("""
    * **고질적인 만년 꼴찌:** 칼슘은 20년 전이나 지금이나 여전히 **500mg 안팎에서 정체**되어 있어 하루 권장량(**700~800mg**)에 한참 못 미치는 수준입니다.
    """)


# [페이지 5] 총정리 및 리포트
def show_summary():
    st.title("🎯 결론 및 종합 성적표")
    st.markdown("### **지난 20년 데이터가 대한민국에 던지는 메시지**")
    st.divider()
    
    st.subheader("📋 3대 영양소 최종 성적표")
    s_col1, s_col2, s_col3 = st.columns(3)
    s_col1.markdown("### 🧂 나트륨\n## **A-**\n**참 잘했어요!**\n섭취량이 42%나 감소하며 짠 식습관을 크게 개선했습니다. **(단, 아직 권장량보다 높음)**")
    s_col2.markdown("### 🥩 단백질\n## **A**\n**훌륭합니다!**\n서구화된 식생활 속에서도 기준치 이상을 아주 안정적으로 유지 중입니다.")
    s_col3.markdown("### 🥛 칼슘\n## **F**\n**노력이 필요해요!**\n20년째 권장량의 65% 수준에 머물러 있는 우리 식단의 최대 약점입니다.")
    
    st.divider()
    
    st.subheader("💡 웰빙 식탁을 위한 앞으로의 실천 가이드")
    st.markdown("""
    데이터 분석 결과, 한국인은 **'짠맛 줄이기'에는 성공했지만 '칼슘 채우기'에는 실패**하고 있습니다. 
    싱겁게 먹으면서도 뼈 건강을 튼튼하게 지키기 위해 다음 두 가지를 실천해 보세요!
    
    1. **나트륨을 WHO 권장량(2,000mg) 이하로 더 낮추기**
       * 지금 많이 줄었어도 **아직 권장량보다 높기 때문에**, 국물 요리를 먹을 때는 건더기 위주로 먹고 외식 시 "싱겁게 해주세요"라고 요청하는 습관이 여전히 중요합니다.
       
    2. **'싱거운 칼슘'을 의도적으로 섭취하기**
       * 기존의 멸치볶음이나 뱅어포 같은 반찬은 나트륨 함량도 높습니다. 
       * 대신 나트륨 걱정이 적은 **우유, 요거트, 두부, 브로콜리, 청경채** 등을 식단에 자주 포함해 주세요.
    """)
    
    st.balloons()


# --- 3. 멀티페이지 네비게이션 설정 ---
page_home = st.Page(show_home, title="종합 대시보드", icon="🏠")
page_sodium = st.Page(show_sodium, title="🧂 나트륨 분석", icon="📉")
page_protein = st.Page(show_protein, title="🥩 단백질 분석", icon="💪")
page_calcium = st.Page(show_calcium, title="🥛 칼슘 분석", icon="⚠️")
page_summary = st.Page(show_summary, title="🎯 최종 총정리", icon="🏅")

pg = st.navigation([page_home, page_sodium, page_protein, page_calcium, page_summary])
st.set_page_config(page_title="한국인 식습관 20년 변천사", page_icon="📊", layout="centered")
pg.run()
