import streamlit as st

# --------------------------
# INIT SESSION STATE
# --------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True


# --------------------------
# TOGGLE FUNCTIONS
# --------------------------
def close_sidebar():
    st.session_state.sidebar_open = False


def open_sidebar():
    st.session_state.sidebar_open = True


# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(page_title="Button Project", layout="wide")


# --------------------------
# GLOBAL CSS (background + neon buttons + hide chevrons)
# --------------------------
st.markdown("""
<style>

    /* FORCE SIDEBAR IMAGE FULL COVER */
    [data-testid="stSidebar"] {
        background-image: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
        background-size: cover !important;
        background-position: center !important;
        background-repeat: no-repeat !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Remove inner containers blocking the image */
    [data-testid="stSidebar"] > div {
        background: transparent !important;
        padding: 0 !important;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* REMOVE STREAMLIT CHEVRONS */
    button[kind="header"] {
        display: none !important;
    }

    /* PURPLE NEON CLOSE BUTTON (inside sidebar) */
    .purple-btn {
        background-color: #8a2be2 !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 10px 25px !important;
        border: 2px solid #c084fc !important;
        box-shadow: 0 0 12px #c084fc !important;
        font-weight: bold !important;
        margin-top: 20px;
    }

    /* GREEN NEON OPEN BUTTON (floating top right) */
    .green-btn {
        position: fixed;
        top: 20px;
        right: 30px;
        z-index: 99999 !important;
        background-color: #22c55e !important;
        color: black !important;
        border-radius: 10px !important;
        padding: 10px 25px !important;
        border: 2px solid #86efac !important;
        box-shadow: 0 0 12px #86efac !important;
        font-weight: bold !important;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------
# RENDER OPEN BUTTON (only when sidebar closed)
# --------------------------
if not st.session_state.sidebar_open:
    if st.button("Open Sidebar", key="open_btn", help="Open menu",
                 use_container_width=False):
        open_sidebar()

    # Apply green CSS
    st.markdown("""
        <script>
            document.querySelector('button[data-testid="open_btn"]').classList.add('green-btn');
        </script>
    """, unsafe_allow_html=True)


# --------------------------
# SIDEBAR CONTENT
# --------------------------
if st.session_state.sidebar_open:
    with st.sidebar:
        st.write("")  # spacer

        # Purple CLOSE button
        if st.button("Close Sidebar", key="close_btn", help="Hide menu"):
            close_sidebar()

        # Apply purple CSS
        st.markdown("""
            <script>
                document.querySelector('button[data-testid="close_btn"]').classList.add('purple-btn');
            </script>
        """, unsafe_allow_html=True)


# --------------------------
# MAIN APP
# --------------------------
st.title("Main App")
st.write("This version uses **pure Streamlit** and will not break on Cloud.")

st.write(f"Sidebar state: `{st.session_state.sidebar_open}`")
