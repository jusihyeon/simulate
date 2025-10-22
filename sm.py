import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import os

# 🔹 1. Windows 한글 폰트 설정 (맑은 고딕)
font_path = "C:/Windows/Fonts/malgun.ttf"  # 기본 설치 폰트 경로
if os.path.exists(font_path):
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)
    plt.rcParams['axes.unicode_minus'] = False
else:
    st.warning("⚠️ 한글 폰트를 찾을 수 없습니다. 그래프의 글자가 깨질 수 있습니다.")

# 🔹 2. 앱 기본 정보
st.title("🔬 원자력 에너지 시뮬레이터 (기초편)")
st.markdown("**우라늄-235 핵분열 시 발생하는 에너지를 계산해보세요.**")

# 상수 정의
AVOGADRO = 6.022e23           # 아보가드로 수
U235_MOLAR_MASS = 235e-3      # kg/mol
ENERGY_PER_FISSION = 200 * 1.602e-13  # 200 MeV → J

# 🔹 3. 사용자 입력
mass = st.slider("우라늄-235 질량 (kg)", min_value=0.001, max_value=5.0, step=0.001, value=0.1)

# 🔹 4. 계산식
num_atoms = (mass / U235_MOLAR_MASS) * AVOGADRO
total_energy_joule = num_atoms * ENERGY_PER_FISSION
total_energy_kwh = total_energy_joule / 3.6e6  # J → kWh
coal_equiv = total_energy_kwh / 8  # 석탄 1kg ≈ 8kWh

# 🔹 5. 결과 표시
st.subheader("결과 요약")
st.write(f"☢️ 총 발생 에너지: **{total_energy_kwh:,.2e} kWh**")
st.write(f"🔥 석탄으로 환산 시: 약 **{coal_equiv:,.2e} kg 석탄**과 동일")

# 🔹 6. 그래프 시각화
masses = [i * 0.1 for i in range(1, 51)]  # 0.1~5kg
energies = [
    ((m / U235_MOLAR_MASS) * AVOGADRO * ENERGY_PER_FISSION) / 3.6e6
    for m in masses
]

fig, ax = plt.subplots()
ax.plot(masses, energies, color="orange", linewidth=2, label="핵분열 에너지 곡선")

# 현재 슬라이더 위치 표시 (빨간 점)
current_energy = ((mass / U235_MOLAR_MASS) * AVOGADRO * ENERGY_PER_FISSION) / 3.6e6
ax.scatter([mass], [current_energy], color="red", s=80, label="현재 선택값")

# 🔹 한글 제목 및 축 이름
ax.set_xlabel("우라늄 질량 (kg)")
ax.set_ylabel("발생 에너지 (kWh)")
ax.set_title("질량에 따른 핵분열 에너지")
ax.legend()

st.pyplot(fig)

# 🔹 출처
st.caption("※ 참고: 핵분열 1회당 약 200 MeV 에너지 방출 (IAEA 자료 기준)")
