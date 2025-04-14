import streamlit as st
from datetime import datetime, timedelta
import time

st.title("RUANG 3 SMAN 1 REJANG LEBONG")
st.write("SIPANDAI are detecting SIMALAS--Sedang dalam proses pengumpulan data!")

# Gambar yang akan ditampilkan saat tidak ada data
NO_DATA_IMAGE = "images/SIPANDAI.jpg"

last_data_time = st.session_state.get("last_data_time", None)

# Simulasi tombol untuk menerima data (hanya untuk demo)
if st.button("Simulasikan Data Masuk"):
    st.session_state.last_data_time = datetime.now()
    st.success("Data masuk!")

last_data_time = st.session_state.get("last_data_time", None)

threshold = timedelta(seconds=5)

if last_data_time is None or datetime.now() - last_data_time > threshold:
    # Jika tidak ada data masuk atau sudah lewat threshold → tampilkan gambar
    st.image(NO_DATA_IMAGE, caption="belum ada data yang masuk.", width=300)
else:
    st.success("Data masih masuk secara aktif.")
