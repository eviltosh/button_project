import streamlit as st

# ---- STATE ----
if "panel_open" not in st.session_state:
    st.session_state.panel_open = True

# ---- BASE CSS: Custom Left Panel ----
st.markdown(f"""
<style>

    /* MAIN CUSTOM PANEL */
    #panel {{
        position: fixed;
        top: 0;
        left: 0;
        width: 260px;
        height: 100vh;
        background: #111;
        border-right: 3px solid #b300ff;
        padding: 20px;
        transition: transform 0.3s ease;
        transform: translateX({ '0' if st.session_state.panel_open else '-105%' });
        z-index: 9000;
        overflow-y: auto;
    }}

    /* Purple CLOSE button inside panel (top-right) */
    #close-btn {{
        position: absolute;
        top: 10px;
        right: 10px;
    }}
    #close-btn button {{
        background-color: #b300ff !important;
        color: white !important;
        border: 2px solid #ff00ff !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 0 12px #ff00ff !important;
    }}

    /* Green OPEN button (top-right of screen) */
    #open-btn {{
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 9500;
        display: { 'none' if st.session_state.panel_open else 'block' };
    }}
    #open-btn button {{
        background-color: #00ff00 !important;
        color: black !important;
        border: 2px solid #00ffaa !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 0 12px #00ff00 !important;
    }}

</style>
""", unsafe_allow_html=True)

# ---- PANEL HTML ----
st.markdown("""
<div id="panel">
    <div id="close-btn">
        <form><button name="close" value="1">Close</button></form>
    </div>
    <h2 style="color:white;">Custom Panel</h2>
    <p style="color:#ccc;">Fully controllable sidebar replacement.</p>
</div>
""", unsafe_allow_html=True)

# ---- OPEN BUTTON ----
st.markdown("""
<div id="open-btn">
    <form><button name="open" value="1">Open</button></form>
</div>
""", unsafe_allow_html=True)

# ---- BUTTON LOGIC ----
qs = st.query_params
if "close" in qs:
    st.session_state.panel_open = False
    st.query_params.clear()
    st.rerun()

if "open" in qs:
    st.session_state.panel_open = True
    st.query_params.clear()
    st.rerun()

# ---- MAIN CONTENT ----
st.title("UNBREAKABLE CUSTOM SIDEBAR")
st.write("This is your new sidebar. It will NEVER break again.")
