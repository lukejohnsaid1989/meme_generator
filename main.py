
import streamlit as st
from streamlit_player import st_player

header = st.header("MALTA MEME ARCHIVE")

with st.container():
    col1_a, col2_a, col3_a = st.columns(3)
    with col1_a:
        zqc_button = st.button(label="ĦA NARAH")
    with col2_a:
        frt_button = st.button(label="AVUKATI PERITI")
    with col3_a:
        hms_button = st.button(label="UX ĦAMSA")

with st.container():
    col1_b, col2_b, col3_b = st.columns(3)
    with col1_b:
        potato_button = st.button(label="MY LIVE IS POTATO")
    with col2_b:
        presente_button = st.button(label="PRESENTE")
    with col3_b:
        ps_ps_button = st.button(label="PSPSPSPS")


if zqc_button:
    url = "https://youtu.be/SM-dfSoGCJ0?t=38"
    player = st_player(loop=True, url=url, playing=True, play_inline=True)


if frt_button:
    url = "https://youtu.be/2_AQxXbXTzY?t=37"
    player = st_player(loop=True, url=url, playing=True, play_inline=True)


if hms_button:
    url = "https://youtu.be/GGxoMr2huZY?t=10"
    player = st_player(loop=True, url=url, playing=True, play_inline=True)


if potato_button:
    url = "https://youtu.be/QiqqC_fbP1c?t=6"
    player = st_player(loop=True, url=url, playing=True, play_inline=True)


if presente_button:
    url = "https://youtu.be/Hf4KIvoz_RE?t=65"
    player = st_player(loop=True, url=url, playing=True, play_inline=True)


if ps_ps_button:
    url = "https://youtu.be/R7-k0phftwo?t=63"
    player = st_player(loop=True, url=url, playing=True, play_inline=True)
