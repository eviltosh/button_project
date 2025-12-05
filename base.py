import streamlit as st

if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# -------------------------
# CSS COLLAPSE / EXPAND
# -------------------------
if st.session_state.sidebar_open:
    st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            width: 300px !important;
            min-width: 300px !important;
        }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            width: 0 !important;
            min-width: 0 !important;
            overflow: hidden !important;
        }
    </style>
    """, unsafe_allow_html=True)

# -------------------------
# HEADER-PLACED OPEN BUTTON (Streamlit top-right system bar)
# -------------------------
if not st.session_state.sidebar_open:
    top_cols = st.columns([15, 1])   # rightmost column is ALWAYS at the top-right
    with top_cols[1]:
        if st.button("Open", key="header_open"):
            st.session_state.sidebar_open = True
            st.rerun()

# -------------------------
# SIDEBAR CONTENT + CLOSE BUTTON
# -------------------------
if st.session_state.sidebar_open:
    with st.sidebar:
        colA, colB = st.columns([3, 1])
        with colB:
            if st.button("Close", key="close_btn"):
                st.session_state.sidebar_open = False
                st.rerun()

# -------------------------
# MAIN
# -------------------------
st.title("Header-Aligned Top-Right Open Button")
st.write("This method uses Streamlit’s header area for perfect top-right placement.")
