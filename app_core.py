import streamlit as st

st.set_page_config(layout="wide", page_title="Neon Sidebar Toggle")

# --------------------------------------------------------
# STATE CONTROL
# --------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

params = st.query_params
if "sidebar" in params:
    st.session_state.sidebar_open = params.get("sidebar") == "1"

# --------------------------------------------------------
# CSS — PERFECT BUTTONS
# --------------------------------------------------------
st.markdown("""
<style>

body {
    overflow-x: hidden !important;
}

/* =======================================================
   NEON BUTTON CORE STYLE
======================================================= */
a.neon-btn {
    display: inline-block !important;
    padding: 10px 18px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    color: white !important;
    background: linear-gradient(135deg, #9b00ff 0%, #b300ff 100%) !important;
    border: 2px solid #b300ff !important;
    border-radius: 10px !important;
    text-decoration: none !important;

    box-shadow: 
        0 0 12px #b300ff,
        0 0 28px rgba(179, 0, 255, 0.5) !important;

    cursor: pointer !important;
}

a.neon-btn:hover {
    transform: scale(1.04);
    box-shadow: 
        0 0 18px #d400ff,
        0 0 40px rgba(212, 0, 255, 0.8) !important;
}

/* =======================================================
   OPEN BUTTON POSITION (TOP-LEFT)
======================================================= */
.open-btn {
    position: fixed !important;
    top: 22px !important;
    left: 22px !important;
    z-index: 999999 !important;
}

/* =======================================================
   CLOSE BUTTON POSITION (INSIDE SIDEBAR TOP-RIGHT)
======================================================= */
.close-btn {
    position: absolute !important;
    top: 18px !important;
    right: 18px !important;
    z-index: 999999 !important;
}

/* Sidebar container */
.custom-sidebar {
    width: 360px;
    min-height: 100vh;
    background-image: url('https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    padding: 24px;
    position: relative;
}

/* Layout wrapper */
.app-row {
    display: flex;
    width: 100%;
}

/* Main content */
.main-content {
    flex: 1;
    padding: 24px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------------
# RENDER
# --------------------------------------------------------
if st.session_state.sidebar_open:

    st.markdown('<div class="app-row">', unsafe_allow_html=True)

    # ---- SIDEBAR ----
    sidebar_html = """
    <div class="custom-sidebar">

        <a href="?sidebar=0" class="neon-btn close-btn">CLOSE</a>

        <div style="margin-top: 80px; color: white; font-size: 28px; font-weight: 700;">
            NEON SIDEBAR
        </div>

        <div style="margin-top: 40px; color: white; font-size: 16px;">
            <p>Sidebar content goes here.</p>
            <p>Your perfect neon controls are ready.</p>
        </div>

    </div>
    """
    st.markdown(sidebar_html, unsafe_allow_html=True)

    # ---- MAIN CONTENT ----
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.title("Sidebar OPEN")
    st.write("Close button is inside the sidebar (top-right).")
    st.markdown('</div></div>', unsafe_allow_html=True)

else:
    # ---- OPEN BUTTON (SIDEBAR CLOSED) ----
    st.markdown(
        '<a href="?sidebar=1" class="neon-btn open-btn">OPEN</a>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="app-row"><div class="main-content">', unsafe_allow_html=True)
    st.title("Sidebar CLOSED")
    st.write("Open button stays fixed in the top-left.")
    st.markdown('</div></div>', unsafe_allow_html=True)
