import streamlit as st

st.set_page_config(layout="wide")

# Image URL (confirmed working)
IMG = (
    "https://raw.githubusercontent.com/eviltosh/"
    "button_project/main/assets/control.png"
)

# init state
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True

# toggle callbacks
def close_sidebar():
    st.session_state.sidebar_open = False

def open_sidebar():
    st.session_state.sidebar_open = True

# --- CSS (short lines, no super long lines) ---
css_lines = [
    "<style>",
    "[data-testid=\"stSidebar\"] {",
    "  background-image: url('" + IMG + "');",
    "  background-size: cover;",
    "  background-position: center;",
    "}",
    ".neon-close {",
    "  position: absolute;",
    "  top: 38px;",
    "  right: 28px;",
    "  padding: 10px 18px;",
    "  font-weight: 800;",
    "  color: white;",
    "  background: #9b00ff;",
    "  border-radius: 8px;",
    "  border: 2px solid #ff66ff;",
    "  box-shadow: 0 0 20px #9b00ff;",
    "  cursor: pointer;",
    "  z-index: 99999;",
    "}",
    ".neon-close:hover {",
    "  background: #c94dff;",
    "}",
    ".neon-open {",
    "  position: fixed;",
    "  top: 38px;",
    "  left: 38px;",
    "  padding: 10px 18px;",
    "  font-weight: 800;",
    "  color: white;",
    "  background: #00c957;",
    "  border-radius: 8px;",
    "  border: 2px solid #66ff99;",
    "  box-shadow: 0 0 20px #00ff66;",
    "  cursor: pointer;",
    "  z-index: 99999;",
    "}",
    ".neon-open:hover {",
    "  background: #33ff77;",
    "}",
    "</style>",
]
st.markdown("\n".join(css_lines), unsafe_allow_html=True)

# --- SIDEBAR: show purple button (HTML) that triggers hidden Streamlit button ---
if st.session_state.sidebar_open:
    with st.sidebar:
        # inject small HTML button that triggers an actual Streamlit button
        html_close = (
            "<button class='neon-close' "
            "onclick=\"document.getElementById('hidden_close').click()\">"
            "CLOSE</button>"
        )
        st.markdown(html_close, unsafe_allow_html=True)
        # the hidden Streamlit button does the real state change
        st.button("hidden_close", key="hidden_close", on_click=close_sidebar)

# --- OPEN button in main area: show only when sidebar closed ---
if not st.session_state.sidebar_open:
    html_open = (
        "<button class='neon-open' "
        "onclick=\"document.getElementById('hidden_open').click()\">"
        "OPEN SIDEBAR</button>"
    )
    st.markdown(html_open, unsafe_allow_html=True)
    st.button("hidden_open", key="hidden_open", on_click=open_sidebar)

# --- fallback: also provide visible Streamlit controls (for keyboard users) ---
# place small visible control buttons for accessibility
col1, col2 = st.columns([1, 8])
with col1:
    if st.button("Open", key="vis_open"):
        open_sidebar()
with col2:
    st.write("")  # spacer

# --- main content ---
st.title("Main App")
st.write("Sidebar toggle now uses stable Streamlit session state.")
st.write("Purple CLOSE (single click). Green OPEN (single click).")

# small debug info (remove when satisfied)
st.write("DEBUG: sidebar_open =", st.session_state.sidebar_open)
