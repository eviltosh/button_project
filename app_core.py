import streamlit as st

st.set_page_config(layout="wide", page_title="Neon Sidebar Toggle")

# --------------------------------------------------------
# STATE CONTROL
# --------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

params = st.query_params
if "sidebar" in params:
    st.session_state.sidebar_open = params.get("sidebar") == "1"

# --------------------------------------------------------
# CSS — PERFECT BUTTONS
# --------------------------------------------------------
st.markdown("""
<style>

body {
    overflow-x: hidden !important;
}

/* ================================================*
