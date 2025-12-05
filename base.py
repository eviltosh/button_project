import streamlit as st

# -------------------------
# SESSION STATE
# -------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True


# -------------------------
# BASE CSS
# -------------------------
st.markdown("""
<style>

    /* Sidebar transition */
    [data-testid="stSidebar"] {
        transition: all 0.25s ease-in-out;
    }

    /* Purple neon button */
    .neon-purple button {
        background-color: #b300ff !important;
        color: white !important;
        border: 2px solid #ff00ff !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 0 10px #ff00ff, 0 0 20px #b300ff !important;
    }

    /* Green neon button */
    .neon-green button {
        background-color: #00ff00 !important;
        color: black !important;
        border: 2px solid #00ffaa !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 0 10px #00ff00, 0 0 20px #00aa00 !important;
    }

</style>
""", unsafe_allow_html=True)


# -------------------------
# SIDEBAR OPEN
# ----------------------
