import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# --------------------------------------------------------
# INIT SESSION STATE
# --------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# --------------------------------------------------------
# JS CALLBACKS (RELIABLE FIRST-CLICK TOGGLE)
# --------------------------------------------------------
toggle_js = """
<script>
function toggle_sidebar(to_open) {
    // Call Streamlit's Python callback
    window.parent.postMessage(
        {type: "streamlit:setComponentValue", value: to_open}, "*"
    );
}
</script>
"""

# --------------------------------------------------------
# CSS (IMPROVED: CLEAN POSITIONING, NO DRIFT)
# --------------------------------------------------------
css = """
<style>

:root {
    --sidebar-width: 380px;
}

/* Sidebar background */
section[data-testid="stSidebar"] {
    background-image: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
    min-height: 100vh;
    padding-top: 20px;
}

/* Neon button shared styles */
.neon-btn {
    position: fixed;
    z-index: 999999;
    padding: 12px 26px;
    font-size: 15px;
    font-weight: bold;
    border-radius: 12px;
    border: none;
    cursor: pointer;
    color: #fff;
    background: linear-gradient(135deg, #9b00ff 0%, #b300ff 100%);
    box-shadow: 0 6px 20px rgba(179,0,255,0.32), 0 0 30px rgba(179,0,255,0.20) inset;
    transition: 0.15s ease;
}

/* Hover */
.neon-btn:hover {
    transform: translateY(-3px) scale(1.03);
}

/* OPEN button (appears when sidebar is CLOSED) */
#open-btn {
    top: 20px;
    left: 20px;
}

/* CLOSE button (inside sidebar top-right) */
#close-btn {
    top: 20px;
    left: calc(var(--sidebar-width) - 110px);
}

</style>
"""

# Inject CSS + JS
st.markdown(css, unsafe_allow_html=True)
components.html(toggle_js, height=0, width=0)

# --------------------------------------------------------
# PYTHON CALLBACK HANDLING
# --------------------------------------------------------
value = components.html(
    """
    <script>
        // placeholder to receive toggle commands
    </script>
    """,
    height=0,
)

# --------------------------------------------------------
# BUTTON RENDERING (NO DOUBLE CLICK)
# --------------------------------------------------------

# OPEN button (when sidebar is CLOSED)
if not st.session_state.sidebar_open:
    st.markdown(
        """<button id="open-btn" class="neon-btn" onclick="toggle_sidebar(true)">OPEN</button>""",
        unsafe_allow_html=True,
    )

# CLOSE button (when sidebar is OPEN)
else:
    st.markdown(
        """<button id="close-btn" class="neon-btn" onclick="toggle_sidebar(false)">CLOSE</button>""",
        unsafe_allow_html=True,
    )

# --------------------------------------------------------
# RECEIVE JS CALLBACK
# --------------------------------------------------------
clicked_value = st.experimental_get_query_params().get("component", None)

# Alternative: use custom Streamlit component channel
# Instead we use this: value is delivered via postMessage
# But we catch via session_state update
if value is not None:
    if isinstance(value, bool):
        st.session_state.sidebar_open = value

# --------------------------------------------------------
# PAGE CONTENT
# --------------------------------------------------------
st.title("Sidebar " + ("OPEN" if st.session_state.sidebar_open else "CLOSED"))

if st.session_state.sidebar_open:
    with st.sidebar:
        st.text_input("Example input")
        st.selectbox("Example select", ["One", "Two", "Three"])
        st.slider("Example slider", 0, 100, 25)
else:
    st.write("Sidebar is collapsed. Click OPEN to show it again.")
