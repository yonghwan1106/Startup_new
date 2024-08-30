import streamlit as st
import sub01, sub02, sub03, sub04, sub05, sub06, sub07

def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def change_menu(new_menu):
    st.session_state.menu = new_menu

def main():
    st.set_page_config(page_title="스타트업 내비게이터", page_icon="🚀", layout="wide")
    local_css("style.css")

    if 'menu' not in st.session_state:
        st.session_state.menu = "홈"

    with st.sidebar:
        st.markdown("<h2 class='sidebar-title'>🚀 스타트업 내비게이터</h2>", unsafe_allow_html=True)
        menu = st.radio(
            "",
            ("홈", "창업 아이템 분석", "인력 수급 예측", "AI 창업 멘토", 
             "정부 지원 정책", "사업 성과 시뮬레이터", "인재 매칭", "창업 커뮤니티"),
            key="menu"
        )

    if 'anthropic_api_key' not in st.session_state:
        st.session_state.anthropic_api_key = ""
    
    st.sidebar.title("설정")
    api_key = st.sidebar.text_input("Anthropic API 키를 입력하세요", type="password", key="api_key_input")
    if api_key:
        st.session_state.anthropic_api_key = api_key
        st.sidebar.success("API 키가 입력되었습니다.")

    if st.session_state.menu == "홈":
        show_home()
    elif st.session_state.menu == "창업 아이템 분석":
        sub01.main()
    elif st.session_state.menu == "인력 수급 예측":
        sub02.show_workforce_prediction()
    elif st.session_state.menu == "AI 창업 멘토":
        sub03.show_ai_mentor()
    elif st.session_state.menu == "정부 지원 정책":
        sub04.show_government_support()
    elif st.session_state.menu == "사업 성과 시뮬레이터":
        sub05.show_business_simulator()
    elif st.session_state.menu == "인재 매칭":
        sub06.show_talent_matching()
    elif st.session_state.menu == "창업 커뮤니티":
        sub07.show_startup_community()

def show_home():
    st.markdown("<h1 class='main-title'>🚀 스타트업 내비게이터</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>당신의 창업 여정을 AI로 지원합니다</p>", unsafe_allow_html=True)
    
    menu_items = [
        ("💡 창업 아이템 분석", "AI 기술을 활용하여 당신의 창업 아이디어의 시장 가능성을 분석합니다."),
        ("👥 인력 수급 예측", "데이터 기반으로 필요한 인력을 예측하고 최적의 채용 전략을 제시합니다."),
        ("🤖 AI 창업 멘토", "24/7 이용 가능한 AI 멘토가 창업 관련 질문에 답변합니다."),
        ("📊 정부 지원 정책", "맞춤형 정부 지원 정책을 찾아 안내해드립니다."),
        ("📈 사업 성과 시뮬레이터", "다양한 시나리오에 따른 사업 성과를 예측하고 분석합니다."),
        ("🎯 인재 매칭", "AI 기반 매칭 시스템으로 최적의 인재를 추천합니다."),
        ("🌐 창업 커뮤니티", "다른 창업자들과 경험을 공유하고 네트워킹할 수 있는 공간입니다.")
    ]

    for item in menu_items:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.button(item[0], key=item[0], on_click=change_menu, args=(item[0].split(' ')[1],))
        with col2:
            st.markdown(f"<p>{item[1]}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()