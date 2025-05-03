import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: transparent;
        color: white !important;
    }

    [data-testid="stMetric"] div {
        color: white !important;
    }

    [data-testid="stMetricValue"] {
        color: white !important;
        font-weight: bold;
    }

    [data-testid="stMetricLabel"] {
        color: #f0f0f0 !important;
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




st.markdown("<h1 style='text-align: center; font-weight: 800;'>Grafik Deteksi Handphone per Jam</h1>", unsafe_allow_html=True)

# Path ke file CSV (ganti sesuai lokasi kamu)
csv_file_path = "https://raw.githubusercontent.com/thedigivators/thedigivatorspnday/main/database.csv" 

try:
    # Baca file CSV
    df = pd.read_csv(csv_file_path)

    # Pastikan kolom "jam" bertipe string agar sort-nya urut
    df['jam'] = df['jam'].astype(str).str.zfill(2)

    # Hitung jumlah per jam
    jumlah_per_jam = df['jam'].value_counts().sort_index()

    # Tampilkan tabel
    st.subheader("Tabel Data Waktu & Jam Deteksi")
    st.dataframe(df)

    # Tampilkan grafik batang
    st.subheader("Jumlah Deteksi per Jam")
    fig, ax = plt.subplots()
    jumlah_per_jam.plot(kind='bar', ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Deteksi")
    ax.set_title("Frekuensi Deteksi Handphone per Jam")
    st.pyplot(fig)

except FileNotFoundError:
    st.error("File CSV tidak ditemukan. Pastikan path sudah benar.")
except Exception as e:
    st.error(f"Terjadi error saat memuat data: {e}")
