import streamlit as st

st.set_page_config(layout="wide")

# -----------------------------
# Read URL params
# -----------------------------
params = st.query_params
if "close" in params:
    st.session_state.sidebar_open = False
if "open" in params:
    st.session_state.sidebar_open = True

# Init default
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True


# -----------------------------
# Sidebar OPEN
# -----------------------------
if st.session_state.sidebar_open:

    # Full background
    st.markdown("""
        <style>
        section[data-testid="stSidebar"] {
            background: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
            background-size: cover;
            background-position: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # PURPLE CLOSE BUTTON (works 100%)
    st.sidebar.markdown(
        """
        <a href="?close=1">
            <button style="
                background:#b300ff;
                color:white;
                padding:10px 20px;
                border:none;
                border-radius:6px;
                font-size:16px;
                cursor:pointer;
                width:100%;
                margin-bottom:20px;
            ">
                CLOSE
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

else:

    # GREEN OPEN BUTTON (works 100%)
    st.markdown(
        """
        <a href="?open=1">
            <button style="
                background:#00ff66;
                color:black;
                padding:10px 20px;
                border:none;
                border-radius:6px;
                font-size:16px;
                cursor:pointer;
                font-size:16px;
            ">
                OPEN SIDEBAR
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# MAIN APP
# -----------------------------
st.title("Main App – QueryParam Toggle System (Bulletproof)")
st.write("Sidebar:", st.session_state.sidebar_open)
