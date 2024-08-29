import streamlit as st
import pandas as pd
import requests
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Anthropic API 설정
anthropic = Anthropic()

# 세션 상태 초기화
if 'user' not in st.session_state:
    st.session_state['user'] = None

# 사용자 인증 함수
def authenticate(username, password):
    # 실제 구현에서는 데이터베이스 확인 등의 로직이 필요합니다
    if username == "test" and password == "password":
        return True
    return False

# 로그인 폼
def login_form():
    with st.form("login_form"):
        username = st.text_input("사용자명")
        password = st.text_input("비밀번호", type="password")
        submit = st.form_submit_button("로그인")
        
        if submit:
            if authenticate(username, password):
                st.session_state['user'] = username
                st.success("로그인 성공!")
            else:
                st.error("잘못된 사용자명 또는 비밀번호입니다.")

# AI 창업 아이템 분석 함수
def analyze_startup_idea(idea):
    prompt = f"{HUMAN_PROMPT}다음 창업 아이템에 대해 분석해주세요: {idea}\n\n분석 항목:\n1. 시장 동향\n2. 경쟁 상황\n3. 성장 가능성\n4. 잠재적 위험 요소\n5. 개선 제안{AI_PROMPT}"
    
    response = anthropic.completions.create(
        model="claude-3-sonnet-20240229",
        max_tokens_to_sample=1000,
        prompt=prompt
    )
    return response.completion

# 메인 앱
def main():
    st.title("AI 기반 창업 아이템 분석기")
    
    # Anthropic API 키 입력
    api_key = st.text_input("Anthropic API 키를 입력하세요", type="password")
    if api_key:
        os.environ["ANTHROPIC_API_KEY"] = api_key
    
    if st.session_state['user'] is None:
        login_form()
    else:
        st.write(f"환영합니다, {st.session_state['user']}님!")
        
        # 창업 아이템 입력
        idea = st.text_area("분석할 창업 아이템을 입력하세요")
        
        if st.button("분석 시작"):
            if not idea:
                st.warning("창업 아이템을 입력해주세요.")
            elif not api_key:
                st.warning("Anthropic API 키를 입력해주세요.")
            else:
                with st.spinner("분석 중..."):
                    analysis = analyze_startup_idea(idea)
                    st.subheader("분석 결과")
                    st.write(analysis)
        
        if st.button("로그아웃"):
            st.session_state['user'] = None
            st.experimental_rerun()

if __name__ == "__main__":
    main()
