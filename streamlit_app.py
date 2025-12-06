import streamlit as st

st.set_page_config(layout="wide")

RAW_URL = "https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png"

# Session state toggle
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# Toggle functions
def close_sidebar():
    st.session_state.sidebar_open = False

def open_sidebar():
    st.session_state.sidebar_open = True

# --- APPLY CSS ---
sidebar_width = "300px" if st.session_state.sidebar_open else "0px"

css = f"""
<style>
/* Sidebar background */
[data-testid="stSidebar"] {{
    width: {sidebar_width} !important;
    min-width: {sidebar_width} !important;
    max-width: {sidebar_width} !important;
    overflow: hidden !important;
    transition: all 0.3s ease-in-out;
}}
[data-testid="stSidebar"] > div:first-child {{
    background-image: url('{RAW_URL}');
    background-size: cover;
    background-position: center;
}}

/* CLOSE BUTTON (inside sidebar) */
.sidebar-close-btn {{
    position: absolute;
    top: 12px;
    right: 12px;
    padding: 8px 14px;
    background: #9500ff;
    border-radius: 8px;
    border: 2px solid #f0caff;
    font-weight: bold;
    color: white;
    cursor: pointer;
}}

/* OPEN BUTTON (main screen) */
.open-btn {{
    position: fixed;
    top: 12px;
    right: 12px;
    padding: 10px 16px;
    background: #33ff33;
    border-radius: 10px;
    border: 2px solid #bbffbb;
    font-weight: bold;
    cursor: pointer;
    z-index: 9999;
    display: { "none" if st.session_state.sidebar_open else "block" };
}}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
if st.session_state.sidebar_open:
    with st.sidebar:
        if st.button("CLOSE", key="close_btn"):
            close_sidebar()

# --- OPEN BUTTON ---
if not st.session_state.sidebar_open:
    if st.button("OPEN SIDEBAR", key="open_btn"):
        open_sidebar()

# --- MAIN CONTENT ---
st.title("Main App")

