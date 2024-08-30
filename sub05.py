import streamlit as st
import anthropic
import pandas as pd
import plotly.express as px

if 'anthropic_api_key' not in st.session_state:
    st.session_state.anthropic_api_key = ""

def set_api_key():
    st.session_state.anthropic_api_key = st.text_input("Anthropic API 키를 입력하세요:", type="password")
    if st.session_state.anthropic_api_key:
        st.success("API 키가 설정되었습니다.")

def simulate_business_performance(industry, investment, timeframe):
    client = anthropic.Anthropic(api_key=st.session_state.anthropic_api_key)
    prompt = f"""
    당신은 사업 성과 예측 전문가입니다. {industry} 산업에서 초기 투자금 {investment}원으로 시작한 스타트업의 향후 {timeframe}년간의 성과를 예측해주세요.
    
    다음 정보를 연도별로 제공해주세요:
    1. 예상 매출
    2. 예상 비용
    3. 예상 순이익
    4. 주요 성과 지표
    
    결과는 JSON 형식으로 제공해주세요.
    """
    
    response = client.completions.create(
        model="claude-3-sonnet-20240229",
        prompt=prompt,
        max_tokens_to_sample=1500,
    )
    
    return eval(response.completion)  # JSON 문자열을 Python 딕셔너리로 변환

def show_business_simulator():
    st.title("사업 성과 시뮬레이터")
    
    if not st.session_state.anthropic_api_key:
        st.warning("API 키가 설정되지 않았습니다. 먼저 API 키를 설정해주세요.")
        set_api_key()
    else:
        industry = st.selectbox("산업을 선택하세요:", ["IT", "금융", "의료", "교육", "제조"])
        investment = st.number_input("초기 투자금(원):", min_value=1000000, max_value=10000000000, value=100000000, step=1000000)
        timeframe = st.slider("예측 기간 (년):", 1, 10, 5)
        
        if st.button("시뮬레이션 시작"):
            with st.spinner("사업 성과를 시뮬레이션 중입니다..."):
                result = simulate_business_performance(industry, investment, timeframe)
            
            st.subheader("시뮬레이션 결과")
            
            # 매출, 비용, 순이익 그래프
            df = pd.DataFrame(result)
            fig = px.line(df, x=df.index, y=['예상 매출', '예상 비용', '예상 순이익'], title="연도별 재무 성과")
            st.plotly_chart(fig)
            
            # 주요 성과 지표
            st.subheader("주요 성과 지표")
            for year, kpi in enumerate(result['주요 성과 지표'], start=1):
                st.write(f"{year}년차: {kpi}")

if __name__ == "__main__":
    show_business_simulator()