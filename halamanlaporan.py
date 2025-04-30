import streamlit as st
import requests
import google.generativeai as genai

headers = {
    "URL_esp32cam" = st.secrets["URL_esp32cam"],
    "gemini_api_key" = st.secrets["gemini_api_key"],
    "ubidots_api_key" = st.secrets["ubidots_api_key"]
    "content-type" : "application/json"
}
model = genai.GenerativeModel("gemini-1.5-flash")
genai.configure(api_key=gemini_api_key)

if "llm" not in st.session_state:
    st.session_state.llm = ""

st.title("SIPANDAI LAPORAN")
st.write("""Halaman ini memudahkan anda untuk membuat laporan kepada guru BK (Bimbingan Konseling) atau guru mata pelajaran, sehingga dapat melakukan tindak lanjut kepada siswa yang terdeteksi menggunakan handphone selama ujian berlangsung.""")

col1, col2 = st.columns(2)
st.write(st.session_state.llm)

if st.button("Buat Laporan Otomatis?"):
    headers = {
        "X-Auth-Token":ubidots_api_key}

    response_detection = requests.get(URL_esp32cam,headers=headers)

    detection_value = float(response_detection.text)


    prompt = f"""
    berdasarkan data berapa kali terdeteksi handphone pada ruangan ini = {detection_value} kali, tolong buatkan laporan otomatis 
    untuk guru pengawas agar dapat dijadikan laporan siap kirim ke guru bk/ guru mata pelajaran yang akan memberi tindak lanjut pada siswa tersebut.

    susun dalam format:
    1. kata pengantar
    2. deteksi yang terjadi
    3. permohonan untuk menindaklanjuti
    4. rekomendasi

    anda akan menyusun surat laporan yang dapat digunakan langsung oleh guru pengawas (siap kirim)
    """
    response = model.generate_content(prompt)
    st.session_state.llm = response.text
