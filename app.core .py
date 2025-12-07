import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# ------------------------------------------------------------------
#   HTML + CSS + JS — REAL SIDEBAR TOGGLE (NO PAGE RELOAD)
# ------------------------------------------------------------------

html = """
<style>
/* Sidebar background */
section[data-testid="stSidebar"] {
    background-image: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
    min-height: 100vh;
    transition: transform 0.35s ease-in-out;
}

/* Hidden state (slide left) */
.sidebar-closed {
    transform: translateX(-380px);
}

/* Open state */
.sidebar-open {
    transform: translateX(0px);
}

/* Neon buttons */
.toggle-btn {
    position: fixed;
    top: 25px;
    z-index: 999999999;
    padding: 12px 24px;
    font-size: 15px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    cursor: pointer;
    color: white;
    background: linear-gradient(135deg, #9b00ff 0%, #c200ff 100%);
    box-shadow: 0 0 18px #b300ff55, 0 0 30px #b300ffaa inset;
}

/* Open button */
#open-btn {
    left: 20px;
    display: none;
}

/* Close button (inside sidebar) */
#close-btn {
    left: 310px;
    display: block;
}
</style>

<script>
// Toggle logic (no reload, no navigation)
function closeSidebar() {
    const sidebar = window.parent.document.querySelector('section[data-testid="stSidebar"]');
    sidebar.classList.remove("sidebar-open");
    sidebar.classList.add("sidebar-closed");

    window.parent.document.getElementById("open-btn").style.display = "block";
    window.parent.document.getElementById("close-btn").style.display = "none";
}

function openSidebar() {
    const sidebar = window.parent.document.querySelector('section[data-testid="stSidebar"]');
    sidebar.classList.remove("sidebar-closed");
    sidebar.classList.add("sidebar-open");

    window.parent.document.getElementById("open-btn").style.display = "none";
    window.parent.document.getElementById("close-btn").style.display = "block";
}
</script>

<!-- External buttons rendered into parent DOM -->
<button id="open-btn" class="toggle-btn" onclick="openSidebar()">OPEN</button>
<button id="close-btn" class="toggle-btn" onclick="closeSidebar()">CLOSE</button>
"""

components.html(html, height=0)

# ------------------------------------------------------------------
#   MAIN PAGE CONTENT
# ------------------------------------------------------------------
st.title("Sidebar Toggle — No Navigation Version")
st.write("Close/Open both work instantly without leaving the page.")
