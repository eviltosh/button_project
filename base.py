import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(initial_sidebar_state="expanded")

# --------------------------------------------------------------
# JavaScript: Collapse the sidebar by simulating the built-in toggle button
# --------------------------------------------------------------
close_sidebar_js = """
<script>
function collapseSidebar() {
    const toggle = window.parent.document.querySelector(
        "button[title='Collapse sidebar']"
    );
    if (toggle) toggle.click();
}
</script>
"""

components.html(close_sidebar_js, height=0)

# --------------------------------------------------------------
# SIDEBAR CONTENT
# --------------------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <style>
        .neon-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background: #a020f0;
            color: white;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 0 10px #c060ff;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if st.button("✕ Close", key="close_sb"):
        components.html("<script>collapseSidebar()</script>", height=0)

# --------------------------------------------------------------
# MAIN PAGE
# --------------------------------------------------------------
st.write("Close button deployed, Major Tom. Sidebar collapse function active.")
