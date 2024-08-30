import streamlit as st
import anthropic

if 'anthropic_api_key' not in st.session_state:
    st.session_state.anthropic_api_key = ""

def set_api_key():
    st.session_state.anthropic_api_key = st.text_input("Anthropic API 키를 입력하세요:", type="password")
    if st.session_state.anthropic_api_key:
        st.success("API 키가 설정되었습니다.")

def match_talent(job_description, company_culture):
    client = anthropic.Anthropic(api_key=st.session_state.anthropic_api_key)
    prompt = f"""
    당신은 인재 매칭 전문가입니다. 다음 직무 설명과 회사 문화를 바탕으로 적합한 인재 프로필을 추천해주세요:

    직무 설명: {job_description}
    회사 문화: {company_culture}

    다음 정보를 포함하는 3명의 가상의 후보자 프로필을 생성해주세요:
    1. 이름 (가명)
    2. 경력 요약
    3. 주요 스킬
    4. 강점
    5. 잠재적 약점
    6. 문화적 적합성

    결과는 JSON 형식으로 제공해주세요.
    """
    
    response = client.completions.create(
        model="claude-3-sonnet-20240229",
        prompt=prompt,
        max_tokens_to_sample=1500,
    )
    
    return eval(response.completion)  # JSON 문자열을 Python 딕셔너리로 변환

def show_talent_matching():
    st.title("AI 기반 인재 매칭")
    
    if not st.session_state.anthropic_api_key:
        st.warning("API 키가 설정되지 않았습니다. 먼저 API 키를 설정해주세요.")
        set_api_key()
    else:
        job_description = st.text_area("직무 설명을 입력하세요:")
        company_culture = st.text_area("회사 문화를 설명해주세요:")
        
        if st.button("인재 매칭 시작"):
            with st.spinner("적합한 인재를 찾고 있습니다..."):
                candidates = match_talent(job_description, company_culture)
            
            st.subheader("추천 후보자")
            for i, candidate in enumerate(candidates, start=1):
                st.write(f"후보자 {i}: {candidate['이름']}")
                st.write(f"경력 요약: {candidate['경력 요약']}")
                st.write(f"주요 스킬: {', '.join(candidate['주요 스킬'])}")
                st.write(f"강점: {candidate['강점']}")
                st.write(f"잠재적 약점: {candidate['잠재적 약점']}")
                st.write(f"문화적 적합성: {candidate['문화적 적합성']}")
                st.write("---")

if __name__ == "__main__":
    show_talent_matching()