import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Neon Sidebar Control",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------
# SIDEBAR JS + BUTTON
# --------------------------

sidebar_html = """
<style>
/* purple neon close button */
#neon-btn-wrapper {
    position: absolute;
    top: 12px;
    right: 14px;
    z-index: 9999;
}

#neon-btn {
    background: #9b4dff;
    padding: 8px 16px;
    border-radius: 8px;
    border: none;
    font-weight: 700;
    color: white;
    cursor: pointer;
    box-shadow: 0 0 12px #b06fff, 0 0 22px #9b4dff;
}

#neon-btn:hover {
    box-shadow: 0 0 18px #d4a1ff, 0 0 28px #b06fff;
}
</style>

<div id="neon-btn-wrapper">
    <button id="neon-btn" onclick="neonClick()">✖ Close</button>
</div>

<script>
function neonClick() {
    // Send message to the Streamlit main frame
    window.parent.postMessage({ neonButton: "pressed" }, "*");
}
</script>
"""

# Inject sidebar content
components.html(sidebar_html, height=80)


# --------------------------
# LISTENER FOR NEON BUTTON
# --------------------------

listener_js = """
<script>
window.addEventListener("message", (event) => {
    if (event.data.neonButton === "pressed") {
        const params = new URLSearchParams(window.location.search);
        params.set("neon", "1");
        window.location.search = params.toString();
    }
});
</script>
"""

st.markdown(listener_js, unsafe_allow_html=True)


# --------------------------
# STREAMLIT RESPONSE
# --------------------------

params = st.experimental_get_query_params()
neon = params.get("neon", ["0"])[0]

if neon == "1":
    # CLOSE SIDEBAR JS
    close_js = """
    <script>
    const sb = window.parent.document.querySelector("section[data-testid='stSidebar']");
    if (sb) {
        sb.style.display = "none";
    }
    </script>
    """
    components.html(close_js, height=0)

    st.success("Neon close button activated, Major Tom.")
else:
    st.info("Press the purple neon button to close the sidebar, Major Tom.")


# --------------------------
# MAIN PAGE CONTENT
# --------------------------

st.title("Neon Sidebar Control Test")
st.write("Sidebar controls loaded.")
