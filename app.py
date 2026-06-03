import streamlit as st

# 페이지 설정 (모바일 브라우저 타이틀 및 레이아웃)
st.set_page_config(
    page_title="My Finance Dashboard Hub",
    page_icon="📈",
    layout="centered" # 모바일에서는 centered가 가독성이 좋습니다.
)

# 커스텀 CSS: 카드 스타일 및 버튼 디자인
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .app-card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        border-left: 5px solid #ff4b4b;
    }
    .app-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #31333F;
        margin-bottom: 5px;
    }
    .app-desc {
        font-size: 0.9rem;
        color: #555;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 주식/ETF 분석 허브")
st.info("각 카드의 버튼을 클릭하면 해당 대시보드로 이동합니다.")

# 앱 데이터 리스트
apps = [
    {"name": "1. 레버리지 ETF MDD 매력도", "url": "https://mdd-dashboard-pd238vju6wrafee2kik6kr.streamlit.app/", "desc": "필수 레버리지 ETF의 과거 MDD 대비 현재 가격 매력도 분석"},
    {"name": "2. 레버리지 ETF 스코어 보드", "url": "https://etf-web-tracker.streamlit.app/", "desc": "전고점 대비 하락율 및 전저점 대비 상승률 조합 점수"},
    {"name": "3. S&P 100 종목 트래커", "url": "https://sp100-mdd-tracke-ictjee8mzgte7j2bahnyrh.streamlit.app/", "desc": "S&P 500 주요 종목의 가격 위치 분석 및 점수 부여"},
    {"name": "4. Nasdaq 100 종목 트래커", "url": "https://ndx-mdd-tracker-us2xqn6nmbp45cmmw4ia9l.streamlit.app/", "desc": "나스닥 100 주요 종목의 가격 위치 분석 및 점수 부여"},
    {"name": "5. 미국주식 눌림목 종목 추천", "url": "https://leading-stock-cgbnyb3uufd7uecwe6okgh.streamlit.app/", "desc": "미국 개별주 상승 추세의 눌림목 종목 추천"},
    {"name": "6. 미국주식 MDD 확인", "url": "https://find-mdd-3qryxn4gmeexn5tnbgjjhx.streamlit.app/", "desc": "미국 개별주 및 ETF 과거 MDD 확인"},
    {"name": "7. 미국주식 재무 비교", "url": "https://financial-info-ajfwuvldvohyl9q92uqlh8.streamlit.app/", "desc": "미국 개별주 vs 벤치마크 종목 주요 재무지표 비교"},
    {"name": "8. 레버리지 시뮬레이터", "url": "https://leverage-visualizer-od6veunxjczztleqmnfc5k.streamlit.app/", "desc": "가상 2배 ETF와 벤치마크 간 수익률 및 MDD 비교"},
    {"name": "9. 미국주식 수익률", "url": "https://performance-evr93cdbzj6bznha8nbmby.streamlit.app/", "desc": "미국 주식 과거 수익률 및 올해 YTD 수익률, 한국 종목도 조회 가능"},
    {"name": "10. 한국주식 재무 비교", "url": "https://k-stock-uki3zdrrysorupc3qd5w7k.streamlit.app/", "desc": "한국 개별주 vs 벤치마크 종목 주요 재무지표 비교"},
    {"name": "11. 국내외 수익률 TOP 10", "url": "https://top-stock-bye8ingxzdftv9nlkc6cpr.streamlit.app/", "desc": "미국 및 한국 주식 수익률 상위 10종목 실시간 순위"},
    {"name": "12. 미국주식 원화 계산기", "url": "https://krw-amount-jpbvqirdphbhgwkwghsgiv.streamlit.app/", "desc": "미국 주식 매수시 종목, 수량 입력시 필요한 원화 금액 자동 계산"},
    {"name": "13. 미국주식 밸류에이션 평가", "url": "https://stock-valuation-twugrgrqhxk6tvmljz3xmw.streamlit.app/", "desc": "미국 주식 과거 및 경쟁 종목 대비 밸류에이션 평가"},
    {"name": "14. 연준의 금리인상기 주도주", "url": "https://fed-hike-3enciihsqhhpqzygyvcsrk.streamlit.app/", "desc": "연준의 금리인상기 미국주식 수익률 상위 10 종목"},
    {"name": "15. 은퇴 계산기", "url": "https://retirement-calculator-cxvfymmsjzvyicxm6yktvs.streamlit.app/", "desc": "노후 준비를 위한 자금 시뮬레이션"}
]

# 앱 리스트를 순회하며 카드 생성
for app in apps:
    with st.container():
        # HTML을 사용하여 카드 디자인 적용
        st.markdown(f"""
            <div class="app-card">
                <div class="app-title">{app['name']}</div>
                <div class="app-desc">{app['desc']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # 실제 클릭 가능한 버튼 (st.link_button은 Streamlit 최신 버전 기능)
        st.link_button(f"👉 {app['name'].split('. ')[1]} 열기", app['url'], use_container_width=True)
        st.write("") # 간격 조절

# 푸터
st.caption("© 2024 My Stock Dashboards. All rights reserved.")
