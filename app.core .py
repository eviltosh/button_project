import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# --------------------------------------------------------
# QUERY PARAMS STATE
# --------------------------------------------------------
params = st.query_params
sidebar_open = params.get("sidebar", "1") == "1"   # default open

# --------------------------------------------------------
# UPDATE QUERY PARAMS (helper)
# --------------------------------------------------------
def set_sidebar_state(is_open: bool):
    st.experimental_set_query_params(sidebar="1" if is_open else "0")

# --------------------------------------------------------
# CSS + HTML + JS
# --------------------------------------------------------
html = f"""
<style>
:root {{
    --sidebar-width: 380px;
}}

section[data-testid="stSidebar"] {{
    position: relative;
    min-height: 100vh !important;
    background-image: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
    box-sizing: border-box;
}}

#open-btn, #close-btn {{
    position: fixed;
    top: 18px;
    z-index: 9999999;
    padding: 12px 20px;
    font-size: 15px;
    font-weight: 700;
    border-radius: 12px;
    border: 0;
    cursor: pointer;
    color: #fff;
    background: linear-gradient(135deg, #9b00ff 0%, #b300ff 100%);
    box-shadow: 0 6px 20px rgba(179, 0, 255, 0.28), 0 0 30px rgba(179,0,255,0.18) inset;
    transition: transform 150ms ease, box-shadow 150ms ease, opacity 150ms ease;
}}

#close-btn {{
    left: calc(var(--sidebar-width) - 120px);
    right: auto;
    display: {"block" if sidebar_open else "none"};
}}

#open-btn {{
    left: 16px;
    right: auto;
    display: {"none" if sidebar_open else "block"};
}}
</style>

<button id="open-btn" onclick="openSide()">OPEN</button>
<button id="close-btn" onclick="closeSide()">CLOSE</button>

<script>
function openSide() {{
    const url = new URL(window.location.href);
    url.searchParams.set("sidebar", "1");
    window.location.replace(url.toString());
}}
function closeSide() {{
    const url = new URL(window.location.href);
    url.searchParams.set("sidebar", "0");
    window.location.replace(url.toString());
}}
</script>
"""

components.html(html, height=0)

# --------------------------------------------------------
# MAIN CONTENT
# --------------------------------------------------------
if sidebar_open:
    st.sidebar.write("Sidebar is OPEN")

st.title("Sidebar Toggle System — FIXED & COMPLETE")
st.write("Sidebar open:", sidebar_open)
