import streamlit as st

st.set_page_config(layout="wide")

# ----------------------------------------------------
# CSS THAT WORKS ON STREAMLIT CLOUD
# ----------------------------------------------------
st.markdown("""
<style>

/* PURPLE CLOSE BUTTON */
span.close-label {
    display: inline-block;
    background: #b300ff !important;
    color: white !important;
    padding: 8px 18px !important;
    border-radius: 8px !important;
    box-shadow: 0 0 12px #b300ff !important;
    font-size: 16px !important;
    font-weight: 600;
}

/* GREEN OPEN BUTTON */
span.open-label {
    display: inline-block;
    background: #00ff66 !important;
    color: black !important;
    padding: 8px 18px !important;
    border-radius: 8px !important;
    box-shadow: 0 0 12px #00ff66 !important;
    font-size: 16px !important;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# Sidebar state logic (unchanged)
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
        # BUTTON LABEL WITH CUSTOM HTML SPAN
        st.button(
            "✖ <span class='close-label'>CLOSE</span>",
            key="close-btn",
            on_click=close_sidebar,
            help="close sidebar",
            use_container_width=True
        )

# ----------------------------------------------------
# Sidebar CLOSED
# ----------------------------------------------------
else:
    st.button(
        "▶ <span class='open-label'>OPEN</span>",
        key="open-btn",
        on_click=open_sidebar,
        help="open sidebar",
        use_container_width=True,
    )

# ----------------------------------------------------
# Main content
# ----------------------------------------------------
st.title("Main App – No JS Toggle System")
st.write("Sidebar open:", st.session_state.sidebar_open)
