# ====== INSTALL REQUIREMENT FIRST ======
# pip install streamlit-custom-sidebar streamlit-float

import streamlit as st
from streamlit_custom_sidebar import CustomSidebarDefault
import streamlit_float

# Page config
st.set_page_config(layout="wide")

# Initialize custom sidebar
streamlit_float.float_init(include_unstable_primary=False)

# Sidebar data (example — can be empty or customised)
data_ = [
    {"index": 0, "label": "Home", "page": "home", "href": "#"},
    {"index": 1, "label": "Settings", "page": "settings", "href": "#"}
]

if "currentPage" not in st.session_state:
    st.session_state["currentPage"] = data_[0]
else:
    st.session_state["currentPage"] = data_[0]

# Render custom sidebar
with st.container():
    custom = CustomSidebarDefault(
        closeNavOnLoad=False,
        backgroundColor="#111",
        loadPageName="home",
        data=data_,
        LocalOrSessionStorage=1,
        serverRendering=False,
        webMedium="local"
    )
    custom.load_custom_sidebar()
    custom.change_page()
    streamlit_float.float_parent(css="position:fixed; top:-1000px;")

# Now inject open/close buttons manually at precise positions
st.markdown("""
<style>
/* Purple neon close button — top right of sidebar panel */
#sidebar-close-button button {
    position: absolute;
    top: 10px;
    right: 10px;
    background-color: #b300ff !important;
    color: white !important;
    border: 2px solid #ff00ff !important;
    border-radius: 8px !important;
    font-weight: bold !important;
    box-shadow: 0 0 10px #ff00ff !important;
    z-index: 10000;
}
/* Green neon open button — top right of main page */
#sidebar-open-button button {
    position: fixed;
    top: 10px;
    right: 10px;
    background-color: #00ff00 !important;
    color: black !important;
    border: 2px solid #00ffaa !important;
    border-radius: 8px !important;
    font-weight: bold !important;
    box-shadow: 0 0 10px #00ff00 !important;
    z-index: 10000;
}
</style>
""", unsafe_allow_html=True)

# Show open/close buttons based on sidebar state
if custom.is_sidebar_visible():
    st.markdown('<div id="sidebar-close-button"><button id="close">Close Sidebar</button></div>', unsafe_allow_html=True)
else:
    st.markdown('<div id="sidebar-open-button"><button id="open">Open Sidebar</button></div>', unsafe_allow_html=True)

# Listen to button clicks via query params — simple but workable
params = st.experimental_get_query_params()
if "open" in params:
    custom.show()
    st.experimental_set_query_params()
    st.experimental_rerun()
if "close" in params:
    custom.hide()
    st.experimental_set_query_params()
    st.experimental_rerun()

# Main content
st.title("Custom Sidebar with Reliable Toggle")
st.write("Using a third-party sidebar component for full control.")
