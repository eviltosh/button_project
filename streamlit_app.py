import streamlit as st

# --------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------
st.set_page_config(layout="wide")

RAW_BG = "https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png"

# --------------------------------------------------------
# SESSION STATE
# --------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True


# --------------------------------------------------------
# SIDEBAR RENDER
# --------------------------------------------------------
def render_sidebar():
    """Draw the sidebar with neon CLOSE button + background image."""
    with st.sidebar:
        st.markdown(
            f"""
            <div style="
                position:absolute;
                inset:0;
                background:url('{RAW_BG}') center/cover no-repeat;
                pointer-events:none;   /* ⭐ IMPORTANT FIX — allows button clicks */
                z-index:0;
            "></div>
            """,
            unsafe_allow_html=True
        )

        # Neon purple CLOSE button
        close_clicked = st.button(
            "CLOSE",
            key="close_button",
            help="Close sidebar",
        )
        if close_clicked:
            st.session_state.sidebar_open = False


# --------------------------------------------------------
# TOP-RIGHT OPEN BUTTON
# --------------------------------------------------------
def render_open_button():
    """
    Renders a green OPEN button below Streamlit’s top toolbar.
    Absolutely positioned to top-right.
    """
    st.markdown(
        """
        <style>
            .open-btn {
                position: fixed;
                top: 70px;       /* ⭐ BELOW the Streamlit toolbar */
                right: 25px;
                z-index: 9999;
                background: #00ff88;
                color: #000;
                padding: 10px 22px;
                border-radius: 8px;
                border: 2px solid #00ff88;
                font-weight: 700;
                cursor: pointer;
                box-shadow: 0 0 12px #00ff88;
                transition: 0.15s;
            }
            .open-btn:hover {
                box-shadow: 0 0 22px #00ffaa;
            }
        </style>

        <button class="open-btn" onclick="fetch('?open=1', {method:'POST'}).then(()=>location.reload())">
            OPEN
        </button>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------------
# HANDLE OPEN VIA QUERY
# --------------------------------------------------------
query_params = st.query_params.to_dict()

if "open" in query_params:
    st.session_state.sidebar_open = True


# --------------------------------------------------------
# MAIN PAGE RENDER
# --------------------------------------------------------
if st.session_state.sidebar_open:
    render_sidebar()
else:
    render_open_button()

st.title("Main App")
st.write("Sidebar toggle now uses stable Streamlit session state.")

st.write("Purple CLOSE (single click). Green OPEN (single click).")
st.write("DEBUG: sidebar_open =", st.session_state.sidebar_open)
