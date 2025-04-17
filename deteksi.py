import streamlit as st
import requests
import google.generativeai as genai
import pandas as pd

URL_esp32cam = "https://industrial.api.ubidots.com/api/v1.6/devices/esp32cam/terdeteksi-handphone/lv"
gemini_api_key = "AIzaSyAOjm2SLbEonHsAHF94u_j0jpEX6VLhKl0"
ubidots_api_key = "BBUS-L5TJHBNJc29LKKgDDXppr4d3jcyFbt"
model = genai.GenerativeModel("gemini-1.5-flash")
genai.configure(api_key=gemini_api_key)

if "llm" not in st.session_state:
    st.session_state.llm = ""



st.title("‼️SIPANDAI Deteksi aksi mencontek dengan AI❗")
st.write("The Digivators-HSC191-SMAN1RL, SIC6. We born to gain & get not to be bad(🫸cheat)")

col1, col2 = st.columns(2)
st.write(st.session_state.llm)

if st.button("Update"):
    headers = {
        "X-Auth-Token":ubidots_api_key}

    response_detection = requests.get(URL_esp32cam,headers=headers)

    detection_value = float(response_detection.text)


    prompt = f"""
    berdasarkan data, total deteksi handphone sebanyak = {detection_value} kali, pada ujian matematika dengan durasi 1 jam, menggunakan metode deteksi handphone dengan model YOLO
    jumlah siswa dalam 1 ruangan 25 orang
    berikan pendapat anda tentang ruangan ini berdasarkan banyaknya total deteksi handphone.
    """
    response = model.generate_content(prompt)

    st.session_state.detection = detection_value
    st.session_state.llm = response.text
    col1.metric("Total Deteksi Handphone", f"{detection_value}")

st.write("SIPANDAI bersama Kejujuran")
st.image("images/urhonesty.jpg")

data_df = pd.DataFrame(
    {
        "SIPANDAI": ["Mendeteksi dan identifikasi siswa yang melakukan kecurangan🤔", "Sensor mengambil gambar sebagai bukti👍", "Bukti akan muncul beserta notifikasi dengan suatu app yang dapat diakses guru pengawas👌", "Guru pengawas pula akan mendapatkan saran dari AI ketika mengakses data hasil kecurangan😎"],
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

st.write("TheDigivators-HSC191-SIC6-SIPANDAI-SMAN1RL")
