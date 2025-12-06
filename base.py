import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(initial_sidebar_state="expanded")

# --------------------------------------------------------------
# JAVASCRIPT — brute force shut the sidebar
# --------------------------------------------------------------
close_sidebar_js = """
<script>
function forceCloseSidebar() {
    const parent = window.parent.document;

    // Streamlit sidebar container
    const sidebar = parent.querySelector('[data-testid="stSidebar"]');
    if (!sidebar) return;

    // Crush it
    sidebar.style.width = "0px";
    sidebar.style.minWidth = "0px";
    sidebar.style.maxWidth = "0px";
    sidebar.style.overflow = "hidden";
    sidebar.style.pointerEvents = "none";
}
</script>
"""
components.html(close_sidebar_js, height=0)

# --------------------------------------------------------------
# SIDEBAR UI
# --------------------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <style>
            .neon-btn {
                background: #a020f0;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
                font-weight: bold;
                box-shadow: 0 0 12px #c060ff, 0 0 20px #a020f0;
                cursor: pointer;
                margin-top: 15px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if st.button("✕ Close", key="close_sb"):
        components.html("<script>forceCloseSidebar()</script>", height=0)

# --------------------------------------------------------------
# MAIN VIEW
# --------------------------------------------------------------
st.write("Sidebar destruction protocol engaged, Major Tom.")
