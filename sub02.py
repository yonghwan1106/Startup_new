import streamlit as st
import anthropic
import pandas as pd
import plotly.express as px
from datetime import datetime

# Anthropic API 키 설정 (세션 상태로 관리)
if 'anthropic_api_key' not in st.session_state:
    st.session_state.anthropic_api_key = ""

def set_api_key():
    st.session_state.anthropic_api_key = st.text_input("Anthropic API 키를 입력하세요:", type="password")
    if st.session_state.anthropic_api_key:
        st.success("API 키가 설정되었습니다.")

def predict_workforce(industry, role, timeframe):
    client = anthropic.Anthropic(api_key=st.session_state.anthropic_api_key)
    prompt = f"""
    당신은 인력 수급 예측 전문가입니다. {industry} 산업에서 {role} 역할에 대한 향후 {timeframe}개월 동안의 인력 수요를 예측해주세요. 
    다음 정보를 포함해주세요:
    1. 예상 인력 수요 (수치로 표현)
    2. 필요한 주요 스킬셋 (5개)
    3. 적정 임금 범위 (최소값과 최대값)
    4. 채용 난이도 (1-10 척도)
    5. 인재 확보 전략 (3가지 제안)
    
    결과는 JSON 형식으로 제공해주세요.
    """
    
    response = client.completions.create(
        model="claude-3-sonnet-20240229",
        prompt=prompt,
        max_tokens_to_sample=1000,
    )
    
    return eval(response.completion)  # JSON 문자열을 Python 딕셔너리로 변환

def show_workforce_prediction():
    st.title("동적 인력 수급 예측 시스템")
    
    if not st.session_state.anthropic_api_key:
        st.warning("API 키가 설정되지 않았습니다. 먼저 API 키를 설정해주세요.")
        set_api_key()
    else:
        industry = st.selectbox("산업을 선택하세요:", ["IT", "금융", "의료", "교육", "제조"])
        role = st.text_input("예측하고자 하는 역할을 입력하세요:")
        timeframe = st.slider("예측 기간 (월):", 1, 24, 6)
        
        if st.button("예측 시작"):
            with st.spinner("예측 중..."):
                result = predict_workforce(industry, role, timeframe)
            
            st.subheader("예측 결과")
            
            # 인력 수요 그래프
            df = pd.DataFrame({
                '월': range(1, timeframe + 1),
                '예상 인력 수요': [result['예상 인력 수요']] * timeframe
            })
            fig = px.line(df, x='월', y='예상 인력 수요', title=f"{industry} 산업의 {role} 역할 인력 수요 예측")
            st.plotly_chart(fig)
            
            # 스킬셋
            st.subheader("필요 스킬셋")
            for skill in result['필요한 주요 스킬셋']:
                st.markdown(f"- {skill}")
            
            # 임금 범위
            st.subheader("적정 임금 범위")
            st.write(f"최소: {result['적정 임금 범위']['최소값']}원 ~ 최대: {result['적정 임금 범위']['최대값']}원")
            
            # 채용 난이도
            st.subheader("채용 난이도")
            st.progress(result['채용 난이도'] / 10)
            st.write(f"{result['채용 난이도']}/10")
            
            # 인재 확보 전략
            st.subheader("인재 확보 전략")
            for strategy in result['인재 확보 전략']:
                st.markdown(f"- {strategy}")

if __name__ == "__main__":
    show_workforce_prediction()