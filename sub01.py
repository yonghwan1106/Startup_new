import streamlit as st
import anthropic
import os

def main():
    st.title("AI 기반 창업 아이템 분석기")
    
    if not st.session_state.anthropic_api_key:
        st.warning("API 키가 설정되지 않았습니다. 사이드바에서 API 키를 입력해주세요.")
        return
    
    # 창업 아이템 입력
    idea = st.text_area("분석할 창업 아이템을 입력하세요")
    
    if st.button("분석 시작"):
        if not idea:
            st.warning("창업 아이템을 입력해주세요.")
        else:
            with st.spinner("분석 중..."):
                analysis = analyze_startup_idea(idea)
                st.subheader("분석 결과")
                st.write(analysis)

def analyze_startup_idea(idea):
    client = anthropic.Anthropic(api_key=st.session_state.anthropic_api_key)
    prompt = f"다음 창업 아이템에 대해 분석해주세요: {idea}\n\n분석 항목:\n1. 시장 동향\n2. 경쟁 상황\n3. 성장 가능성\n4. 잠재적 위험 요소\n5. 개선 제안"
    
    response = client.completions.create(
        model="claude-3-sonnet-20240229",
        max_tokens_to_sample=1000,
        prompt=prompt
    )
    return response.completion

if __name__ == "__main__":
    main()