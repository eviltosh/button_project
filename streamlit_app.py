import streamlit as st

st.set_page_config(layout="wide")

RAW_URL = "https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png"

# STATE
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# TOGGLE FUNCTIONS
def toggle_sidebar():
    st.session_state.sidebar_open = not st.session_state.sidebar_open

# WIDTH LOGIC
sidebar_width = "300px" if st.session_state.sidebar_open else "0px"

# ---------------------- CSS ----------------------
css = f"""
<style>
/* Sidebar container width */
[data-testid="stSidebar"] {{
    width: {sidebar_width} !important;
    min-width: {sidebar_width} !important;
    max-width: {sidebar_width} !important;
    padding: 0 !important;
    overflow: hidden !important;
    transition: width 0.15s ease-out;
}}

/* Sidebar background image */
[data-testid="stSidebar"] > div:first-child {{
    background-image: url('{RAW_URL}');
    background-size: cover;
    background-position: center;
    padding-top: 70px; /* space for close button */
}}

/* PURPLE CLOSE BUTTON */
.close-btn {{
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
    z-index: 1000;
}}
.close-btn:hover {{
    background: #c94dff;
}}

/* GREEN OPEN BUTTON */
.open-btn {{
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
    z-index: 1000;
    display: {"none" if st.session_state.sidebar_open else "block"};
}}
.open-btn:hover {{
    background: #66ff66;
}}
</style>
"""
st.markdown(css, unsafe_allow_html=True)
# -------------------------------------------------

# OPEN BUTTON
if not st.session_state.sidebar_open:
    if st.button("OPEN SIDEBAR", key="open_button"):
        toggle_sidebar()

    st.markdown(
        "<button class='open-btn'>OPEN</button>",
        unsafe_allow_html=True
    )

# CLOSE BUTTON
if st.session_state.sidebar_open:
    with st.sidebar:
        if st.button("CLOSE SIDEBAR", key="close_button"):
            toggle_sidebar()

        st.markdown(
            "<button class='close-btn'>CLOSE</button>",
            unsafe_allow_html=True
        )

# MAIN CONTENT
st.title("Main App")
st.write("Sidebar toggle is working with neon buttons.")
