import streamlit as st
import requests
import google.generativeai as genai

URL_esp32cam = "https://industrial.api.ubidots.com/api/v1.6/devices/esp32cam/terdeteksi-handphone/lv"
gemini_api_key = "AIzaSyAOjm2SLbEonHsAHF94u_j0jpEX6VLhKl0"
model = genai.GenerativeModel("gemini-1.5-flash")
genai.configure(api_key=gemini_api_key)

if "llm" not in st.session_state:
    st.session_state.llm = ""

st.title("SIPANDAI SARAN")

col1, col2 = st.columns(2)
st.write(st.session_state.llm)
# st.button("Tindak lanjut?")

if st.button("Tindak Lanjut?"):
    prompt = f"""
    anda adalah seorang guru bimbingan konseling yang handal dalam memberi saran
    setiap terjadi pelanggaran di sekolah. berikan rekomendasi tindak lanjut untuk anak anak yang terdeteksi mencontek. saran ini ditujukan pada guru bimbingan konseling yang ada di sekolah tersebut.
    ingat, jangan gunakan kata ganti "saya", "aku", dan sejenisnya. hanya saran kepada guru bimbingan konseling/ mata pelajaran.
    """
    response = model.generate_content(prompt)

    st.session_state.llm = response.text
    
