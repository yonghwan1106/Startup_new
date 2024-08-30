import streamlit as st
import streamlit.components.v1 as components

def check_device_type():
    # JavaScript를 사용하여 디바이스 유형 확인
    device_check_js = """
    <script>
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        document.querySelector('#device-type').textContent = 'mobile';
    } else {
        document.querySelector('#device-type').textContent = 'desktop';
    }
    </script>
    <p id="device-type" style="display:none;"></p>
    """
    components.html(device_check_js, height=0)
    return st.empty()

def show_pc_content():
    st.title("PC 버전 - 스타트업 내비게이터")
    st.write("PC에 최적화된 스타트업 내비게이터 화면입니다.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("창업 아이템 분석")
        st.write("AI 기반 시장 동향 및 경쟁 분석")
    with col2:
        st.subheader("인력 수급 예측")
        st.write("실시간 인력 수요 및 공급 예측")
    with col3:
        st.subheader("AI 창업 멘토")
        st.write("24/7 맞춤형 창업 조언")

def show_mobile_content():
    st.title("모바일 버전 - 스타트업 내비게이터")
    st.write("모바일에 최적화된 스타트업 내비게이터 화면입니다.")
    
    st.subheader("주요 기능")
    st.write("1. 창업 아이템 분석")
    st.write("2. 인력 수급 예측")
    st.write("3. AI 창업 멘토")
    
    if st.button("자세히 보기"):
        st.write("모바일에서는 간단한 정보만 제공됩니다. 상세 정보는 PC 버전을 이용해주세요.")

def main():
    device_type_container = check_device_type()
    
    # 디바이스 유형 확인 후 적절한 콘텐츠 표시
    if device_type_container.text == 'mobile':
        show_mobile_content()
    else:
        show_pc_content()

    # API 키 입력 (PC/모바일 공통)
    st.sidebar.title("설정")
    api_key = st.sidebar.text_input("Anthropic API 키를 입력하세요", type="password")
    if api_key:
        st.sidebar.success("API 키가 입력되었습니다.")

if __name__ == "__main__":
    main()