import streamlit as st

# ---------------------------------------------------------
# 1) INIT SESSION STATE
# ---------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = False


# ---------------------------------------------------------
# 2) GLOBAL CSS (ROOT LEVEL, NOT SIDEBAR)
# ---------------------------------------------------------
st.markdown("""
<style>

button[kind="secondary"] {
    background-color: #444 !important;
}

/* OPEN button (green) */
#open_btn button {
    background-color: #00cc66 !important;
    color: black !important;
    font-weight: 700 !important;
    border-radius: 6px !important;
}

/* CLOSE button (purple) */
#close_btn button {
    background-color: #b300ff !important;
    color: white !important;
    font-weight: 700 !important;
    border-radius: 6px !important;
}

/* Sidebar full background */
section[data-testid="stSidebar"] {
    background-image: url('https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png');
    background-size: cover;
    background-position: center;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# 3) SIDEBAR LOGIC
# ---------------------------------------------------------
if st.session_state.sidebar_open:
    with st.sidebar:
        st.markdown("### ")

        # This box forces a stable DOM target (#close_btn)
        close_box = st.container()
        with close_box:
            st.markdown('<div id="close_btn">', unsafe_allow_html=True)
            if st.button("CLOSE", key="close_visible"):
                st.session_state.sidebar_open = False
            st.markdown('</div>', unsafe_allow_html=True)

        # Hidden internal control (still needed)
        if st.button("hidden_close", key="hidden_close"):
            st.session_state.sidebar_open = False


# ---------------------------------------------------------
# 4) MAIN PAGE
# ---------------------------------------------------------
# OPEN button container (stable DOM target)
st.markdown('<div id="open_btn">', unsafe_allow_html=True)
if not st.session_state.sidebar_open:
    if st.button("OPEN", key="open_visible"):
        st.session_state.sidebar_open = True
st.markdown('</div>', unsafe_allow_html=True)

# Hidden open button
if st.button("hidden_open", key="hidden_open"):
    st.session_state.sidebar_open = True


# ---------------------------------------------------------
# 5) MAIN CONTENT
# ---------------------------------------------------------
st.title("Main App – No-JS Toggle System")

st.write("Sidebar open:", st.session_state.sidebar_open)
