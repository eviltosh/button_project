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
# TOP-RIGHT OPEN BUTTON (MAIN AREA)
# -------------------------
if not st.session_state.sidebar_open:
    col1, col2 = st.columns([8, 1])  # right-align
    with col2:
        if st.button("Open", key="open_btn"):
            st.session_state.sidebar_open = True
            st.rerun()


# -------------------------
# SIDEBAR CONTENT + CLOSE BUTTON
# -------------------------
if st.session_state.sidebar_open:
    with st.sidebar:
        colA, colB = st.columns([4, 1])
        with colB:
            if st.button("Close", key="close_btn"):
                st.session_state.sidebar_open = False
                st.rerun()


# -------------------------
# MAIN
# -------------------------
st.title("New Method: Column-Aligned Toggle")
st.write("No JS. No DOM. No crashes. Guaranteed to render.")
