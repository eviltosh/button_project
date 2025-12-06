import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(initial_sidebar_state="expanded")

# ---- CUSTOM JS TO CLOSE SIDEBAR ----
close_js = """
<script>
    function closeSidebar() {
        const sidebar = window.parent.document.querySelector("section[data-testid='stSidebar']");
        if (sidebar) {
            sidebar.style.display = 'none';
        }
    }
</script>
"""

# ---- DISPLAY JS ----
components.html(close_js, height=0, width=0)

# ---- SIDEBAR ----
with st.sidebar:
    st.markdown(
        """
        <style>
        .neon-close {
            position: absolute;
            top: 10px;
            right: 12px;
            background: #9b4dff;
            padding: 8px 14px;
            border-radius: 6px;
            font-weight: 700;
            cursor: pointer;
            color: white;
            box-shadow: 0 0 12px #b06fff;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Button that triggers JS
    clicked = st.button("✕ Close", key="close_button")

    if clicked:
        components.html("<script>closeSidebar()</script>", height=0, width=0)

# ---- MAIN PAGE ----
st.write("Sidebar loaded. Close button is active, Major Tom.")
