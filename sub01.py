import streamlit as st
import anthropic
import os

def main():
    st.title('🚀 AI 기반 창업 아이템 분석기')
    
    if not st.session_state.get('anthropic_api_key'):
        st.warning("API 키가 설정되지 않았습니다. 사이드바에서 API 키를 입력해주세요.")
        return
    
    # 창업 아이템 입력
    idea = st.text_area("분석할 창업 아이템을 입력하세요")
    
    if st.button("분석 시작"):
        if not idea:
            st.warning("창업 아이템을 입력해주세요.")
        else:
            with st.spinner("분석 중..."):
                try:
                    analysis = analyze_startup_idea(idea)
                    st.subheader("분석 결과")
                    st.write(analysis)
                except Exception as e:
                    st.error(f"분석 중 오류가 발생했습니다: {str(e)}")

def analyze_startup_idea(idea):
    client = anthropic.Anthropic(api_key=st.session_state.anthropic_api_key)
    
    prompt = f"""As an AI startup analyst, provide a comprehensive analysis for the startup idea: "{idea}". Structure your response in the following format:

    ## 1. 시장 동향 분석

    - 현재 국내 및 글로벌 시장 규모 (금액):
    - 주요 소비자 트렌드:
    - 시장을 주도하는 핵심 기술이나 혁신 요소:

    ## 2. 경쟁 상황 평가
    - 국내외 주요 경쟁사와 각 기업의 강점 및 약점:
    - 시장 점유율 상위 3개 기업의 점유율:
    - 주요 진입 장벽:
    - 대체 상품/서비스의 위협 정도:

    ## 3. 성장 전망 예측
    - 향후 3년, 5년간의 예상 시장 성장률:
    - 낙관적, 중립적, 비관적 시나리오별 성장 전망:
    - 시장 성장에 영향을 미칠 수 있는 주요 외부 요인:

    ## 4. 성공 사례 분석
    - 성공한 국내외 기업 사례:
    - 각 성공 사례의 주요 성공 요인:
    - 초기 진입 전략과 성장 과정에서의 주요 전환점:
    - 경쟁사와의 차별화 포인트:

    ## 5. 실패 사례 분석
    - 실패한 국내외 기업 사례:
    - 각 실패 사례의 주요 실패 원인:
    - 실패를 극복하기 위한 구체적인 방안:
    - 각 실패 사례에서 얻을 수 있는 핵심 교훈:

    ## 6. 핵심 성공 요인 도출
    - 핵심 성공 요인 (1-10 척도의 중요도 포함):
    - 제시된 창업 아이템의 각 성공 요인에 대한 적합성 평가 및 개선 방안:
    - 아이템의 장기적 성공을 위한 전략적 제언:

    Provide detailed and data-driven insights for each section. Use realistic but imaginary data where specific numbers are required. Ensure the analysis is comprehensive and tailored to the specific startup idea."""

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4000,
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.content[0].text

if __name__ == "__main__":
    main()