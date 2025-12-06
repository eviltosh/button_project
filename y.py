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


# -----------------------------
# SIDEBAR CONTENT (when open)
# -----------------------------
if st.session_state.sidebar_open:
    
    # Inject background image for full sidebar coverage
    st.markdown("""
        <style>
        section[data-testid="stSidebar"] {
            background: url("https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png");
            background-size: cover;
            background-position: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Purple CLOSE button (visual)
    st.sidebar.markdown("""
        <button class="neon-close"
                onclick="document.getElementById('hidden_close').click();"
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

    # Hidden working close button
    st.sidebar.button("hidden_close", key="hidden_close", on_click=close_sidebar)

else:
    # -----------------------------
    # SHOW OPEN BUTTON ON MAIN PAGE
    # -----------------------------
    st.markdown("""
        <button class="neon-open"
                onclick="document.getElementById('hidden_open').click();"
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

    # Hidden working open button
    st.button("hidden_open", key="hidden_open", on_click=open_sidebar)


# -----------------------------
# MAIN PAGE CONTENT
# -----------------------------
st.title("Main App")
st.write("This version uses **pure Streamlit** and is stable on Cloud.")
st.write("Sidebar state:", st.session_state.sidebar_open)
