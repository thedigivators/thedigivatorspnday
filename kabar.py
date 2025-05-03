import streamlit as st
import requests
import google.generativeai as genai
import pandas as pd
import base64

# HARUS PALING ATAS: Konfigurasi halaman
st.set_page_config(page_title="Tentang SIPANDAI", layout="wide")

# Fungsi untuk mengatur latar belakang dari file lokal
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
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
# === Styling Tambahan ===
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

    html, body, [data-testid="stApp"] {
        font-family: 'Poppins', sans-serif;
        color: white;
    }

    .report-container {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        margin-top: 25px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }

    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        text-align: center;
    }

    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 300;
    }

    .stButton button {
        background-color: #ffffff10;
        border: 1px solid #ffffff30;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 1rem;
        color: white;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        background-color: #ffffff30;
        transform: scale(1.02);
    }

    .llm-result {
        font-size: 1.05rem;
        line-height: 1.7;
    }
    </style>
""", unsafe_allow_html=True)


# Terapkan latar belakang
set_bg_from_local("images/latarstreamlit.jpg")

# Styling tambahan
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&family=Poppins:wght@700;900&display=swap');

    html, body, [data-testid="stApp"] {
        background-color: #4B4E7A;
        color: white;
        font-family: 'Open Sans', sans-serif;
    }

    .title {
        text-align: center;
        font-size: 3rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 800;
        margin-top: 2rem;
    }

    .subtitle {
        text-align: center;
        font-size: 1.8rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        margin-bottom: 2rem;
    }

    .desc {
        font-size: 1.35rem;
        text-align: justify;
        font-family: 'Open Sans', sans-serif;
        padding: 1.1rem;
    }

    .kegiatan-title-main {
        text-align: center;
        font-size: 3rem;
        font-family: 'Poppins', sans-serif;
        font-weight: 800;
        margin-top: 5rem;
        margin-bottom: 2rem;
    }

    .kegiatan-title {
        font-weight: bold;
        font-size: 1.3em;
        font-family: 'Poppins', sans-serif;
        margin-top: 1rem;
    }

    .kegiatan-desc {
        font-size: 1.1em;
        font-family: 'Open Sans', sans-serif;
        text-align: justify;
    }
    </style>
""", unsafe_allow_html=True)

URL_esp32cam = "https://industrial.api.ubidots.com/api/v1.6/devices/esp32cam/terdeteksi-handphone/lv"
gemini_api_key = "AIzaSyAOjm2SLbEonHsAHF94u_j0jpEX6VLhKl0"
ubidots_api_key = "BBUS-L5TJHBNJc29LKKgDDXppr4d3jcyFbt"
model = genai.GenerativeModel("gemini-1.5-flash")
genai.configure(api_key=gemini_api_key)

if "llm" not in st.session_state:
    st.session_state.llm = ""


st.title("SIPANDAI Sistem Pendeteksi Kecurangan Berbasis IoT dan AI")

col1, col2 = st.columns(2)
st.write(st.session_state.llm)

if st.button("Update"):
    headers = {"X-Auth-Token":ubidots_api_key}
    response_detection = requests.get(URL_esp32cam,headers=headers)
    
    detection_value = float(response_detection.text)
    
    
    prompt = f"""
       berdasarkan data, total deteksi handphone sebanyak = {detection_value} kali, pada ujian matematika dengan durasi 1 jam, menggunakan metode deteksi handphone dengan model YOLO
       jumlah siswa dalam 1 ruangan 25 orang. saat siswa melakukan kecurangan (handphone terdeteksi), program akan menangkap gambar dan menyimpannya ke dalam server sehingga bukti dapat ditunjukkan untuk tindak lanjut.
       berikan pendapat singkat anda tentang ruangan ini berdasarkan banyaknya total deteksi handphone.
       """
    response = model.generate_content(prompt)
    
    st.session_state.detection = detection_value
    st.session_state.llm = response.text
    col1.metric("Total Deteksi Handphone", f"{detection_value}")
    
