import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 🔹 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우
plt.rcParams['axes.unicode_minus'] = False     # 마이너스 깨짐 방지

# 앱 제목
st.title("🔬 원자력 에너지 시뮬레이터 (기초편)")
st.markdown("**우라늄-235 핵분열 시 발생하는 에너지를 계산해보세요.**")

# 상수 정의
AVOGADRO = 6.022e23           # 아보가드로 수
U235_MOLAR_MASS = 235e-3      # kg/mol
ENERGY_PER_FISSION = 200 * 1.602e-13  # 200 MeV → J

# 사용자 입력: 우라늄 질량 (kg)
mass = st.slider("우라늄-235 질량 (kg)", min_value=0.001, max_value=5.0, step=0.001, value=0.1)

# 계산
num_atoms = (mass / U235_MOLAR_MASS) * AVOGADRO
total_energy_joule = num_atoms * ENERGY_PER_FISSION
total_energy_kwh = total_energy_joule / 3.6e6  # J → kWh

# 비교: 석탄 에너지 (1kg 석탄 ≈ 8 kWh)
coal_equiv = total_energy_kwh / 8

# 결과 출력
st.subheader("결과 요약")
st.write(f"☢️ 총 발생 에너지: **{total_energy_kwh:,.2e} kWh**")
st.write(f"🔥 석탄으로 환산 시: 약 **{coal_equiv:,.2e} kg 석탄**과 동일")

# 그래프 시각화
masses = [i * 0.1 for i in range(1, 51)]  # 0.1~5kg
energies = [
    ((m / U235_MOLAR_MASS) * AVOGADRO * ENERGY_PER_FISSION) / 3.6e6
    for m in masses
]

fig, ax = plt.subplots()
ax.plot(masses, energies, color="orange", linewidth=2, label="핵분열 에너지 곡선")

# 현재 선택된 질량 위치에 점 표시
current_energy = ((mass / U235_MOLAR_MASS) * AVOGADRO * ENERGY_PER_FISSION) / 3.6e6
ax.scatter([mass], [current_energy], color="red", s=80, label="현재 선택값")

ax.set_xlabel("우라늄 질량 (kg)")
ax.set_ylabel("발생 에너지 (kWh)")
ax.set_title("질량에 따른 핵분열 에너지")
ax.legend()
st.pyplot(fig)

# 출처
st.caption("※ 참고: 핵분열 1회당 약 200 MeV 에너지 방출 (IAEA 자료 기준)")
