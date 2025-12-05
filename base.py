import streamlit as st

# -------------------------
# SESSION STATE
# -------------------------
if "custom_sidebar_open" not in st.session_state:
    st.session_state.custom_sidebar_open = True


# -------------------------
# BASE CSS
# -------------------------
st.markdown("""
<style>

    /* --- Custom Sidebar Container --- */
    #custom-sidebar {
        position: fixed;
        top: 0;
        left: 0;
        width: 260px;
        height: 100vh;
        background: #111;
        border-right: 3px solid #3f0071;
        padding: 20px;
        transition: transform 0.3s ease-in-out;
        z-index: 9000;
        overflow-y: auto;
    }

    /* Hidden (collapsed) */
    #custom-sidebar.closed {
        transform: translateX(-110%);
    }

    /* Purple neon CLOSE button */
    .purple-btn {
        position: absolute;
        top: 10px;
        right: 10px;
    }
    .purple-btn button {
        background-color: #b300ff !important;
        color: white !important;
        border: 2px solid #ff00ff !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 0 12px #ff00ff !important;
    }

    /* Green neon OPEN button */
    #open-button-container {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 9500;
    }
    #open-button-container button {
        background-color: #00ff00 !important;
        color: black !important;
        border: 2px solid #00ffaa !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 0 12px #00ff00 !important;
    }

</style>
""", unsafe_allow_html=True)


# -------------------------
# CUSTOM SIDEBAR HTML
# -------------------------
sidebar_class = "" if st.session_state.custom_sidebar_open else "closed"

st.markdown(f"""
<div id="custom-sidebar" class="{sidebar_class}">
    <div class="purple-btn">
        <form action="#" method="get">
            <button name="close_btn" value="1">Close</button>
        </form>
    </div>

    <h2 style="color:white;">Custom Sidebar</h2>
    <p style="color:#ccc;">This sidebar is 100% under our control.</p>
</div>
""", unsafe_allow_html=True)


# -------------------------
# BUTTON HANDLING
# -------------------------
# CLOSE pressed
if "close_btn" in st.query_params:
    st.session_state.custom_sidebar_open = False
    st.query_params.clear()


# OPEN button (visible ONLY when closed)
if not st.session_state.custom_sidebar_open:
    st.markdown("""
        <div id="open-button-container">
            <form action="#" method="get">
                <button name="open_btn" value="1">Open</button>
            </form>
        </div>
    """, unsafe_allow_html=True)

# OPEN pressed
if "open_btn" in st.query_params:
    st.session_state.custom_sidebar_open = True
    st.query_params.clear()


# -------------------------
# MAIN CONTENT
# -------------------------
st.title("Custom Sidebar Prototype")
st.write("This version is **stable**. No hacks. No native sidebar. Full control.")
