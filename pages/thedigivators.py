import streamlit as st
import numpy as np
import pandas as pd
from datetime import time

st.title("🎓 SIPANDAI THE DIGIVATORS")
st.write("Pendeteksi kecurangan siswa ketika pengambilan penilaian by The Digivators")

st.image("images/let.us.jpg")

with st.container():
    st.write("Hi everyone, we're the digivators, the digital innovators. We're born to gain and be the main, get the motivation and be the inspiration😎😎" \
    " SIPANDAI, adalah suatu teknologi yang sedang ingin kami kembangkan. Tentu banyak sekali faktor yang menjadi latar belakang terciptanya ide untuk menciptakan SIPANDAI"
    " Banyaknya kecurangan yang terjadi menyebabkan kemampuan siswa dalam berbagai hal menjadi menurun, tentunya hal tersebut juga menjadikan siswa-siswi yang berproses dalam kejujuran merasa tidak adil"
    ". Oleh karena itu, bersama SIPANDAI, kami mengharapkan dapat membantu pengambilan penilaian yang lebih objektif dan menghasilkan generasi yang PANDAI bersama KEJUJURAN")


data_df = pd.DataFrame(
    {
        "SIPANDAI": ["Meningkatkan minat belajar siswa", "Meminimalisir kecurangan yang menghasilkan penilaian tidak objektif", "Meningkatkan kemampuan berpikir kritis siswa", "Menjadikan siswa yang memiliki kejujuran"],
    }
)

vertical_alignment = st.selectbox(
    "Vertical alignment", ["top", "center", "bottom"], index=2
)

left, middle, right = st.columns(3, vertical_alignment=vertical_alignment)
left.image("images/webcam-toy-photo8.jpg")
middle.image("images/webcam-toy-photo10.jpg")
right.image("images/webcam-toy-photo12.jpg")

st.write("Harapan SIPANDAI")

data_df = pd.DataFrame(
    {
        "SIPANDAI": ["Meningkatkan minat belajar dan kemampuan pembelajaran siswa", "Menghasilkan nilai yang objektif", "Menghindari adanya permasalahan antarsiswa", "Menjadikan generasi jujur yang menolak kecurangan"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "SIPANDAI": st.column_config.TextColumn(
            "SIPANDAI",
            help="Menjadi **PANDAI** bersama **SIPANDAI**",
            default="st.",
            max_chars=50,
            validate=r"^st\.[a-z_]+$",
        )
    },
    hide_index=True,
)

st.write("We hope thedigivators can advance to the next stage. How much we love our SIC-HSC191. Aamiin😉😉")