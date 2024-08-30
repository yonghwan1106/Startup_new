import streamlit as st
import anthropic

if 'anthropic_api_key' not in st.session_state:
    st.session_state.anthropic_api_key = ""

def set_api_key():
    st.session_state.anthropic_api_key = st.text_input("Anthropic API 키를 입력하세요:", type="password")
    if st.session_state.anthropic_api_key:
        st.success("API 키가 설정되었습니다.")

def generate_community_content(topic):
    client = anthropic.Anthropic(api_key=st.session_state.anthropic_api_key)
    prompt = f"""
    당신은 창업 커뮤니티 매니저입니다. '{topic}'에 관한 창업자들의 토론을 시뮬레이션해주세요.
    
    다음 내용을 포함해주세요:
    1. 토론 주제 소개
    2. 3명의 가상의 창업자들의 의견 (찬성, 반대, 중립)
    3. 각 의견에 대한 간단한 논평
    4. 토론의 결론 및 시사점
    
    결과는 마크다운 형식으로 제공해주세요.
    """
    
    response = client.completions.create(
        model="claude-3-sonnet-20240229",
        prompt=prompt,
        max_tokens_to_sample=1500,
    )
    
    return response.completion

def show_startup_community():
    st.title("창업 커뮤니티")
    
    if not st.session_state.anthropic_api_key:
        st.warning("API 키가 설정되지 않았습니다. 먼저 API 키를 설정해주세요.")
        set_api_key()
    else:
        topic = st.text_input("토론하고 싶은 창업 관련 주제를 입력하세요:")
        
        if st.button("토론 시작"):
            with st.spinner("창업자들의 토론을 생성 중입니다..."):
                discussion = generate_community_content(topic)
            
            st.subheader("가상 창업자 토론")
            st.markdown(discussion)
        
        st.subheader("실제 커뮤니티 기능")
        st.write("이 섹션에서는 실제 사용자들이 참여할 수 있는 커뮤니티 기능을 구현할 수 있습니다.")
        st.write("예: 게시판, 댓글 시스템, 실시간 채팅 등")

if __name__ == "__main__":
    show_startup_community()