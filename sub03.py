import streamlit as st
import anthropic

if 'anthropic_api_key' not in st.session_state:
    st.session_state.anthropic_api_key = ""

def set_api_key():
    st.session_state.anthropic_api_key = st.text_input("Anthropic API 키를 입력하세요:", type="password")
    if st.session_state.anthropic_api_key:
        st.success("API 키가 설정되었습니다.")

def get_ai_mentor_advice(question):
    client = anthropic.Anthropic(api_key=st.session_state.anthropic_api_key)
    prompt = f"""
    당신은 경험 많은 창업 멘토입니다. 다음 질문에 대해 조언해주세요: {question}
    
    조언은 다음 형식으로 제공해주세요:
    1. 핵심 조언
    2. 세부 설명
    3. 주의사항
    4. 추천 리소스
    """
    
    response = client.completions.create(
        model="claude-3-sonnet-20240229",
        prompt=prompt,
        max_tokens_to_sample=1000,
    )
    
    return response.completion

def show_ai_mentor():
    st.title("AI 창업 멘토")
    
    if not st.session_state.anthropic_api_key:
        st.warning("API 키가 설정되지 않았습니다. 먼저 API 키를 설정해주세요.")
        set_api_key()
    else:
        question = st.text_area("창업과 관련된 질문을 입력하세요:")
        
        if st.button("조언 받기"):
            with st.spinner("AI 멘토가 답변을 생성 중입니다..."):
                advice = get_ai_mentor_advice(question)
            
            st.subheader("AI 멘토의 조언")
            st.write(advice)

if __name__ == "__main__":
    show_ai_mentor()