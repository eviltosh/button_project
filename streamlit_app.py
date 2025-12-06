import streamlit as st

st.set_page_config(layout="wide")

# Initialize state
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True


# ---- CSS ----
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
    background-size: cover;
    background-position: center;
}

/* Purple CLOSE button */
.neon-close {
    position: absolute;
    top: 40px;
    right: 30px;
    padding: 10px 22px;
    font-weight: 800;
    color: white;
    background: #a000ff;
    border-radius: 8px;
    border: 2px solid #ff66ff;
    box-shadow: 0 0 20px #a000ff;
    cursor: pointer;
}

/* Green OPEN button */
.neon-open {
    position: fixed;
    top: 40px;
    left: 40px;
    padding: 10px 22px;
    font-weight: 800;
    color: white;
    background: #00ff66;
    border-radius: 8px;
    border: 2px solid #00ff99;
    box-shadow: 0 0 20px #00ff66;
    cursor: pointer;
    z-index: 999999;
}
</style>
""", unsafe_allow_html=True)


# ---- LOGIC ----

def close_sidebar():
    st.session_state.sidebar_open = False

def open_sidebar():
    st.session_state.sidebar_open = True


# ---- SIDEBAR ----
if st.session_state.sidebar_open:
    with st.sidebar:
        st.markdown(
            '<button class="neon-close" onclick="document.getElementById(\'close_button\').click()">CLOSE</button>',
            unsafe_allow_html=True
        )
        st.button("hidden close", key="close_bu_
