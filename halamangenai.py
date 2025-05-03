import streamlit as st
import requests
import google.generativeai as genai
import base64

# === Konfigurasi API ===
URL_esp32cam = "https://industrial.api.ubidots.com/api/v1.6/devices/esp32cam/terdeteksi-handphone/lv"
gemini_api_key = "AIzaSyAOjm2SLbEonHsAHF94u_j0jpEX6VLhKl0"
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === Background Lokal ===
def set_bg_from_local(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        [data-testid="stApp"] {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_from_local("images/latarstreamlit.jpg")  # Ganti dengan path lokal kamu

# === Styling ===
st.markdown(
    """
    <style>
    .center-text {
        text-align: center;
        font-size: 20px;
        font-family: 'Segoe UI', sans-serif;
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 12px;
        margin: 30px auto;
        width: 80%;
        color: white;
    }
    .stButton > button {
        background-color: transparent !important;
        color: white !important;
        border: 2px solid white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        transition: 0.3s ease;
    }
    .stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# === Session State untuk hasil LLM ===
if "llm" not in st.session_state:
    st.session_state.llm = ""

# === Judul Aplikasi ===
st.markdown("<h1 style='text-align: center; color: white;'>SIPANDAI SARAN</h1>", unsafe_allow_html=True)


# === Tombol dan Logika ===
if st.button("Tindak Lanjut?"):
    prompt = """
    anda adalah seorang guru bimbingan konseling yang handal dalam memberi saran
    setiap terjadi pelanggaran di sekolah. berikan rekomendasi tindak lanjut untuk anak anak yang terdeteksi mencontek. saran ini ditujukan pada guru bimbingan konseling yang ada di sekolah tersebut.
    ingat, jangan gunakan kata ganti "saya", "aku", dan sejenisnya. hanya saran kepada guru bimbingan konseling/ mata pelajaran.
    """
    response = model.generate_content(prompt)
    st.session_state.llm = response.text

# === Tampilkan Hasil LLM ===
if st.session_state.llm:
    st.markdown(f'<div class="center-text">{st.session_state.llm}</div>', unsafe_allow_html=True)

