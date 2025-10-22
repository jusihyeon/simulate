import streamlit as st
import numpy as np
import time

# 앱 제목
st.title("원자력 온도 시뮬레이터 (Nuclear Reactor Temperature Simulator)")

# --- 설정 영역 ---
st.sidebar.header("시뮬레이션 설정")
initial_temp = st.sidebar.slider("초기 온도 (°C)", 300, 1000, 600)
cooling_rate = st.sidebar.slider("냉각률 (°C/초)", 1, 20, 5)
reaction_intensity = st.sidebar.slider("반응 강도", 1.0, 5.0, 2.0)

# --- 시뮬레이션 표시 ---
st.write("### 시뮬레이션 실행 중...")

temperature = initial_temp
chart = st.line_chart([temperature])

# --- 30초 동안 온도 변화 ---
for second in range(30):
    # 온도 계산 (간단한 가상 모델)
    temperature += np.random.uniform(-reaction_intensity, reaction_intensity) - cooling_rate * 0.1
    chart.add_rows([temperature])
    st.write(f"시간: {second + 1}초 | 온도: {temperature:.2f}°C")
    time.sleep(0.2)

st.success("✅ 시뮬레이션 완료!")

# --- 그래프 제목 영어로 추가 ---
st.markdown("### 📈 Graph: Reactor Core Temperature over Time")
