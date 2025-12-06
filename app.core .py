import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# ------------------------------------------------------------------------------
# STATE
# ------------------------------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# ------------------------------------------------------------------------------
# HTML, CSS, JS
# ------------------------------------------------------------------------------

html_code = f"""
<style>

/* --- FIXED OPEN BUTTON (MAIN PAGE) --- */
#open-btn {{
    position: fixed;
    top: 20px;
    left: 20px;
    z-index: 99999;
    background: #00ff66;
    color: black;
    padding: 12px 22px;
    border-radius: 10px;
    border: none;
    font-size: 18px;
    font-weight: 700;
    box-shadow: 0 0 15px #00ff66;
    cursor: pointer;
    display: {'block' if not st.session_state.sidebar_open else 'none'};
}}

/* --- FIXED CLOSE BUTTON (INSIDE SIDEBAR AREA) --- */
#close-btn {{
    position: fixed;
    top: 20px;
    left: 270px; /* slightly inside sidebar */
    z-index: 99999;
    background: #b300ff;
    color: white;
    padding: 12px 22px;
    border-radius: 10px;
    border: none;
    font-size: 18px;
    font-weight: 700;
    box-shadow: 0 0 15px #b300ff;
    cursor: pointer;
    display: {'block' if st.session_state.sidebar_open else 'none'};
}}

/* --- SIDEBAR BACKGROUND --- */
section[data-testid="stSidebar"] {{
    background-image: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
    background-size: cover;
    background-position: center;
}}

</style>

<button id="open-btn" onclick="openSidebar()">OPEN</button>
<button id="close-btn" onclick="closeSidebar()">CLOSE</button>

<script>
function openSidebar() {{
    fetch('/open', {{method: 'POST'}}).then(() => window.parent.location.reload());
}}
function closeSidebar() {{
    fetch('/close', {{method: 'POST'}}).then(() => window.parent.location.reload());
}}
</script>
"""

components.html(html_code, height=0)

# ------------------------------------------------------------------------------
# PYTHON ENDPOINTS FOR JS
# ------------------------------------------------------------------------------
@st.experimental_rpc("open", kind="http")
def api_open():
    st.session_state.sidebar_open = True
    return True

@st.experimental_rpc("close", kind="http")
def api_close():
    st.session_state.sidebar_open = False
    return True

# ------------------------------------------------------------------------------
# MAIN CONTENT
# ------------------------------------------------------------------------------
st.title("Main App – Fixed HUD Toggle System")
st.write("Sidebar open:", st.session_state.sidebar_open)
