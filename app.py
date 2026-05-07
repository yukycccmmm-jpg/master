import streamlit as st
from dotenv import load_dotenv

from src.scenario_generator import ScenarioGenerator, ScenarioRequest

load_dotenv()

st.set_page_config(page_title="투자 시나리오 생성기", page_icon="📊", layout="wide")

st.title("📊 투자 시나리오 생성기")
st.caption("종목과 투자 논리를 입력하면 Bull/Base/Bear 시나리오를 생성합니다.")

with st.sidebar:
    st.subheader("설정")
    model = st.text_input("모델", value="gpt-4.1-mini")
    st.markdown("- API 키는 `.env`의 `OPENAI_API_KEY`를 사용합니다.")

col1, col2 = st.columns([1, 1])
with col1:
    ticker = st.text_input("1) 종목 입력", placeholder="예: AAPL 또는 TSLA")
with col2:
    st.write("")
    st.write("")
    st.info("티커 외에 기업명으로도 가능하지만, 티커 권장")

thesis = st.text_area(
    "2) 투자 논리 입력",
    placeholder="예: AI 수요 증가로 데이터센터 매출 성장, 다만 밸류에이션 부담 존재...",
    height=200,
)

run = st.button("3) 시나리오 생성", type="primary", use_container_width=True)

if run:
    if not ticker or not thesis:
        st.warning("종목과 투자 논리를 모두 입력해주세요.")
    else:
        try:
            with st.spinner("시나리오 생성 중..."):
                generator = ScenarioGenerator()
                result = generator.generate(ScenarioRequest(ticker=ticker, thesis=thesis, model=model))

            st.success("생성 완료!")

            st.subheader("요약")
            st.write(result.get("summary", "-"))

            st.subheader("4) Bull / Base / Bear 시나리오")
            scenarios = result.get("scenarios", [])
            scenario_cols = st.columns(3)

            for idx, name in enumerate(["Bull", "Base", "Bear"]):
                target = next((s for s in scenarios if s.get("name", "").lower() == name.lower()), None)
                with scenario_cols[idx]:
                    st.markdown(f"### {name}")
                    if target:
                        st.metric("확률", target.get("probability", "-"))
                        st.markdown(f"**촉발 요인**\n\n{target.get('trigger', '-')}" )
                        st.markdown(f"**결과**\n\n{target.get('outcome', '-')}" )
                        st.markdown("**핵심 지표**")
                        for metric in target.get("key_metrics", []):
                            st.write(f"- {metric}")
                    else:
                        st.write("데이터 없음")

            st.subheader("5) 핵심 변수 정리")
            variables = result.get("key_variables", [])
            for v in variables:
                with st.container(border=True):
                    st.markdown(f"**{v.get('variable', '-') }**")
                    st.write(f"- 중요 이유: {v.get('why_it_matters', '-')}")
                    st.write(f"- 관찰 포인트: {v.get('watch_points', '-')}")

            with st.expander("주요 리스크"):
                for risk in result.get("risks", []):
                    st.write(f"- {risk}")

            with st.expander("다음 점검 체크리스트"):
                for item in result.get("next_checklist", []):
                    st.write(f"- {item}")

            st.download_button(
                "JSON 다운로드",
                data=str(result),
                file_name=f"{ticker}_scenarios.json",
                use_container_width=True,
            )

        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
