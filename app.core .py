import streamlit as st

st.set_page_config(layout="wide")

# --------------------------------------------------------
# STATE (for open/close)
# --------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

params = st.query_params
if "sidebar" in params:
    st.session_state.sidebar_open = params.get("sidebar") == "1"

# --------------------------------------------------------
# CSS (no errors, stable)
# --------------------------------------------------------
st.markdown("""
<style>
.app-row {
  display: flex;
  width: 100%;
}

.custom-sidebar {
  width: 360px;
  min-height: 100vh;
  padding: 24px 20px;
  background-image: url('https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
}

/* MAIN CONTENT */
.main-content {
  flex: 1;
  padding: 24px;
}

/* NEON BUTTON */
.neon-btn {
  display: inline-block;
  text-decoration: none;
  color: white !important;
  background: linear-gradient(135deg, #9b00ff, #b300ff);
  padding: 10px 18px;
  font-weight: 700;
  border-radius: 12px;
  box-shadow: 0 8px 36px rgba(179,0,255,0.3);
}

/* CLOSE BUTTON (top-right of sidebar) */
.sidebar-top-right {
  position: absolute;
  top: 18px;
  right: 18px;
}

/* OPEN BUTTON (visible when sidebar closed) */
.open-left {
  position: fixed;
  top: 18px;
  left: 14px;
  z-index: 99999;
  padding: 8px 14px;
  border-radius: 10px;
  font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------
# RENDER LAYOUT
# --------------------------------------------------------
if st.session_state.sidebar_open:

    st.markdown('<div class="app-row">', unsafe_allow_html=True)

    # SIDEBAR HTML
    sidebar_html = """
    <div class="custom-sidebar" id="SIDEBAR">
        <a class="neon-btn sidebar-top-right" href="?sidebar=0">CLOSE</a>
        <div class="sidebar-title" style="margin-top:80px; font-size:26px; font-weight:700; color:white;">
            NEON SIDEBAR
        </div>
        <div class="sidebar-section" style="margin-top:40px; color:white;">
            <p>Sidebar content goes here.</p>
        </div>
    </div>
    """
    st.markdown(sidebar_html, unsafe_allow_html=True)

    # MAIN CONTENT
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.title("Sidebar OPEN")
    st.write("Close button works and background displays.")
    st.markdown("</div></div>", unsafe_allow_html=True)

else:
    # --------------------------------------------------------
    # SIDEBAR CLOSED — OPEN BUTTON VISIBLE
    # --------------------------------------------------------
    st.markdown(
        '<a class="neon-btn open-left" id="OPENBTN" href="?sidebar=1">OPEN</a>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="app-row"><div class="main-content">', unsafe_allow_html=True)
    st.title("Sidebar CLOSED")
    st.write("Open button now appears and works.")
    st.markdown("</div></div>", unsafe_allow_html=True)
