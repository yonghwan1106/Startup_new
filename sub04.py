import streamlit as st
import anthropic

if 'anthropic_api_key' not in st.session_state:
    st.session_state.anthropic_api_key = ""

def set_api_key():
    st.session_state.anthropic_api_key = st.text_input("Anthropic API 키를 입력하세요:", type="password")
    if st.session_state.anthropic_api_key:
        st.success("API 키가 설정되었습니다.")

def get_government_support(industry, stage):
    client = anthropic.Anthropic(api_key=st.session_state.anthropic_api_key)
    prompt = f"""
    당신은 정부 지원 정책 전문가입니다. {industry} 산업의 {stage} 단계 스타트업을 위한 정부 지원 정책을 추천해주세요.
    
    다음 정보를 포함해주세요:
    1. 정책명
    2. 지원 내용
    3. 신청 자격
    4. 신청 방법
    5. 주의사항
    
    3개의 정책을 추천해주세요.
    """
    
    response = client.completions.create(
        model="claude-3-sonnet-20240229",
        prompt=prompt,
        max_tokens_to_sample=1500,
    )
    
    return response.completion

def show_government_support():
    st.title("정부 지원 정책 추천")
    
    if not st.session_state.anthropic_api_key:
        st.warning("API 키가 설정되지 않았습니다. 먼저 API 키를 설정해주세요.")
        set_api_key()
    else:
        industry = st.selectbox("산업을 선택하세요:", ["IT", "금융", "의료", "교육", "제조"])
        stage = st.selectbox("창업 단계를 선택하세요:", ["아이디어", "초기", "성장", "확장"])
        
        if st.button("정책 추천 받기"):
            with st.spinner("정부 지원 정책을 검색 중입니다..."):
                policies = get_government_support(industry, stage)
            
            st.subheader("추천 정부 지원 정책")
            st.write(policies)

if __name__ == "__main__":
    show_government_support()