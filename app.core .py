import streamlit as st

st.set_page_config(layout="wide")

# ----------------------------------------------------
# CSS — works by targeting EACH button key using data-testid
# ----------------------------------------------------
st.markdown("""
<style>

button[kind="secondary"][data-testid="baseButton-close"] {
    background: #b300ff !important;
    color: white !important;
    border-radius: 8px !important;
    border: none !important;
    box-shadow: 0 0 12px #b300ff !important;
}

button[kind="secondary"][data-testid="baseButton-open"] {
    background: #00ff66 !important;
    color: black !important;
    border-radius: 8px !important;
    border: none !important;
    box-shadow: 0 0 12px #00ff66 !important;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# Session state
# ----------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

def close_sidebar():
    st.session_state.sidebar_open = False

def open_sidebar():
    st.session_state.sidebar_open = True

# ----------------------------------------------------
# Sidebar OPEN
# ----------------------------------------------------
if st.session_state.sidebar_open:

    # Sidebar background
    st.markdown("""
        <style>
        section[data-testid="stSidebar"] {
            background: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
            background-size: cover;
            background-position: center;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.button("CLOSE", key="close", on_click=close_sidebar)

# ----------------------------------------------------
# Sidebar CLOSED
# ----------------------------------------------------
else:
    st.button("OPEN", key="open", on_click=open_sidebar)

# ----------------------------------------------------
# Main app
# ----------------------------------------------------
st.title("Main App – No JS Toggle System")
st.write("Sidebar open:", st.session_state.sidebar_open)

