import streamlit as st

# --------------------------------------------------------
# INITIAL SIDEBAR STATE
# --------------------------------------------------------
if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = "expanded"  # "expanded" or "collapsed"

# Page setup using the stored state
st.set_page_config(
    page_title="Sidebar Toggle System",
    layout="wide",
    initial_sidebar_state=st.session_state.sidebar_state,
)

# --------------------------------------------------------
# UI
# --------------------------------------------------------
st.title("Sidebar Toggle System — WORKING VERSION")

# Toggle button
if st.button("Toggle Sidebar", type="primary"):
    st.session_state.sidebar_state = (
        "collapsed"
        if st.session_state.sidebar_state == "expanded"
        else "expanded"
    )
    st.experimental_rerun()

# Show current state
st.write("Sidebar state:", st.session_state.sidebar_state)

# Sidebar content
with st.sidebar:
    st.markdown("### Sidebar is OPEN")
