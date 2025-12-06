import streamlit as st
from streamlit.components.v1 import html

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(layout="wide")

# ----------------------------------------------------
# SESSION STATE SETUP
# ----------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True


# ----------------------------------------------------
# CALLBACK FOR OPEN/CLOSE (Triggered by JS Messages)
# ----------------------------------------------------
def handle_js_message():
    """Reads messages from the JS bridge."""
    msg = st.session_state.get("js_msg")
    if msg == "close":
        st.session_state.sidebar_open = False
    elif msg == "open":
        st.session_state.sidebar_open = True
    st.session_state.js_msg = ""  # reset after handling


if "js_msg" not in st.session_state:
    st.session_state.js_msg = ""


# ----------------------------------------------------
# JS → PYTHON BRIDGE (IMPORTANT)
# ----------------------------------------------------
html("""
<script>
window.addEventListener("message", (event) => {
    if (event.data === "close") {
        window.parent.postMessage(
            {isStreamlitMessage: true, type: "streamlit:setComponentValue", value: "close"},
            "*"
        );
    }
    if (event.data === "open") {
        window.parent.postMessage(
            {isStreamlitMessage: true, type: "streamlit:setComponentValue", value: "open"},
            "*"
        );
    }
});
</script>
""", height=0, width=0)

# Component to receive messages
msg = st.experimental_get_query_params().get("componentValue", [""])[0]
if msg:
    st.session_state.js_msg = msg
    handle_js_message()


# ----------------------------------------------------
# SIDEBAR CONTENT (OPEN)
# ----------------------------------------------------
if st.session_state.sidebar_open:

    # Full neon background
    st.markdown("""
        <style>
        section[data-testid="stSidebar"] {
            background: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
            background-size: cover;
            background-position: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # PURPLE CLOSE BUTTON (ONE CLICK, WORKS)
    st.sidebar.markdown("""
        <button onclick="window.postMessage('close','*');"
            style="
                background:#b300ff;
                color:white;
                padding:12px 22px;
                border:none;
                border-radius:8px;
                font-size:18px;
                cursor:pointer;
                width:100%;
                margin-bottom:20px;
                box-shadow:0 0 12px #b300ff;
            ">
            CLOSE
        </button>
    """, unsafe_allow_html=True)


# ----------------------------------------------------
# MAIN PAGE OPEN BUTTON (WHEN SIDEBAR CLOSED)
# ----------------------------------------------------
else:
    st.markdown("""
        <button onclick="window.postMessage('open','*');"
            style="
                background:#00ff66;
                color:black;
                padding:12px 22px;
                border:none;
                border-radius:8px;
                font-size:18px;
                cursor:pointer;
                box-shadow:0 0 12px #00ff66;
            ">
            OPEN SIDEBAR
        </button>
    """, unsafe_allow_html=True)


# ----------------------------------------------------
# MAIN PAGE
# ----------------------------------------------------
st.title("Main App – Cloud-Safe Toggle System")
st.write("Sidebar open:", st.session_state.sidebar_open)
