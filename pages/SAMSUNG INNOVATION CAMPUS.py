import streamlit as st
import numpy as np
import pandas as pd
from datetime import time

pages = {
    "Our Product": [
        st.Page("Dashboard-SIPANDAIHSC191.py", title="SIPANDAI"),
        st.Page("pages/halamangenai.py", title="SIPANDAI SARAN"),
        st.Page("pages/halamanlaporan.py", title="SIPANDAI LAPORAN")
    ],
    "About Us": [
        st.Page("pages/SAMSUNG INNOVATION CAMPUS.py", title="Samsung Innovation Campus"),
        st.Page("pages/thedigivators.py", title="The Digivators"),
    ],
}

pg = st.navigation(pages)
pg.run() 

st.title("🎓 SAMSUNG INNOVATION CAMPUS")
st.write("From HSC191-The Digivators-SMAN 1 Rejang Lebong")

st.text("Hi Hactiv8-SIC. We wanna say thanks sm for the journey of SIC. Membersamai SIC Batch 6 adalah suatu hal yang sangat kami syukuri. Membersamai kemajuan teknologi, Mempelajari betapa pentingnya ilmu teknologi, Menyadari bahwa kami perlu menginovasi.")
st.image("images/sic.191.jpg")

st.image("images/hacktiv8td.jpg")
st.title("🌏succes for us SIC-HACKTIV8")
st.write("Terimakasih telah menjadikan kami berusaha untuk pandai dalam membentuk SIPANDAI")
