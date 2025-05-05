import streamlit as st
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

# Judul utama dan subjudul
st.markdown('<div class="title">SIPANDAI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Sistem Pendeteksi Kecurangan Berbasis IoT dan AI</div>', unsafe_allow_html=True)

# Layout 2 kolom: logo dan deskripsi
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div style="margin-top: 50px;"></div>', unsafe_allow_html=True)
    st.image("images/logosipandai.jpg", width=500)

with col2:
    st.markdown("""
    <div class="desc">
    SIPANDAI adalah inovasi berbasis <em>Internet of Things (IoT)</em> dan <em>Artificial Intelligence (AI)</em> 
    yang dirancang untuk membantu institusi pendidikan dalam mengurangi kecurangan akademik, khususnya saat ujian berlangsung.
    Sistem ini mampu memantau aktivitas peserta ujian secara <strong>real-time</strong> dan memberikan notifikasi otomatis 
    apabila terdeteksi tindakan mencurigakan seperti penggunaan perangkat yang tidak diizinkan.
    SIPANDAI menggabungkan <strong>kamera</strong>, <strong>pengenalan objek AI</strong>, serta <strong>sistem MQTT</strong> 
    untuk lingkungan ujian yang adil dan transparan.
    </div>
    """, unsafe_allow_html=True)

# Section: Manfaat SIPANDAI
st.markdown('<div class="kegiatan-title-main">Manfaat SIPANDAI</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/hpterdeteksi.png", width=500)
    st.markdown('<div class="kegiatan-title">Deteksi Kecurangan Otomatis</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="kegiatan-desc">
    SIPANDAI mampu mendeteksi secara otomatis siswa yang menggunakan handphone saat ujian berlangsung. Deteksi ini dilakukan secara real-time dengan bantuan kamera dan kecerdasan buatan (AI), sehingga meminimalisir celah kecurangan dan meningkatkan kejujuran dalam pelaksanaan ujian.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("images/buzzer.png", width=500)
    st.markdown('<div class="kegiatan-title">Teguran Tanpa Gangguan</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="kegiatan-desc">
    Melalui sinyal buzzer dan LED yang dipasang pada perangkat siswa, SIPANDAI dapat memberikan teguran langsung secara personal ketika terjadi pelanggaran. Dengan cara ini, siswa lain tidak akan terganggu, dan suasana ujian tetap kondusif serta fokus.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.image("images/berita.png", width=500)
    st.markdown('<div class="kegiatan-title">Bukti Nyata untuk Tindak Lanjut</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="kegiatan-desc">
    Setiap pelanggaran yang terdeteksi secara otomatis akan disertai dengan dokumentasi berupa tangkapan gambar dan notifikasi langsung ke pengawas. Bukti ini dapat digunakan oleh guru mata pelajaran atau pihak BK untuk menindaklanjuti pelanggaran secara objektif dan transparan.
    </div>
    """, unsafe_allow_html=True)



