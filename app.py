import streamlit as st
import pandas as pd
from PIL import Image

# 페이지 설정
st.set_page_config(page_title="스타트업 내비게이터", page_icon="🚀", layout="wide")

# 사용자 정의 CSS 추가
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        margin-bottom: 1rem;
    }
    .feature-card {
        background-color: #F5F5F5;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# 헤더
st.markdown("<h1 class='main-header'>스타트업 내비게이터에 오신 것을 환영합니다!</h1>", unsafe_allow_html=True)

# 소개문
st.markdown("스타트업 내비게이터는 당신의 창업 여정을 안내하는 AI 기반 플랫폼입니다.")

# 주요 기능 섹션
st.markdown("<h2 class='sub-header'>주요 기능</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='feature-card'>
        <div class='feature-icon'>🔍</div>
        <h3>AI 기반 창업 아이템 분석기</h3>
        <p>실시간 시장 동향 분석 및 예측</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-card'>
        <div class='feature-icon'>👥</div>
        <h3>동적 인력 수급 예측 시스템</h3>
        <p>맞춤형 인재 수요 예측 및 추천</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-card'>
        <div class='feature-icon'>🤖</div>
        <h3>AI 창업 멘토</h3>
        <p>24/7 질의응답 및 맞춤형 조언</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-card'>
        <div class='feature-icon'>📊</div>
        <h3>AI 기반 사업 성과 시뮬레이터</h3>
        <p>다양한 시나리오에 따른 성과 분석</p>
    </div>
    """, unsafe_allow_html=True)

# 시작하기 버튼
st.markdown("<br>", unsafe_allow_html=True)
if st.button("시작하기", key="start_button", help="클릭하여 스타트업 내비게이터 사용을 시작하세요"):
    st.success("환영합니다! 스타트업 내비게이터를 시작합니다.")

# 푸터
st.markdown("<br><hr><p style='text-align: center;'>© 2023 스타트업 내비게이터. All rights reserved.</p>", unsafe_allow_html=True)