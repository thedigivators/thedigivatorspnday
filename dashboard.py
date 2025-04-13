import streamlit as st
import requests
import google.generativeai as genai
import detect_phone

URL_esp32cam = "https://industrial.api.ubidots.com/api/v1.6/devices/esp32cam/terdeteksi-handphone/lv"
gemini_api_key = "AIzaSyAOjm2SLbEonHsAHF94u_j0jpEX6VLhKl0"
ubidots_api_key = "BBUS-Ubq4m0YjEKtSfJDfVolqxOOs2gZfoz"
model = genai.GenerativeModel("gemini-1.5-flash")
genai.configure(api_key=gemini_api_key)

if "llm" not in st.session_state:
    st.session_state.llm = ""

st.title("SIPANDAI Deteksi contek dengan AI")

col1, col2 = st.columns(2)
st.write(st.session_state.llm)

if st.button("Update"):
    headers = {
        "X-Auth-Token":ubidots_api_key}

    response_detection = requests.get(URL_esp32cam,headers=headers)

    detection_value = float(response_detection.text)


    prompt = f"""
    berdasarkan data anak yang mencontek = {detection_value} orang, mohon berilah saran kepada guru pengawas tentang ruang ujian ini...
    "Kondisi ruangan ujian ini..."

    berikan pendapat anda tentang ruangan ini berdasarkan banyaknya anak yang mencontek, serta beri saran singkat untuk guru pengawas
    """
    response = model.generate_content(prompt)

    st.session_state.detection = detection_value
    st.session_state.llm = response.text
    col1.metric("Total Deteksi Handphone", f"{detection_value}")
