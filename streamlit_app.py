import streamlit as st

# -----------------------------------------------------
#  PAGE CONFIG
# -----------------------------------------------------
st.set_page_config(page_title="Button Project", layout="wide")

# -----------------------------------------------------
#  INITIAL STATE
# -----------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# -----------------------------------------------------
#  BACKGROUND IMAGE CSS FOR SIDEBAR
# -----------------------------------------------------
SIDEBAR_BG = """
<style>
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-image: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
        background-size: cover !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
    }

    /* NEON PURPLE CLOSE BUTTON */
    .neon-close {
        background: #b026ff !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 26px !important;
        border: 2px solid #ff7bff !important;
        box-shadow: 0 0 12px #d17dff, 0 0 20px #b026ff;
        font-weight: 700 !important;
        margin-top: 12px;
        margin-left: 12px;
    }

    /* NEON GREEN OPEN BUTTON */
    .neon-open {
        background: #00ff88 !important;
        color: black !important;
        border-radius: 8px !important;
        padding: 10px 26px !important;
        border: 2px solid #7affc0 !important;
        box-shadow: 0 0 12px #00ff88, 0 0 20px #00cc66;
        font-weight: 700 !important;
        margin-top: 12px;
        margin-left: 12px;
    }
</style>
"""
st.markdown(SIDEBAR_BG, unsafe_allow_html=True)

# -----------------------------------------------------
#  SIDEBAR TOGGLE LOGIC
# -----------------------------------------------------
def open_sidebar():
    st.session_state.sidebar_open = True

def close_sidebar():
    st.session_state.sidebar_open = False

# -----------------------------------------------------
#  RENDER SIDEBAR (only when open)
# -----------------------------------------------------
if st.session_state.sidebar_open:
    with st.sidebar:
        st.markdown("### ")  # spacer

        st.markdown(
            '<button class="neon-close" onclick="window.location.reload()">CLOSE</button>',
            unsafe_allow_html=True
        )

        # Real Streamlit close button (hidden)
        if st.button("hidden_close", key="hidden_close_button"):
            close_sidebar()

# -----------------------------------------------------
#  RENDER OPEN BUTTON WHEN SIDEBAR COLLAPSED
# -----------------------------------------------------
if not st.session_state.sidebar_open:
    st.markdown(
        '<button class="neon-open" onclick="window.location.reload()">OPEN SIDEBAR</button>',
        unsafe_allow_html=True
    )

    if st.button("hidden_open", key="hidden_open_button"):
        open_sidebar()

# -----------------------------------------------------
#  MAIN CONTENT
# -----------------------------------------------------
st.title("Main App")
st.write("This version uses **pure Streamlit** and will not break on Cloud.")

st.write("Sidebar state:", st.session_state.sidebar_open)
