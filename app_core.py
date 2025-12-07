import streamlit as st

st.set_page_config(layout="wide", page_title="Neon Sidebar Toggle")

# --------------------------------------------------------
# STATE CONTROL
# --------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# Sync with ?sidebar= param if present
params = st.query_params
if "sidebar" in params:
    st.session_state.sidebar_open = params.get("sidebar") == "1"

# --------------------------------------------------------
# CSS STYLING
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

/* =======================================================
   NEON BUTTON (Global)
   ======================================================= */
.neon-btn {
  display: inline-block !important;
  text-decoration: none !important;
  color: #ffffff !important;
  background: linear-gradient(135deg, #9b00ff 0%, #b300ff 100%) !important;
  padding: 12px 20px !important;
  font-weight: 700 !important;
  font-size: 15px !important;
  border-radius: 12px !important;
  box-shadow: 0 0 12px #b300ff, 0 0 28px rgba(179,0,255,0.7) !important;
  border: 2px solid #b300ff !important;
  cursor: pointer;
  z-index: 999999 !important;
}

.neon-btn:hover {
  transform: scale(1.05);
}

/* CLOSE BUTTON (inside sidebar) */
.sidebar-top-right {
  position: absolute !important;
  top: 18px !important;
  right: 18px !important;
}

/* OPEN button — fixed top-left */
.open-left {
  position: fixed !important;
  top: 20px !important;
  left: 20px !important;
  z-index: 999999 !important;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------
# RENDERING
# --------------------------------------------------------
if st.session_state.sidebar_open:

    # WRAP ROW
    st.markdown('<div class="app-row">', unsafe_allow_html=True)

    # ----------------------------------------
    # SIDEBAR HTML (correct, clean, safe)
    # ----------------------------------------
    sidebar_html = """
    <div class="custom-sidebar" id="SIDEBAR">

        <a class="neon-btn sidebar-top-right" onclick="closeSide()" href="javascript:void(0);">CLOSE</a>

        <script>
        function closeSide() {
            const url = new URL(window.location.href);
            url.searchParams.set("sidebar", "0");
            window.location.replace(url.toString());
        }
        </script>

        <div style="margin-top:80px; font-size:26px; font-weight:700; color:white;">
            NEON SIDEBAR
        </div>

        <div style="margin-top:40px; color:white;">
            <p>Sidebar content goes here.</p>
        </div>

    </div>
    """
    st.markdown(sidebar_html, unsafe_allow_html=True)

    # ----------------------------------------
    # MAIN CONTENT
    # ----------------------------------------
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.title("Sidebar OPEN")
    st.write("Close button works. Background displayed.")
    st.markdown("</div></div>", unsafe_allow_html=True)

else:
    # --------------------------------------------------------
    # SIDEBAR CLOSED → SHOW OPEN BUTTON
    # --------------------------------------------------------
    open_btn = """
    <a class="neon-btn open-left" onclick="openSide()" href="javascript:void(0);">OPEN</a>

    <script>
    function openSide() {
        const url = new URL(window.location.href);
        url.searchParams.set("sidebar", "1");
        window.location.replace(url.toString());
    }
    </script>
    """
    st.markdown(open_btn, unsafe_allow_html=True)

    # Main content
    st.markdown('<div class="app-row"><div class="main-content">', unsafe_allow_html=True)
    st.title("Sidebar CLOSED")
    st.write("Open button now appears and works.")
    st.markdown("</div></div>", unsafe_allow_html=True)
