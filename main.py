import streamlit as st
import streamlit.components.v1 as components
import sub01, sub02, sub03, sub04, sub05, sub06, sub07

# Custom CSS for improved design
def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="스타트업 내비게이터", page_icon="🚀", layout="wide")
    local_css("style.css")  # Make sure to create this CSS file

    # Header
    st.markdown("<h1 class='main-title'>스타트업 내비게이터</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>당신의 창업 여정을 AI로 지원합니다</p>", unsafe_allow_html=True)

    # Sidebar menu
    with st.sidebar:
        st.markdown("<h2 class='sidebar-title'>메뉴</h2>", unsafe_allow_html=True)
        menu = st.radio(
            "",
            ("홈", "창업 아이템 분석", "인력 수급 예측", "AI 창업 멘토", 
             "정부 지원 정책", "사업 성과 시뮬레이터", "인재 매칭", "창업 커뮤니티")
        )

    # API 키 입력 (공통)
    if 'anthropic_api_key' not in st.session_state:
        st.session_state.anthropic_api_key = ""
    
    st.sidebar.title("설정")
    api_key = st.sidebar.text_input("Anthropic API 키를 입력하세요", type="password", key="api_key_input")
    if api_key:
        st.session_state.anthropic_api_key = api_key
        st.sidebar.success("API 키가 입력되었습니다.")

    # 메뉴에 따른 페이지 표시
    if menu == "홈":
        show_home()
    elif menu == "창업 아이템 분석":
        sub01.main()
    elif menu == "인력 수급 예측":
        sub02.show_workforce_prediction()
    elif menu == "AI 창업 멘토":
        sub03.show_ai_mentor()
    elif menu == "정부 지원 정책":
        sub04.show_government_support()
    elif menu == "사업 성과 시뮬레이터":
        sub05.show_business_simulator()
    elif menu == "인재 매칭":
        sub06.show_talent_matching()
    elif menu == "창업 커뮤니티":
        sub07.show_startup_community()

def show_home():
    st.markdown("<h2 class='welcome-title'>환영합니다!</h2>", unsafe_allow_html=True)
    st.markdown("<p class='welcome-text'>스타트업 내비게이터는 AI 기술을 활용하여 당신의 창업 여정을 지원합니다.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h3>창업 아이템 분석</h3>
            <p>시장 동향과 경쟁 상황을 AI로 분석합니다.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='info-card'>
            <h3>AI 창업 멘토</h3>
            <p>24/7 당신의 질문에 답변하는 AI 멘토</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='info-card'>
            <h3>사업 성과 시뮬레이터</h3>
            <p>다양한 시나리오에 따른 사업 성과를 예측합니다.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<h2 class='start-title'>시작하기</h2>", unsafe_allow_html=True)
    st.markdown("<p class='start-text'>왼쪽 사이드바에서 원하는 기능을 선택하세요.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
