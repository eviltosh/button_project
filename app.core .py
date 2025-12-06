import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(layout="wide")

# -----------------------------
# SESSION STATE
# -----------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True


# -----------------------------
# CALLBACKS
# -----------------------------
def close_sidebar():
    st.session_state.sidebar_open = False

def open_sidebar():
    st.session_state.sidebar_open = True


# =====================================================
# STABLE HTML-ID WRAPPERS FOR HIDDEN BUTTONS
# =====================================================
# We wrap the Streamlit button inside a <div id="...">
# so JS can reliably click it from your neon HTML buttons.
# =====================================================

def stable_hidden_button(id_html: str, label: str, key: str, callback):
    st.markdown(f'<div id="{id_html}">', unsafe_allow_html=True)
    st.button(label, key=key, on_click=callback)
    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# SIDEBAR CONTENT (when open)
# -----------------------------
if st.session_state.sidebar_open:

    # Full sidebar background image
    st.markdown("""
        <style>
        section[data-testid="stSidebar"] {
            background: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
            background-size: cover;
            background-position: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # -----------------------------
    # PURPLE CLOSE BUTTON (VISIBLE)
    # -----------------------------
    st.sidebar.markdown("""
        <button 
            onclick="document.querySelector('#hidden_close button').click();"
            style="
                background:#b300ff;
                color:white;
                padding:10px 20px;
                border:none;
                border-radius:6px;
                font-size:16px;
                margin-bottom:20px;
                cursor:pointer;
            ">
            CLOSE
        </button>
    """, unsafe_allow_html=True)

    # Hidden button with stable ID
    with st.sidebar:
        stable_hidden_button(
            id_html="hidden_close",
            label="hidden_close",
            key="hidden_close_key",
            callback=close_sidebar
        )

else:
    # -----------------------------
    # GREEN OPEN BUTTON (VISIBLE)
    # -----------------------------
    st.markdown("""
        <button 
            onclick="document.querySelector('#hidden_open button').click();"
            style="
                background:#00ff66;
                color:black;
                padding:10px 20px;
                border:none;
                border-radius:6px;
                font-size:16px;
                cursor:pointer;
            ">
            Open Sidebar
        </button>
    """, unsafe_allow_html=True)

    # Hidden button with stable ID
    stable_hidden_button(
        id_html="hidden_open",
        label="hidden_open",
        key="hidden_open_key",
        callback=open_sidebar
    )


# -----------------------------
# MAIN PAGE CONTENT
# -----------------------------
st.title("Main App")
st.write("Sidebar toggle uses **stable Streamlit session state**.")
st.write("Purple CLOSE = one click. Green OPEN = one click.")
st.write("DEBUG: sidebar_open =", st.session_state.sidebar_open)
