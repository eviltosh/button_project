import streamlit as st

st.set_page_config(layout="wide")

RAW_URL = "https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png"

# STATE
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# TOGGLE FUNCTIONS
def close_sidebar():
    st.session_state.sidebar_open = False
    st.experimental_rerun()

def open_sidebar():
    st.session_state.sidebar_open = True
    st.experimental_rerun()

# SIDEBAR WIDTH
sidebar_width = "300px" if st.session_state.sidebar_open else "0px"

# ---------------------- CSS ----------------------
css = f"""
<style>
/* Sidebar background */
[data-testid="stSidebar"] {{
    width: {sidebar_width} !important;
    min-width: {sidebar_width} !important;
    max-width: {sidebar_width} !important;
    padding: 0;
    overflow: hidden !important;
    transition: width 0.1s ease-out;
}}
[data-testid="stSidebar"] > div:first-child {{
    background-image: url('{RAW_URL}');
    background-size: cover;
    background-position: center;
}}

/* CLOSE BUTTON */
#close-btn {{
    position: absolute;
    top: 12px;
    right: 12px;
    padding: 10px 16px;
    background: #9b00ff;
    color: white;
    font-weight: 700;
    border-radius: 10px;
    border: 2px solid #ffb5ff;
    cursor: pointer;
    z-index: 9999;
}}
#close-btn:hover {{
    background: #c94dff;
}}

/* OPEN BUTTON */
#open-btn {{
    position: fixed;
    top: 12px;
    right: 12px;
    padding: 12px 18px;
    background: #33ff33;
    color: black;
    font-weight: 700;
    border-radius: 10px;
    border: 2px solid #aaffaa;
    cursor: pointer;
    z-index: 9999;
    display: {"none" if st.session_state.sidebar_open else "block"};
}}
#open-btn:hover {{
    background: #66ff66;
}}
</style>
"""
st.markdown(css, unsafe_allow_html=True)
# -------------------------------------------------

# CLOSE BUTTON in sidebar (custom HTML)
if st.session_state.sidebar_open:
    with st.sidebar:
        st.markdown(
            """
            <button id="close-btn" onclick="fetch('/close', {method:'POST'})">CLOSE</button>
            """,
            unsafe_allow_html=True
        )

# OPEN BUTTON (custom HTML)
if not st.session_state.sidebar_open:
    st.markdown(
        """
        <button id="open-btn" onclick="fetch('/open', {method:'POST'})">OPEN</button>
        """,
        unsafe_allow_html=True
    )

# HIDDEN API ENDPOINTS FOR BUTTONS
def _close_handler():
    close_sidebar()

def _open_handler():
    open_sidebar()

st.experimental_http_endpoint("/close")(_close_handler)
st.experimental_http_endpoint("/open")(_open_handler)

# MAIN APP CONTENT
st.title("Main App")
