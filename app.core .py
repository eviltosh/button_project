import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# ----------------------------------------------------------
# STATE (Streamlit-safe)
# ----------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# ----------------------------------------------------------
# CSS – Hide real Streamlit sidebar toggle
# ----------------------------------------------------------
st.markdown("""
<style>
button[kind="header"] { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# CUSTOM SIDEBAR + BUTTONS (ALWAYS VISIBLE)
# ----------------------------------------------------------
html = f"""
<style>
/* CONTAINER */
#custom-sidebar {{
    position: fixed;
    top: 0;
    left: 0;
    width: 380px;
    height: 100vh;
    background-image: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    transition: transform 0.35s ease-in-out;
    z-index: 999999;
    padding: 30px;
    box-sizing: border-box;
    overflow-y: auto;
    color: white;
}}

/* CLOSED STATE */
#custom-sidebar.closed {{
    transform: translateX(-380px);
}}

/* OPEN STATE */
#custom-sidebar.open {{
    transform: translateX(0px);
}}

/* BUTTON STYLES */
.neon-btn {{
    position: fixed;
    top: 20px;
    padding: 12px 22px;
    border-radius: 12px;
    border: none;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    color: white;
    z-index: 999999999;
    background: linear-gradient(135deg, #9b00ff 0%, #c200ff 100%);
    box-shadow: 0 0 20px #b300ff99;
}}

#open-btn {{
    left: 20px;
    display: {"none" if st.session_state.sidebar_open else "block"};
}}

#close-btn {{
    left: 300px;
    display: {"block" if st.session_state.sidebar_open else "none"};
}}
</style>

<div id="custom-sidebar" class="{ 'open' if st.session_state.sidebar_open else 'closed' }">
    <h2>NEON SIDEBAR</h2>
    <p>Sidebar content...</p>
</div>

<button id="open-btn" class="neon-btn" onclick="toggleSidebar(true)">OPEN</button>
<button id="close-btn" class="neon-btn" onclick="toggleSidebar(false)">CLOSE</button>

<script>
function toggleSidebar(isOpen) {{
    const sidebar = window.parent.document.querySelector("#custom-sidebar");
    const openBtn = window.parent.document.querySelector("#open-btn");
    const closeBtn = window.parent.document.querySelector("#close-btn");

    if (isOpen) {{
        sidebar.classList.remove("closed");
        sidebar.classList.add("open");
        openBtn.style.display = "none";
        closeBtn.style.display = "block";
    }} else {{
        sidebar.classList.remove("open");
        sidebar.classList.add("closed");
        openBtn.style.display = "block";
        closeBtn.style.display = "none";
    }}
}}
</script>
"""

components.html(html, height=0)

# ----------------------------------------------------------
# PAGE CONTENT
# ----------------------------------------------------------
st.title("CUSTOM SIDEBAR — ALWAYS SHOWS BUTTONS")
st.write("Buttons ALWAYS visible. No navigation. No glitches.")
