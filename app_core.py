import streamlit as st

st.set_page_config(layout="wide", page_title="Neon Sidebar Toggle")

# ----------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True


# ----------------------------------------------------------
# CSS
# ----------------------------------------------------------
st.markdown("""
<style>

section[data-testid="stSidebar"] { display: none !important; }
div[data-testid="collapsedControl"] { display: none !important; }

/* Sidebar container */
.custom-sidebar {
    width: 360px;
    min-height: 100vh;
    padding: 24px 20px;
    background-image: url('https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    position: relative;
    color: white;
}

/* Main */
.main-content {
    flex: 1;
    padding: 24px;
}

/* Neon buttons */
.neon-btn {
    display: inline-block !important;
    text-decoration: none !important;
    color: #ffffff !important;
    background: linear-gradient(135deg, #9b00ff 0%, #b300ff 100%) !important;
    padding: 12px 20px !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    border-radius: 12px !important;
    box-shadow: 0 0 12px #b300ff, 0 0 28px rgba(179,0,255,0.7) !important;
    border: 2px solid #b300ff !important;
    z-index: 999999 !important;
    cursor: pointer;
}

.neon-btn:hover {
    transform: scale(1.05);
}

/* CLOSE button inside sidebar */
.sidebar-close {
    position: absolute !important;
    top: 18px !important;
    right: 18px !important;
}

/* OPEN button fixed */
.open-left {
    position: fixed !important;
    top: 20px !important;
    left: 20px !important;
    z-index: 999999 !important;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------------------------------------
# JAVASCRIPT (inserted cleanly)
# ----------------------------------------------------------
st.markdown("""
<script>

function openSide() {
    const url = new URL(window.location.href);
    url.searchParams.set("sidebar", "1");
    window.location.replace(url.toString());
}

function closeSide() {
    const url = new URL(window.location.href);
    url.searchParams.set("sidebar", "0");
    window.location.replace(url.toString());
}

</script>
""", unsafe_allow_html=True)


# ----------------------------------------------------------
# APPLY QUERY PARAM STATE
# ----------------------------------------------------------
params = st.query_params
if "sidebar" in params:
    st.session_state.sidebar_op
