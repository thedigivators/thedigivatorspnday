try:
    response = requests.get(url, headers=headers)
    
    # DEBUG: tampilkan status dan isi JSON
    st.subheader("🔍 Debug Response")
    st.write("Status code:", response.status_code)
    st.json(response.json())

    # Cek jika response sukses
    if response.status_code != 200:
        st.error("❌ Request gagal. Periksa token, device, atau variable name.")
        st.stop()

    json_data = response.json()

    # Cek apakah key 'results' ada
    if "results" not in json_data:
        st.error("⚠️ Data tidak ditemukan. Mungkin variabel salah atau belum ada data terkirim.")
        st.stop()

    # Lanjut jika aman
    data = json_data["results"]
    df = pd.DataFrame(data)

    if df.empty:
        st.warning("⚠️ Tidak ada data deteksi yang tersedia saat ini.")
        st.stop()

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df["jam"] = df["timestamp"].dt.strftime("%H")

    jumlah_per_jam = df["jam"].value_counts().sort_index()

    st.subheader("📋 Tabel Data dari Ubidots")
    st.dataframe(df[["timestamp", "value", "jam"]])

    st.subheader("📊 Grafik Jumlah Deteksi per Jam")
    fig, ax = plt.subplots()
    jumlah_per_jam.plot(kind="bar", ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Deteksi")
    ax.set_title("Frekuensi Deteksi dari Ubidots")
    st.pyplot(fig)

except Exception as e:
    st.error(f"❌ Terjadi error saat mengambil atau memproses data: {e}")
