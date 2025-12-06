import streamlit as st

st.set_page_config(layout="wide")

# ==========================================================
# CSS — green open button (outside), purple close button (inside)
# ==========================================================
st.markdown("""
<style>
/* ---- GREEN OPEN BUTTON OUTSIDE ---- */
#open-sidebar-btn {
    position: fixed;
    top: 20px;
    left: 20px;
    z-index: 999999;
    padding: 10px 18px;
    background: #00ff9f;
    color: black;
    font-weight: 700;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    box-shadow: 0 0 12px #00ff9f;
}

/* ---- PURPLE CLOSE BUTTON INSIDE SIDEBAR ---- */
.neon-close-btn {
    background: #a200ff !important;
    color: white !important;
    font-weight: 800 !important;
    border-radius: 10px !important;
    border: 2px solid #ff00ff !important;
    box-shadow: 0 0 14px #c400ff !important;
}
</style>

<button id="open-sidebar-btn">OPEN SIDEBAR</button>

""", unsafe_allow_html=True)


# ==========================================================
# JAVASCRIPT — control sidebar expand / collapse
# ==========================================================
sidebar_js = """
<script>

function openSidebar() {
    const sidebar = window.parent.document.querySelector('section[data-testid="stSidebar"]');
    if (sidebar) {
        sidebar.style.transform = "translateX(0px)";
        sidebar.style.transition = "300ms";
    }
}

function closeSidebar() {
    const sidebar = window.parent.document.querySelector('section[data-testid="stSidebar"]');
    if (sidebar) {
        sidebar.style.transform = "translateX(-350px)";
        sidebar.style.transition = "300ms";
    }
}

document.getElementById("open-sidebar-btn").onclick = openSidebar;

</script>
"""
st.markdown(sidebar_js, unsafe_allow_html=True)


# ==========================================================
# SIDEBAR CONTENT — purple neon close button
# ==========================================================
with st.sidebar:
    st.markdown("### Sidebar Panel")

    # Purple neon collapse button (no rerun)
    close_clicked = st.button("CLOSE SIDEBAR", key="close_btn")

    if close_clicked:
        st.markdown(
            "<script>closeSidebar();</script>",
            unsafe_allow_html=True
        )


# ==========================================================
# MAIN PAGE
# ==========================================================
st.write("Main app loaded. Sidebar can be opened/closed.")
