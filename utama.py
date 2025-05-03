import streamlit as st

pages = {
    "Our Product": [
        st.Page("kabar.py", title="SIPANDAI"),
        st.Page("halamangenai.py", title="SIPANDAI SARAN"),
        st.Page("halamanlaporan.py", title="SIPANDAI LAPORAN"),
    ],
    "About Us": [
        st.Page("deteksi.py", title="Samsung Innovation Campus"),
    ],
}

pg = st.navigation(pages)
pg.run()
