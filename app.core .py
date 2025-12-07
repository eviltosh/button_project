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
# CSS + HTML + JS (FULLY FIXED)
# --------------------------------------------------------
html = f"""
<style>
:root {{
    --sidebar-width: 380px;
}}

/* --- UNIVERSAL BUTTON STYLE (NEON PURPLE) --- */
#open-btn, #close-btn {{
    position: fixed;
    top: 20px;
    right: 25px;               /* TOP RIGHT */
    z-index: 999999;
    padding: 12px 22px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    cursor: pointer;
    box-shadow: 0 0 18px #b300ff;
    background: #b300ff;
    color: white;
}}

/* show open only when sidebar is closed */
#open-btn {{
    display: {"none" if sidebar_open else "block"};
}}

/* show close only when sidebar is open */
#close-btn {{
    display: {"block" if sidebar_open else "none"};
}}

/* --- SIDEBAR BACKGROUND --- */
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
