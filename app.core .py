# app.core.py  <- make sure filename exactly this (no trailing space)
import streamlit as st

# -------------------------
# Read explicit query param (if any) so HTML links can control state on reload
# -------------------------
params = st.experimental_get_query_params()
sidebar_q = params.get("sidebar", [None])[0]  # expected "1" or "0" or None

# -------------------------
# Initialize session state (fallback to expanded)
# -------------------------
if "sidebar_open" not in st.session_state:
    if sidebar_q is not None:
        st.session_state.sidebar_open = True if sidebar_q == "1" else False
    else:
        st.session_state.sidebar_open = True  # default open

# If query param present, prefer it (makes the HTML links deterministic)
if sidebar_q is not None:
    st.session_state.sidebar_open = True if sidebar_q == "1" else False

# -------------------------
# Page config (use initial_sidebar_state only for consistency; we don't rely on Streamlit built-in sidebar)
# -------------------------
st.set_page_config(page_title="Custom Sidebar — Reliable", layout="wide", initial_sidebar_state="expanded")

# -------------------------
# Styling for the custom sidebar + neon button
# - We use only CSS injected via st.markdown(unsafe_allow_html=True)
# - Buttons are simple <a href="?sidebar=1"> links which reload the page with the desired param
# -------------------------
css = """
<style>
/* Layout helpers */
.app-row {
  display: flex;
  width: 100%;
  gap: 0;
  align-items: flex-start;
}

/* Sidebar container mimic */
.custom-sidebar {
  width: 360px;            /* change this if you want different sidebar width */
  min-height: 100vh;
  box-sizing: border-box;
  padding: 24px 20px;
  background-image: url('https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  border-right: 1px solid rgba(0,0,0,0.06);
  position: relative;
}

/* Main content takes remaining space */
.main-content {
  flex: 1;
  padding: 24px;
}

/* Neon button (anchor) */
.neon-btn {
  display: inline-block;
  text-decoration: none;
  color: white !important;
  background: linear-gradient(135deg, #9b00ff 0%, #b300ff 100%);
  padding: 10px 18px;
  font-weight: 700;
  border-radius: 12px;
  box-shadow: 0 8px 30px rgba(179,0,255,0.28), 0 0 36px rgba(179,0,255,0.18) inset;
  transition: transform 120ms ease, box-shadow 120ms ease;
  border: none;
}

/* hover */
.neon-btn:hover {
  transform: translateY(-3px);
}

/* Positioning: top-right of sidebar area */
.neon-btn.sidebar-top-right {
  position: absolute;
  top: 18px;
  right: 18px;
  z-index: 9999;
}

/* Small open button when sidebar is closed (left edge) */
.neon-btn.open-left {
  position: fixed;
  top: 18px;
  left: 12px;
  z-index: 9999;
  padding: 8px 12px;
  border-radius: 10px;
  font-size: 14px;
}

/* small visual niceties */
.sidebar-title {
  margin-top: 56px; /* leave room for the top-right button visually */
  color: white;
  text-shadow: 0 2px 8px rgba(0,0,0,0.4);
  font-weight: 800;
  font-size: 20px;
}
.sidebar-section {
  margin-top: 18px;
  background: rgba(255,255,255,0.03);
  padding: 12px;
  border-radius: 8px;
  color: #fff;
}

/* Make main content text readable */
body .main-content, body .main-content p {
  color: #111;
  background: #fff;
}

/* Small responsive tweak */
@media (max-width: 900px) {
  .custom-sidebar {
    display: none; /* on small screens hide the fake sidebar; the open button will be used */
  }
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# -------------------------
# Build layout:
# If sidebar_open: show sidebar container + main content
# If closed: show only main content, and an OPEN button positioned at left
# -------------------------
if st.session_state.sidebar_open:
    # Sidebar is visible — render the sidebar container and the neon close button (top-right inside sidebar)
    st.markdown('<div class="app-row">', unsafe_allow_html=True)
    sidebar_html = f"""
    <div class="custom-sidebar">
      <a class="neon-btn sidebar-top-right" href="?sidebar=0" aria-label="Close sidebar">CLOSE</a>
      <div class="sidebar-title">NEON SIDEBAR</div>
      <div class="sidebar-section">
        <p><strong>Links</strong></p>
        <ul>
          <li>Home</li>
          <li>Dashboard</li>
          <li>Settings</li>
        </ul>
      </div>
      <div class="sidebar-section">
        <p><strong>Controls</strong></p>
        <p>Use the Close button top-right to collapse the sidebar.</p>
      </div>
    </div>
    """
    st.markdown(sidebar_html, unsafe_allow_html=True)

    # Main content column
    main_html = """
    <div class="main-content">
    """
    st.markdown(main_html, unsafe_allow_html=True)

    # Place some interactive Streamlit widgets (they live in the main content area)
    st.header("Main App — Sidebar OPEN (custom)")
    st.write("This is a fully controlled custom sidebar. It does not rely on Streamlit's built-in sidebar.")
    st.write("Click CLOSE (top-right of sidebar) to collapse the sidebar. That link reloads the page with ?sidebar=0 and Python will read it.")
    # example controls
    st.text_input("Example input")
    st.selectbox("Example select", ["One", "Two", "Three"])
    st.slider("Example slider", 0, 100, 25)

    # close the main content div
    st.markdown("</div></div>", unsafe_allow_html=True)

else:
    # Sidebar is closed — render only main content and an OPEN button at left edge
    # The OPEN anchor reloads page with ?sidebar=1 which we read on load
    st.markdown('<div class="app-row">', unsafe_allow_html=True)
    # No sidebar HTML inserted (hidden)
    main_html = """
    <div class="main-content">
    """
    st.markdown(main_html, unsafe_allow_html=True)

    # Render the open button (styled anchor)
    st.markdown('<a class="neon-btn open-left" href="?sidebar=1" aria-label="Open sidebar">OPEN</a>', unsafe_allow_html=True)

    st.header("Main App — Sidebar COLLAPSED (custom)")
    st.write("Sidebar is collapsed. Click OPEN (left) to show the custom sidebar.")
    st.write("This is pure Streamlit + HTML anchors; no JS necessary.")

    # example controls
    st.text_input("Example input")
    st.selectbox("Example select", ["A", "B", "C"])
    st.slider("Example slider", 0, 50, 10)

    st.markdown("</div></div>", unsafe_allow_html=True)

# -------------------------
# Debug / Info (optional)
# -------------------------
st.markdown("---")
st.write("session_state.sidebar_open:", st.session_state.sidebar_open)
st.write("Tip: If you want the sidebar width changed, edit the CSS `.custom-sidebar { width: ...px; }` in this file.")
