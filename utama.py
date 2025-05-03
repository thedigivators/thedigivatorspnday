import streamlit as st

pages = {
    "Our Product": [
        st.Page("kabar.py", title="SIPANDAI Kabar"),
        st.Page("halamangenai.py", title="SIPANDAI Saran"),
        st.Page("halamanlaporan.py", title="SIPANDAI Laporan"),
        st.Page("grafik.py", title="SIPANDAI Riwayat"),
    ],
    "About Us": [
        st.Page("aboutsipandai.py", title="Tentang SIPANDAI"),
    ],
}

pg = st.navigation(pages)
pg.run()
