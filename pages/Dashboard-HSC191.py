import streamlit as st

pages = {
    "Our Product": [
        st.Page("Dashboard-SIPANDAIHSC191.py", title="SIPANDAI"),
        st.Page("pages/halamanlaporan.py", title="SIPANDAI LAPORAN"),
        st.Page("pages/halamangenai.py", title="SIPANDAI SARAN")
    ],
    "About Us": [
        st.Page("pages/SAMSUNG INNOVATION CAMPUS.py", title="Samsung Innovation Campus"),
        st.Page("pages/thedigivators.py", title="The Digivators"),
    ],
}

pg = st.navigation(pages)
pg.run()

