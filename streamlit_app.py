import streamlit as st

st.set_page_config(layout="wide")

# Background image URL
BG_URL = "https://raw.githubusercontent.com/eviltosh/button_project/main/assets/control.png"

# ----------------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True


# ----------------------------------------------------------------
# SIDEBAR (PURE STREAMLIT)
# ----------------------------------------------------------------
def render_sidebar():
    with st.sidebar:
        # Background image (in Markdown block)
        st.markdown(
            f"""
            <div style="
                width:100%;
                height:280px;
                background:url('{BG_URL}') center/cover no-repeat;
                border-radius:8px;
                margin-bottom:20px;
            ">
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")  # spacing

        # Purple native Streamlit button
        close_pressed = st.button(
            "Close Sidebar",
            use_container_width=True
        )
        if close_pressed:
            st.session_state.sidebar_open = False


# ----------------------------------------------------------------
# MAIN PAGE OPEN BUTTON
# ----------------------------------------------------------------
def render_open_button():
    open_pressed = st.button(
        "Open Sidebar",
        key="open_btn_main",
        type="primary",
    )
    if open_pressed:
        st.session_state.sidebar_open = True


# ----------------------------------------------------------------
# RENDER LOGIC
# ----------------------------------------------------------------
if st.session_state.sidebar_open:
    render_sidebar()
else:
    render_open_button()

# ----------------------------------------------------------------
# MAIN CONTENT
# ----------------------------------------------------------------
st.title("Main App")
st.write("This version uses **pure Streamlit** and will not break on Cloud.")
st.write("Sidebar state:", st.session_state.sidebar_open)
