import streamlit as st

st.set_page_config(layout="wide")

# -------------------------------------
# CSS to make Streamlit buttons neon
# -------------------------------------
st.markdown("""
<style>
/* Purple CLOSE button */
div[data-testid="stSidebar"] button[kind="secondary"] {
    background: #b300ff !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 12px 22px !important;
    border: none !important;
    width: 100% !important;
    box-shadow: 0 0 15px #b300ff !important;
    font-size: 18px !important;
}

/* Green OPEN button */
button#open_button button {
    background: #00ff66 !important;
    color: black !important;
    border-radius: 10px !important;
    padding: 12px 22px !important;
    border: none !important;
    box-shadow: 0 0 15px #00ff66 !important;
    font-size: 18px !important;
}

/* Alternative selector (Streamlit uses random structure) */
button[data-testid="open-btn"] {
    background: #00ff66 !important;
    color: black !important;
    border-radius: 10px !important;
    padding: 12px 22px !important;
    border: none !important;
    box-shadow: 0 0 15px #00ff66 !important;
    font-size: 18px !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------
# Sidebar state
# -------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

def close_sidebar():
    st.session_state.sidebar_open = False

def open_sidebar():
    st.session_state.sidebar_open = True

# -------------------------------------
# Sidebar OPEN
# -------------------------------------
if st.session_state.sidebar_open:

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
        st.button("CLOSE", key="close-btn", on_click=close_sidebar)

# -------------------------------------
# Sidebar CLOSED
# -------------------------------------
else:
    st.button("OPEN", key="open-btn", on_click=open_sidebar)

# -------------------------------------
# Main content
# -------------------------------------
st.title("Main App – No-JS Toggle System")
st.write("Sidebar open:", st.session_state.sidebar_open)
