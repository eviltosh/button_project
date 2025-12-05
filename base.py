import streamlit as st

if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True


# ============================================================
#   TOP-RIGHT ANCHOR USING st.empty()  (NEW METHOD)
# ============================================================

top_anchor = st.empty()   # Always stays at top of page

with top_anchor.container():
    if not st.session_state.sidebar_open:
        c1, c2 = st.columns([12, 1])  # right-aligned anchor
        with c2:
            if st.button("Open", key="open_btn"):
                st.session_state.sidebar_open = True
                st.rerun()


# ============================================================
#   CSS COLLAPSE / EXPAND (unchanged, safe)
# ============================================================

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


# ============================================================
#   SIDEBAR CONTENT + CLOSE BUTTON
# ============================================================

if st.session_state.sidebar_open:
    with st.sidebar:
        cA, cB = st.columns([3, 1])
        with cB:
            if st.button("Close", key="close_btn"):
                st.session_state.sidebar_open = False
                st.rerun()


# ============================================================
#   MAIN CONTENT
# ============================================================

st.title("ANCHOR METHOD — TOP RIGHT BUTTON")
st.write("Using st.empty() as a persistent top-right anchor.")
