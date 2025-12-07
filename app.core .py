# app.core.py  (overwrite your current file)
import streamlit as st

# Page config
st.set_page_config(layout="wide", page_title="Custom Sidebar — Reliable")

# -------------------------
# Session-state: sidebar open/closed
# -------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True  # default open

# -------------------------
# Neon styling for Streamlit buttons and sidebar visuals
# (Targets Streamlit rendered <button> elements; uses !important to override themes)
# -------------------------
st.markdown(
    """
    <style>
    /* Sidebar background mimic for the left column */
    .custom-sidebar-box {
        background-image: url('https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh;
        padding: 20px;
        box-sizing: border-box;
        color: white;
    }

    /* Neon style for Streamlit buttons */
    div.stButton > button, button.css-1emrehy { /* fallback selector for some versions */
        background: linear-gradient(135deg,#9b00ff 0%,#b300ff 100%) !important;
        color: #fff !important;
        border-radius: 12px !important;
        padding: 10px 18px !important;
        font-weight: 700 !important;
        border: 2px solid #b300ff !important;
        box-shadow: 0 8px 30px rgba(179,0,255,0.28), 0 0 36px rgba(179,0,255,0.18) inset !important;
    }

    /* Smaller button when desired */
    .neon-small button {
        padding: 8px 14px !important;
        font-size: 14px !important;
    }

    /* Position helpers inside the sidebar column */
    .sidebar-top-row {
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }

    /* Make main content area sit flush when sidebar is open/closed */
    .main-area {
        padding: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Layout logic:
# - When sidebar is open: render a left column (sidebar) + right column (main)
# - When sidebar is closed: render only main column (full width) but show OPEN button at top-left inside main
# -------------------------
if st.session_state.sidebar_open:
    # 2 columns: sidebar (1) and main (4) -> adjust ratio as desired
    sidebar_col, main_col = st.columns([1, 4])

    # Sidebar column
    with sidebar_col:
        # Container that carries background image via CSS class
        st.markdown('<div class="custom-sidebar-box">', unsafe_allow_html=True)

        # Top row inside sidebar: keep CLOSE button at top-right (prime directive)
        # We create two columns inside the sidebar area: left filler + right for the button
        c1, c2 = st.columns([4, 1])
        with c1:
            st.write("")  # filler - preserves location so close is top-right
        with c2:
            # CLOSE button (streamlit button) — preserved behavior; when clicked it flips state
            if st.button("CLOSE"):
                st.session_state.sidebar_open = False

        # Sidebar title & content (keeps the original visuals/content)
        st.markdown('<div style="margin-top:40px; font-size:24px; font-weight:800; color:white;">NEON SIDEBAR</div>', unsafe_allow_html=True)
        st.markdown('<div style="margin-top:20px; color:white;">Sidebar content goes here.</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)  # close custom-sidebar-box

    # Main column
    with main_col:
        st.markdown('<div class="main-area">', unsafe_allow_html=True)
        st.title("Sidebar OPEN")
        st.write("Close button is top-right in the sidebar. Background image displays. This is the stable mode.")
        # put example widgets (interactive)
        st.text_input("Example input")
        st.selectbox("Example select", ["One", "Two", "Three"])
        st.slider("Example slider", 0, 100, 25)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # Sidebar closed: show full-width main content, but provide an OPEN button at top-left
    st.markdown('<div class="main-area">', unsafe_allow_html=True)

    # Place the OPEN button in a tiny two-column row so it appears left-aligned
    left_col, right_col = st.columns([1, 6])
    with left_col:
        # Use a smaller neon button style optionally
        if st.button("OPEN"):
            st.session_state.sidebar_open = True
    with right_col:
        st.write("")  # filler

    st.title("Sidebar CLOSED")
    st.write("Sidebar is collapsed. Click OPEN to show it again.")
    # example widgets in closed state
    st.text_input("Example input")
    st.selectbox("Example select", ["A", "B", "C"])
    st.slider("Example slider", 0, 50, 10)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Debug info (optional; remove if you don't want it)
# -------------------------
st.markdown("---")
st.write("session_state.sidebar_open:", st.session_state.sidebar_open)
