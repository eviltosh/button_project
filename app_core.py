import streamlit as st

st.set_page_config(layout="wide", page_title="Neon Sidebar Toggle")

# ----------------------------------------------------------
# SESSION STATE — Sidebar open/closed
# ----------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# ----------------------------------------------------------
# CSS — Neon styling + hiding default Streamlit sidebar
# ----------------------------------------------------------
st.markdown("""
<style>

    /* Hide default Streamlit sidebar completely */
    section[data-testid="stSidebar"] { display: none !important; }
    div[data-testid="collapsedControl"] { display: none !important; }

    /* Grid layout container */
    .app-row {
        display: flex;
        width: 100%;
    }

    /* Custom Sidebar */
    .custom-sidebar {
        width: 360px;
        min-height: 100vh;
        padding: 24px 20px;
        background-image: url('https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        position: relative;
        color: white;
        border-right: 3px solid rgba(155,0,255,0.45);
        box-shadow: 8px 0px 22px rgba(155,0,255,0.4);
    }

    /* Main content area */
    .main-content {
        flex: 1;
        padding: 24px;
    }

    /* Neon button */
    .neon-btn {
        background: linear-gradient(135deg, #9b00ff 0%, #b300ff 100%) !important;
        color: white !important;
        padding: 12px 20px !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        border: 2px solid #b300ff !important;
        box-shadow: 0 0 12px #b300ff, 0 0 28px rgba(179,0,255,0.7) !important;
        cursor: pointer;
        width: 100%;
    }

    .neon-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 0 18px #d400ff, 0 0 40px rgba(212,0,255,0.9) !important;
    }

    /* OPEN button position (fixed on top-left when sidebar closed) */
    .open-fixed {
        position: fixed;
        top: 20px;
        left: 20px;
        z-index: 999999;
        width: 120px;
    }

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# RENDER LAYOUT
# ----------------------------------------------------------
if st.session_state.sidebar_open:

    st.markdown('<div class="app-row">', unsafe_allow_html=True)

    # -------------------
    # SIDEBAR
    # -------------------
    st.markdown('<div class="custom-sidebar">', unsafe_allow_html=True)

    # CLOSE BUTTON (pure Streamlit)
    if st.button("CLOSE", key="close_btn", help="Close sidebar", use_container_width=True):
        st.session_state.sidebar_open = False
        st.rerun()

    # Sidebar header
    st.markdown("""
        <div style="margin-top:40px; font-size:28px; font-weight:800;">
            NEON SIDEBAR
        </div>
    """, unsafe_allow_html=True)

    st.write("Sidebar content goes here.")
    st.write("This is a fully stable version with no JS at all.")

    st.markdown("</div>", unsafe_allow_html=True)  # END SIDEBAR

    # -------------------
    # MAIN CONTENT
    # -------------------
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.title("Sidebar OPEN")
    st.write("Close button works. Background stable.")
    st.markdown("</div></div>", unsafe_allow_html=True)

else:
    # -------------------
    # SIDEBAR CLOSED → SHOW OPEN BUTTON
    # -------------------
    st.markdown('<div class="open-fixed">', unsafe_allow_html=True)

    if st.button("OPEN", key="open_btn", help="Open sidebar", use_container_width=True):
        st.session_state.sidebar_open = True
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # MAIN CONTENT (closed)
    st.title("Sidebar CLOSED")
    st.write("Open button is fixed in the top-left.")
