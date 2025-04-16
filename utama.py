import streamlit as st

pages = {
    "Our Product": [
        st.Page("deteksi.py", title="SIPANDAI"),
        st.Page("halamangenai.py", title="SIPANDAI SARAN"),
        st.Page("halamanlaporan.py", title="SIPANDAI LAPORAN"),
    ],
    "About Us": [
        st.Page("aboutsic.py", title="Samsung Innovation Campus"),
        #st.Page("thedigivators.py", title="The Digivators"),
    ],
}

pg = st.navigation(pages)
pg.run()
