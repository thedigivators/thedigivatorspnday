import streamlit as st
import requests
import google.generativeai as genai
import base64

# === Set Background ===
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

set_bg_from_local("images/latarstreamlit.jpg")

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

# === Konfigurasi API ===
URL_esp32cam = "https://industrial.api.ubidots.com/api/v1.6/devices/esp32cam/terdeteksi-handphone/lv"
gemini_api_key = "AIzaSyAOjm2SLbEonHsAHF94u_j0jpEX6VLhKl0"
ubidots_api_key = "BBUS-Ubq4m0YjEKtSfJDfVolqxOOs2gZfoz"

genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === State untuk LLM ===
if "llm" not in st.session_state:
    st.session_state.llm = ""

# === Judul ===
st.markdown('<div class="main-title">SIPANDAI LAPORAN</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Halaman ini memudahkan anda untuk membuat laporan kepada guru BK (Bimbingan Konseling) atau guru mata pelajaran, sehingga dapat melakukan tindak lanjut kepada siswa yang terdeteksi menggunakan handphone selama ujian berlangsung.</div>',
    unsafe_allow_html=True
)

# === Tombol Generate ===
if st.button("📄 Buat Laporan Otomatis"):
    headers = {"X-Auth-Token": ubidots_api_key}
    response_detection = requests.get(URL_esp32cam, headers=headers)

    try:
        detection_value = float(response_detection.text)
    except ValueError:
        detection_value = 0

    prompt = f"""
    Berdasarkan data, telah terdeteksi penggunaan handphone di ruang ujian sebanyak {detection_value} kali. 
    Tolong buatkan laporan otomatis untuk guru pengawas agar dapat dikirim ke guru BK atau guru mata pelajaran 
    yang bersangkutan untuk menindaklanjuti siswa tersebut.

    Format yang harus dihasilkan:
    1. Kata pengantar
    2. Uraian deteksi
    3. Permohonan tindak lanjut
    4. Rekomendasi

    Namun, jangan tampilkan format angka atau poin secara eksplisit.
    """

    response = model.generate_content(prompt)
    st.session_state.llm = response.text

# === Tampilkan Hasil ===
if st.session_state.llm:
    st.markdown('<div class="report-container">', unsafe_allow_html=True)
    st.markdown(f'<div class="llm-result">{st.session_state.llm}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
