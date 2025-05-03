import streamlit as st

pages = {
    "SIPANDAI": [
        st.Page("kabar.py", title="Kabar"),
        st.Page("halamangenai.py", title="Saran"),
        st.Page("halamanlaporan.py", title="Laporan"),
        st.Page("grafik.py", title="Riwayat"),
        st.Page("grafik2.py", title="Riwayat real time"),
    ],
    "About Us": [
        st.Page("aboutsipandai.py", title="Tentang SIPANDAI"),
    ],
}

pg = st.navigation(pages)
pg.run()
