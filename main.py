import streamlit as st
from PIL import Image

from theme import red_dark

im = Image.open("assets/logo.png")
st.set_page_config(page_title="Risk Radar", page_icon=im, layout="wide")

red_dark()

home = st.Page(
    page="views/home.py",
    title="Home",
    icon="🏠"
)

vendor_reg = st.Page(
    page="views/registration.py",
    title="Vendor Registration",
    icon="🤵"
)

scrape = st.Page(
    page="views/custom_scraping.py",
    title="Custom Scraping",
    icon="⚙️"
)

thread = st.Page(
    page="views/init_thread.py",
    title="Threads",
    icon="🤖"
)

pg = st.navigation(
    {
        "Home":[home],
        "Services":[thread,scrape],
        "Register":[vendor_reg]
    }
)
pg.run()

st.logo("assets/menu-text.svg")