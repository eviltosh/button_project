import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# --------------------------------------------------------
# QUERY PARAMS STATE
# --------------------------------------------------------
params = st.query_params
sidebar_open = params.get("sidebar", "1") == "1"   # default open

# --------------------------------------------------------
# UPDATE QUERY PARAMS
# --------------------------------------------------------
def set_sidebar_state(is_open: bool):
    st.query_params["sidebar"] = "1" if is_open else "0"

# --------------------------------------------------------
# CSS + HTML + JS
# --------------------------------------------------------
html = f"""
<style>

:root {{
    /* REAL Streamlit Cloud sidebar width */
    --sidebar-width: 380px;
}}

#open-btn {{
    position: fixed;
    top: 20px;
    left: 20px;
    z-index: 999999;
    background: #00ff66;
    color: black;
    padding: 12px 22px;
    border-radius: 10px;
    border: none;
    font-size: 18px;
    font-weight: bold;
    box-shadow: 0 0 15px #00ff66;
    cursor: pointer;
    display: {"none" if sidebar_open else "block"};
}}

#close-btn {{
    position: fixed;
    top: 20px;
    left: calc(var(--sidebar-width) - 120px); /* PERFECT position */
    z-index: 999999;
    background: #b300ff;
    color: white;
    padding: 12px 22px;
    border-radius: 10px;
    border: none;
    font-size: 18px;
    font-weight: bold;
    box-shadow: 0 0 15px #b300ff;
    cursor: pointer;
    display: {"block" if sidebar_open else "none"};
}}

section[data-testid="stSidebar"] {{
    background-image: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
    min-height: 100vh !important;
}}

</style>

<button id="open-btn" onclick="openSide()">OPEN</button>
<button id="close-btn" onclick="closeSide()">CLOSE</button>

<script>
function openSide() {{
    const url = new URL(window.location.href);
    url.searchParams.set("sidebar", "1");
    window.location.href = url.toString();
}}
function closeSide() {{
    const url = new URL(window.location.href);
    url.searchParams.set("sidebar", "0");
    window.location.href = url.toString();
}}
</script>
"""

components.html(html, height=0)

# --------------------------------------------------------
# MAIN CONTENT
# --------------------------------------------------------
if sidebar_open:
    st.sidebar.write("Sidebar is OPEN")

st.title("Sidebar Toggle System — FINAL FIXED VERSION")
st.write("Sidebar open:", sidebar_open)
