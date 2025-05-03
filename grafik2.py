import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Konfigurasi
UBIDOTS_TOKEN = "BBUS-L5TJHBNJc29LKKgDDXppr4d3jcyFbt"  # token kamu
DEVICE = "esp32cam"
VARIABLE = "terdeteksi-handphone"

# Fetch data from Ubidots
url = f"https://industrial.api.ubidots.com/api/v1.6/devices/esp32cam/values"
headers = {"X-Auth-Token": UBIDOTS_TOKEN}

st.title("Grafik Real-Time dari Ubidots")

try:
    response = requests.get(url, headers=headers)
    data = response.json()["results"]

    # Convert to DataFrame
    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df["jam"] = df["timestamp"].dt.strftime("%H")

    # Hitung jumlah deteksi per jam
    jumlah_per_jam = df["jam"].value_counts().sort_index()

    st.subheader("Tabel Data dari Ubidots")
    st.dataframe(df[["timestamp", "value", "jam"]])

    st.subheader("Grafik Jumlah Deteksi per Jam")
    fig, ax = plt.subplots()
    jumlah_per_jam.plot(kind="bar", ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Deteksi")
    ax.set_title("Frekuensi Deteksi dari Ubidots")
    st.pyplot(fig)

except Exception as e:
    st.error(f"❌ Gagal mengambil data dari Ubidots: {e}")
