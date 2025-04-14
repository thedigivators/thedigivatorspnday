import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Judul dashboard
st.set_page_config(page_title="Dashboard Deteksi Kecurangan Ujian", layout="wide")
st.title("RUANG 1 SMAN 1 REJANG LEBONG")
st.write("SIPANDAI are detecting SIMALAS")

# ==== DATA DUMMY ====
jumlah_siswa_kelas = 30
jumlah_terdeteksi_total = 7

# Membuat data waktu deteksi 1 jam terakhir
def generate_data_1_jam():
    now = datetime.now()
    data = []
    for i in range(6):  # 6 interval (10 menit)
        waktu = now - timedelta(minutes=10 * i)
        terdeteksi = random.randint(0, 3)
        data.append({"waktu": waktu.strftime("%H:%M"), "terdeteksi": terdeteksi})
    return list(reversed(data))

data_jam = generate_data_1_jam()
df = pd.DataFrame(data_jam)

# ==== KARTU STATISTIK ====
col1, col2 = st.columns(2)
with col1:
    st.metric("👨‍🎓 Jumlah Siswa di Kelas", jumlah_siswa_kelas)
with col2:
    st.metric("🚨 Siswa Terdeteksi Mencontek", jumlah_terdeteksi_total)

st.markdown("---")

# ==== GRAFIK DETEKSI PER JAM ====
st.subheader("📈 Grafik Deteksi Siswa Mencontek per 10 Menit (1 Jam Terakhir)")

st.line_chart(df.set_index("waktu"))

# ==== TABEL OPSIONAL ====
with st.expander("📋 Lihat Detail Tabel Deteksi per Waktu"):
    st.table(df)












