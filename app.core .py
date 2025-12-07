import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# --------------------------------------------------------
# STATE CONTROL (now purely internal)
# --------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# --------------------------------------------------------
# CSS — SAME DESIGN, SAME CLOSE BUTTON, SAME OPEN BUTTON
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
  position: fixed;
  top: 0;
  left: 0;
  transition: transform 0.35s ease-in-out;
  z-index: 9999998;
}

.custom-sidebar.closed {
  transform: translateX(-380px);
}

/* MAIN CONTENT */
.main-content {
  flex: 1;
  padding: 24px;
  margin-left: 380px;
}

/* Adjust when sidebar is closed */
.main-content.sidebar-closed {
  margin-left: 0px;
}

/* =======================================================
   NEON BUTTON (UNCHANGED STYLE)
   ======================================================= */
.neon-btn {
  text-decoration: none !important;
  color: #ffffff !important;
  background: linear-gradient(135deg, #9b00ff 0%, #b300ff 100%) !important;
  padding: 12px 20px !important;
  font-weight: 700 !important;
  font-size: 15px !important;
  border-radius: 12px !important;
  box-shadow: 0 0 12px #b300ff, 0 0 28px rgba(179,0,255,0.7) !important;
  border: 2px solid #b300ff !important;
  cursor: pointer !important;
  display: inline-block !important;
  position: fixed !important;
  z-index: 9999999 !important;
}

/* CLOSE BUTTON (UNCHANGED POSITION) */
#close-btn {
  top: 18px;
  left: 300px;
}

/* OPEN BUTTON (UNCHANGED POSITION) */
#open-btn {
  top: 20px;
  left: 20px;
}

/* Hide open button when sidebar is visible */
#open-btn.hidden {
  display: none !important;
}

/* Hide close button when sidebar is hidden */
#close-btn.hidden {
  display: none !important;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------
# HTML + JS — No Page Reload, No Navigation
# --------------------------------------------------------

html = f"""
<div id="sidebar" class="custom-sidebar {'open' if st.session_state.sidebar_open else 'closed'}">

    <button id="close-btn" class="neon-btn {'hidden' if not st.session_state.sidebar_open else ''}" onclick="closeSidebar()">
        CLOSE
    </button>

    <div style="margin-top:80px; font-size:26px; font-weight:700; color:white;">
        NEON SIDEBAR
    </div>

    <div style="margin-top:40px; color:white;">
        <p>Sidebar content goes here.</p>
    </div>

</div>

<button id="open-btn" class="neon-btn {'hidden' if st.session_state.sidebar_open else ''}" onclick="openSidebar()">
    OPEN
</button>

<script>

function openSidebar() {{
    const s = window.parent.document.getElementById("sidebar");
    const o = window.parent.document.getElementById("open-btn");
    const c = window.parent.document.getElementById("close-btn");

    s.classList.remove("closed");
    s.classList.add("open");

    o.classList.add("hidden");
    c.classList.remove("hidden");
}}

function closeSidebar() {{
    const s = window.parent.document.getElementById("sidebar");
    const o = window.parent.document.getElementById("open-btn");
    const c = window.parent.document.getElementById("close-btn");

    s.classList.remove("open");
    s.classList.add("closed");

    o.classList.remove("hidden");
    c.classList.add("hidden");
}}

</script>
"""

components.html(html, height=0)

# --------------------------------------------------------
# MAIN CONTENT
# --------------------------------------------------------
sidebar_closed_class = "sidebar-closed" if not st.session_state.sidebar_open else ""

st.markdown(f'<div class="main-content {sidebar_closed_class}">', unsafe_allow_html=True)

if st.session_state.sidebar_open:
    st.title("Sidebar OPEN")
else:
    st.title("Sidebar CLOSED")

st.write("Open + Close now work WITHOUT page navigation and WITHOUT breaking design.")

st.markdown("</div>", unsafe_allow_html=True)
