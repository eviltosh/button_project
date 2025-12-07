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
# CSS + HTML + JS (IMPROVED: button sits at top-right of sidebar area)
# --------------------------------------------------------
# Explanation:
# - --sidebar-width defines how wide the sidebar is (adjust if your theme changes it)
# - When sidebar_open is True: button left position is calculated so it visually sits inside the sidebar (near its right edge)
# - When sidebar_open is False: OPEN button is at the left edge of the window (where collapsed sidebar would be)
html = f"""
<style>
:root {{
    --sidebar-width: 380px; /* change this if your sidebar width differs */
}}

/* Make the sidebar visually positioned, so absolute/ fixed button positions line up */
section[data-testid="stSidebar"] {{
    position: relative;
    min-height: 100vh !important;
    background-image: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
    box-sizing: border-box;
}}

/* Neon button shared styles */
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
    display: inline-flex;
    align-items: center;
    gap: 10px;
    -webkit-tap-highlight-color: transparent;
}

/* Hover / focus */
#open-btn:hover, #close-btn:hover {{
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 10px 30px rgba(179,0,255,0.36), 0 0 36px rgba(179,0,255,0.22) inset;
}}
#open-btn:focus, #close-btn:focus {{
    outline: 3px solid rgba(155,0,255,0.18);
    outline-offset: 2px;
}}

/* When sidebar is OPEN: place CLOSE button visually at the top-right inside the sidebar area */
#close-btn {{
    left: calc(var(--sidebar-width) - 120px); /* positions button near the right edge of the sidebar */
    right: auto;
    display: {"block" if sidebar_open else "none"};
}}

/* When sidebar is CLOSED: place OPEN button near the left edge of the page where the sidebar appears */
#open-btn {{
    left: 16px;
    right: auto;
    display: {"none" if sidebar_open else "block"};
}}

/* Small responsive tweak: for very narrow screens, nudge the button inward */
@media (max-width: 680px) {{
    #close-btn {{
        left: calc(var(--sidebar-width) - 140px);
        top: 12px;
        padding: 10px 16px;
    }}
    #open-btn {{
        left: 10px;
        top: 12px;
        padding: 10px 14px;
    }}
}}
</style>

<!-- Buttons -->
<button id="open-btn" aria-label="Open sidebar" onclick="openSide()">OPEN</button>
<button id="close-btn" aria-label="Close sidebar" onclick="closeSide()">CLOSE</button>

<script>
function openSide() {{
    const url = new URL(window.location.href);
    url.searchParams.set("sidebar", "1");
    // Use location.replace to avoid creating extra history entries when toggling repeatedly:
    window.location.replace(url.toString());
}}
function closeSide() {{
    const url = new URL(window.location.href);
    url.searchParams.set("sidebar", "0");
    window.location.replace(url.toString());
}}
</script>
"""

# Render the HTML/CSS/JS
components.html(html, height=0)

# --------------------------------------------------------
# MAIN CONTENT
# --------------------------------------------------------
if sidebar_open:
    st.sidebar.write("Sidebar is OPEN")

st.title("Sidebar Toggle System — IMPROVED ITERATION")
st.write("Sidebar open:", sidebar_open)
