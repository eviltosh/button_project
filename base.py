import streamlit as st

if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        transition: all 0.25s ease-in-out;
    }

    .neon-purple button {
        background-color: #b300ff !important;
        color: white !important;
        border: 2px solid #ff00ff !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 0 10px #ff00ff, 0 0 20px #b300ff !important;
    }

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

# -------- OPEN STATE --------
if st.session_state.sidebar_open:

    st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            width: 300px !important;
            min-width: 300px !important;
            visibility: visible !important;
        }
        .sidebar-top-right {
            position: absolute;
            top: 10px;
            right: 10px;
            z-index: 999;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown('<div class="sidebar-top-right neon-purple">', unsafe_allow_html=True)
        if st.button("Close"):
            st.session_state.sidebar_open = False
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# -------- CLOSED STATE --------
else:

    st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            width: 0 !important;
            min-width: 0 !important;
            visibility: hidden !important;
        }

        .green-floating {
            position: fixed;
            top: 10px;
            right: 10px;
            left: auto !important;
            z-index: 2000;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="green-floating neon-green">', unsafe_allow_html=True)
    if st.button("Open"):
        st.session_state.sidebar_open = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.title("Sidebar Toggle Test — SAFE MODE")
